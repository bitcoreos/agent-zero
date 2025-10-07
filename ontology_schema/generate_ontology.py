"""Generate ontology artifacts from the semantic mesh manifest."""
from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = REPO_ROOT / "semantic_mesh" / "mesh_manifest.yaml"
OUTPUT_TTL = REPO_ROOT / "ontology_schema" / "mesh_ontology.ttl"
OUTPUT_JSONLD = REPO_ROOT / "ontology_schema" / "mesh_ontology.jsonld"

BASE_NODE = "urn:mesh:node/"
BASE_OWNER = "urn:mesh:owner/"
BASE_ARTIFACT = "urn:mesh:artifact/"
BASE_PROP = "urn:mesh:prop/"
BASE_REL = "urn:mesh:relation/"
BASE_CLASS = "urn:mesh:class/"

PREFIXES = OrderedDict([
    ("@base", "urn:mesh:"),
    ("meshnode", BASE_NODE),
    ("meshowner", BASE_OWNER),
    ("meshart", BASE_ARTIFACT),
    ("meshprop", BASE_PROP),
    ("meshrel", BASE_REL),
    ("meshclass", BASE_CLASS),
    ("dct", "http://purl.org/dc/terms/"),
    ("schema", "http://schema.org/"),
    ("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
    ("rdfs", "http://www.w3.org/2000/01/rdf-schema#"),
])


class Artifact:
    """Normalized representation of an artifact entry."""

    def __init__(self, path: str, sha256: str, section: Optional[str] = None) -> None:
        self.path = path
        self.sha256 = sha256
        self.section = section
        self.slug = slugify(path)

    @property
    def iri(self) -> str:
        return f"{BASE_ARTIFACT}{self.slug}"

    def ttl_block(self) -> List[str]:
        lines = [f"meshart:{self.slug} a meshclass:MeshArtifact ;"]
        lines.append(f"  meshprop:path {turtle_literal(self.path)} ;")
        lines.append(f"  meshprop:sha256 {turtle_literal(self.sha256)}")
        if self.section:
            lines[-1] += " ;"
            lines.append(f"  meshprop:section {turtle_literal(self.section)}")
        lines[-1] += " ."
        return lines

    def jsonld_object(self) -> Dict[str, object]:
        obj: Dict[str, object] = {
            "@id": self.iri,
            "@type": "MeshArtifact",
            "path": self.path,
            "sha256": self.sha256,
        }
        if self.section:
            obj["section"] = self.section
        return obj


class Owner:
    """Owner role entry."""

    def __init__(self, owner_id: str, label: str) -> None:
        self.owner_id = owner_id
        self.label = label

    @property
    def slug(self) -> str:
        return slugify(self.owner_id)

    @property
    def iri(self) -> str:
        return f"{BASE_OWNER}{self.owner_id}"

    def ttl_block(self) -> List[str]:
        return [
            f"meshowner:{self.owner_id} a meshclass:MeshOwner ;",
            f"  rdfs:label {turtle_literal(self.label)} .",
        ]

    def jsonld_object(self) -> Dict[str, object]:
        return {
            "@id": self.iri,
            "@type": "MeshOwner",
            "rdfs:label": self.label,
        }


class Node:
    """Semantic mesh node."""

    def __init__(
        self,
        node_id: str,
        title: str,
        summary: str,
        definition: Optional[str],
        owner: str,
        artifacts: Iterable[Artifact],
        related: Iterable[str],
        ontology_term: Optional[str],
    ) -> None:
        self.node_id = node_id
        self.title = title
        self.summary = summary
        self.definition = definition
        self.owner = owner
        self.artifacts = list(artifacts)
        self.related = list(related)
        self.ontology_term = ontology_term or f"{BASE_NODE}{node_id}"

    @property
    def iri(self) -> str:
        return self.ontology_term

    def ttl_block(self) -> List[str]:
        lines = [f"meshnode:{self.node_id} a meshclass:MeshNode ;"]
        lines.append(f"  dct:title {turtle_literal(self.title)} ;")
        lines.append(f"  schema:description {turtle_literal(self.summary)} ;")
        if self.definition:
            lines.append(f"  meshprop:definition {turtle_literal(self.definition)} ;")
        lines.append(f"  meshprop:hasOwner meshowner:{self.owner} ;")
        if self.artifacts:
            for art in self.artifacts[:-1]:
                lines.append(f"  meshprop:hasArtifact meshart:{art.slug} ;")
            lines.append(f"  meshprop:hasArtifact meshart:{self.artifacts[-1].slug} ;")
        if self.related:
            for rel in self.related[:-1]:
                lines.append(f"  meshprop:relatedTo meshnode:{rel} ;")
            lines.append(f"  meshprop:relatedTo meshnode:{self.related[-1]} ;")
        lines.append(f"  meshprop:manifestPath {turtle_literal('semantic_mesh/mesh_manifest.yaml')} .")
        return lines

    def jsonld_object(self) -> Dict[str, object]:
        obj: Dict[str, object] = {
            "@id": self.iri,
            "@type": "MeshNode",
            "title": self.title,
            "summary": self.summary,
            "hasOwner": f"{BASE_OWNER}{self.owner}",
            "manifestPath": "semantic_mesh/mesh_manifest.yaml",
        }
        if self.definition:
            obj["definition"] = self.definition
        if self.artifacts:
            obj["hasArtifact"] = [artifact.iri for artifact in self.artifacts]
        if self.related:
            obj["relatedTo"] = [f"{BASE_NODE}{rel}" for rel in self.related]
        return obj


def slugify(value: str) -> str:
    value = value.strip().replace("/", "_")
    value = re.sub(r"[^A-Za-z0-9_]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value.lower() or "root"


def turtle_literal(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace("\"", '\\"')
    return f'"{escaped}"'


def build_artifacts(nodes_raw: Iterable[dict]) -> Dict[Tuple[str, Optional[str]], Artifact]:
    artifact_map: Dict[Tuple[str, Optional[str]], Artifact] = {}
    for node in nodes_raw:
        for art in node.get("artifacts", []):
            path = art["path"]
            sha = art.get("sha256")
            if sha is None:
                raise ValueError(f"Missing sha256 for artifact path: {path}")
            section = art.get("section")
            key = (path, section)
            if key in artifact_map:
                continue
            artifact_map[key] = Artifact(path=path, sha256=sha, section=section)
    return artifact_map


def load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"Manifest not found at {MANIFEST_PATH}")
    with MANIFEST_PATH.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def build_nodes(manifest: dict, artifacts: Dict[Tuple[str, Optional[str]], Artifact]) -> List[Node]:
    nodes: List[Node] = []
    for node in manifest.get("nodes", []):
        node_artifacts = []
        for art in node.get("artifacts", []):
            key = (art["path"], art.get("section"))
            node_artifacts.append(artifacts[key])
        nodes.append(
            Node(
                node_id=node["id"],
                title=node["title"],
                summary=node["summary"],
                definition=node.get("definition"),
                owner=node["owner"],
                artifacts=node_artifacts,
                related=node.get("related", []),
                ontology_term=node.get("ontology_term"),
            )
        )
    return nodes


def build_ttl(
    manifest: dict,
    nodes: List[Node],
    artifacts: Dict[Tuple[str, Optional[str]], Artifact],
) -> str:
    lines: List[str] = ["# Generated from semantic_mesh/mesh_manifest.yaml"]
    for prefix, iri in PREFIXES.items():
        if prefix == "@base":
            lines.append(f"@base <{iri}> .")
        else:
            lines.append(f"@prefix {prefix}: <{iri}> .")
    lines.append("")

    # Class definitions
    lines.extend([
        "meshclass:MeshNode a rdfs:Class ;",
        "  rdfs:label \"Mesh Node\" .",
        "",
        "meshclass:MeshArtifact a rdfs:Class ;",
        "  rdfs:label \"Mesh Artifact\" .",
        "",
        "meshclass:MeshOwner a rdfs:Class ;",
        "  rdfs:label \"Mesh Owner\" .",
        "",
        "meshclass:MeshRelation a rdfs:Class ;",
        "  rdfs:label \"Mesh Relation\" .",
        "",
    ])

    # Property definitions
    property_blocks = [
        ("hasOwner", "MeshNode", "MeshOwner", "Associates a mesh node with its accountable owner."),
        ("hasArtifact", "MeshNode", "MeshArtifact", "Links a mesh node to supporting evidence artifacts."),
        ("relatedTo", "MeshNode", "MeshNode", "Generic relationship between mesh nodes."),
    ("manifestPath", "MeshNode", None, "Indicates the manifest file that defined the node."),
    ("definition", "MeshNode", None, "Canonical ontological definition of the mesh node."),
        ("path", "MeshArtifact", None, "Filesystem path of the artifact."),
        ("sha256", "MeshArtifact", None, "SHA-256 checksum recorded in the manifest."),
        ("section", "MeshArtifact", None, "Optional section anchor within the artifact."),
    ]
    for prop, domain, range_, comment in property_blocks:
        lines.append(f"meshprop:{prop} a rdf:Property ;")
        lines.append(f"  rdfs:label {turtle_literal(prop)} ;")
        lines.append(f"  rdfs:comment {turtle_literal(comment)} ;")
        if domain:
            lines.append(f"  rdfs:domain meshclass:{domain} ;")
        if range_:
            lines.append(f"  rdfs:range meshclass:{range_} ;")
        lines[-1] = lines[-1].rstrip(" ;") + " ."
        lines.append("")

    relation_types = sorted({rel["type"] for rel in manifest.get("relations", [])})
    for rel_type in relation_types:
        lines.append(f"meshrel:{rel_type} a rdf:Property ;")
        lines.append(f"  rdfs:label {turtle_literal(rel_type)} ;")
        lines.append("  rdfs:subPropertyOf meshprop:relatedTo ;")
        lines.append("  rdfs:domain meshclass:MeshNode ;")
        lines.append("  rdfs:range meshclass:MeshNode .")
        lines.append("")

    # Owners
    owners = [Owner(owner_id, label) for owner_id, label in manifest.get("owners", {}).items()]
    for owner in owners:
        lines.extend(owner.ttl_block())
        lines.append("")

    # Artifacts
    for artifact in sorted(artifacts.values(), key=lambda a: a.slug):
        lines.extend(artifact.ttl_block())
        lines.append("")

    # Nodes
    for node in nodes:
        lines.extend(node.ttl_block())
        lines.append("")

    # Relations
    for rel in manifest.get("relations", []):
        source = rel["source"]
        target = rel["target"]
        rel_type = rel["type"]
        lines.append(f"meshnode:{source} meshrel:{rel_type} meshnode:{target} .")
    lines.append("")

    return "\n".join(lines)


def build_jsonld(
    manifest: dict,
    nodes: List[Node],
    artifacts: Dict[Tuple[str, Optional[str]], Artifact],
) -> dict:
    relation_types = sorted({rel["type"] for rel in manifest.get("relations", [])})
    context: Dict[str, object] = {
        "meshnode": BASE_NODE,
        "meshowner": BASE_OWNER,
        "meshart": BASE_ARTIFACT,
        "meshprop": BASE_PROP,
        "meshrel": BASE_REL,
        "MeshNode": f"{BASE_CLASS}MeshNode",
        "MeshArtifact": f"{BASE_CLASS}MeshArtifact",
        "MeshOwner": f"{BASE_CLASS}MeshOwner",
        "MeshRelation": f"{BASE_CLASS}MeshRelation",
        "title": "http://purl.org/dc/terms/title",
        "summary": "http://purl.org/dc/terms/abstract",
        "path": "urn:mesh:prop/path",
        "sha256": "urn:mesh:prop/sha256",
        "section": "urn:mesh:prop/section",
        "manifestPath": "urn:mesh:prop/manifestPath",
    "definition": "urn:mesh:prop/definition",
        "schema": "http://schema.org/",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "hasOwner": {"@id": "urn:mesh:prop/hasOwner", "@type": "@id"},
        "hasArtifact": {"@id": "urn:mesh:prop/hasArtifact", "@type": "@id"},
        "relatedTo": {"@id": "urn:mesh:prop/relatedTo", "@type": "@id"},
    }
    for rel_type in relation_types:
        context[rel_type] = {"@id": f"{BASE_REL}{rel_type}", "@type": "@id"}

    graph: List[Dict[str, object]] = []

    # Class definitions
    graph.extend(
        [
            {"@id": f"{BASE_CLASS}MeshNode", "@type": "rdfs:Class", "rdfs:label": "Mesh Node"},
            {"@id": f"{BASE_CLASS}MeshArtifact", "@type": "rdfs:Class", "rdfs:label": "Mesh Artifact"},
            {"@id": f"{BASE_CLASS}MeshOwner", "@type": "rdfs:Class", "rdfs:label": "Mesh Owner"},
            {"@id": f"{BASE_CLASS}MeshRelation", "@type": "rdfs:Class", "rdfs:label": "Mesh Relation"},
        ]
    )

    # Property definitions
    property_defs = [
        ("hasOwner", "MeshNode", "MeshOwner", "Associates a mesh node with its accountable owner."),
        ("hasArtifact", "MeshNode", "MeshArtifact", "Links a mesh node to supporting evidence artifacts."),
        ("relatedTo", "MeshNode", "MeshNode", "Generic relationship between mesh nodes."),
        ("manifestPath", "MeshNode", None, "Indicates the manifest file that defined the node."),
        ("path", "MeshArtifact", None, "Filesystem path of the artifact."),
        ("sha256", "MeshArtifact", None, "SHA-256 checksum recorded in the manifest."),
        ("section", "MeshArtifact", None, "Optional section anchor within the artifact."),
    ]
    for prop, domain, range_, comment in property_defs:
        prop_obj: Dict[str, object] = {
            "@id": f"{BASE_PROP}{prop}",
            "@type": "rdf:Property",
            "rdfs:label": prop,
            "rdfs:comment": comment,
        }
        if domain:
            prop_obj["rdfs:domain"] = f"{BASE_CLASS}{domain}"
        if range_:
            prop_obj["rdfs:range"] = f"{BASE_CLASS}{range_}"
        graph.append(prop_obj)

    for rel_type in relation_types:
        graph.append(
            {
                "@id": f"{BASE_REL}{rel_type}",
                "@type": "rdf:Property",
                "rdfs:label": rel_type,
                "rdfs:subPropertyOf": f"{BASE_PROP}relatedTo",
                "rdfs:domain": f"{BASE_CLASS}MeshNode",
                "rdfs:range": f"{BASE_CLASS}MeshNode",
            }
        )

    # Owners
    for owner_id, label in manifest.get("owners", {}).items():
        graph.append({
            "@id": f"{BASE_OWNER}{owner_id}",
            "@type": "MeshOwner",
            "rdfs:label": label,
        })

    # Artifacts
    for artifact in sorted(artifacts.values(), key=lambda a: a.slug):
        graph.append(artifact.jsonld_object())

    # Nodes
    for node in nodes:
        graph.append(node.jsonld_object())

    # Relations
    for rel in manifest.get("relations", []):
        graph.append(
            {
                "@id": f"{BASE_NODE}{rel['source']}#{rel['type']}#{rel['target']}",
                "@type": "MeshRelation",
                "schema:source": f"{BASE_NODE}{rel['source']}",
                "schema:target": f"{BASE_NODE}{rel['target']}",
                rel["type"]: f"{BASE_NODE}{rel['target']}",
            }
        )

    return {"@context": context, "@graph": graph}


def main() -> None:
    manifest = load_manifest()
    artifacts = build_artifacts(manifest.get("nodes", []))
    nodes = build_nodes(manifest, artifacts)
    ttl = build_ttl(manifest, nodes, artifacts)
    OUTPUT_TTL.write_text(ttl, encoding="utf-8")
    jsonld = build_jsonld(manifest, nodes, artifacts)
    OUTPUT_JSONLD.write_text(json.dumps(jsonld, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {OUTPUT_TTL.relative_to(REPO_ROOT)}")
    print(f"Wrote {OUTPUT_JSONLD.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
