import requests
import json
from datetime import datetime, timedelta

class DiscourseToWikiSync:
    def __init__(self, discourse_url, wiki_url, api_key):
        self.discourse_url = discourse_url
        self.wiki_url = wiki_url
        self.api_key = api_key
        self.headers = {'Api-Key': api_key, 'Content-Type': 'application/json'}
    
    def get_recent_topics(self, days=1):
        """Get recent topics from Discourse"""
        url = f"{self.discourse_url}/latest.json"
        response = requests.get(url)
        if response.status_code == 200:
            topics = response.json()['topic_list']['topics']
            recent_topics = []
            cutoff_date = datetime.now() - timedelta(days=days)
            for topic in topics:
                created_at = datetime.fromisoformat(topic['created_at'].replace('Z', '+00:00'))
                if created_at >= cutoff_date:
                    recent_topics.append(topic)
            return recent_topics
        return []
    
    def get_topic_posts(self, topic_id):
        """Get all posts from a topic"""
        url = f"{self.discourse_url}/t/{topic_id}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['post_stream']['posts']
        return []
    
    def create_wiki_page(self, title, content):
        """Create a new page in MediaWiki"""
        # This would use MediaWiki API with proper authentication
        # Implementation depends on wiki authentication setup
        print(f"Creating wiki page: {title}")
        # In production, would use requests to MediaWiki API
        # with proper edit tokens and authentication
        return True
    
    def extract_key_insights(self, posts):
        """Extract key insights from discussion posts"""
        # This would use AI to summarize and extract key points
        # For now, returns a simple compilation
        content = """{{/Template:DiscussionSummary}}\n\n== Summary ==\n"""
        
        for i, post in enumerate(posts):
            if i == 0:
                # First post is usually the main content
                content += f"\n{post['cooked']}\n"
            else:
                # Subsequent posts are comments/replies
                username = post['username']
                cooked = post['cooked']
                content += f"\n=== Response from {username} ===\n{cooked}\n"
        
        content += """\n\n== References ==\n{{/References}}\n\n[[Category:Discourse Sync]]"""
        return content
    
    def sync_recent_discussions(self):
        """Main method to sync recent discussions to wiki"""
        print(f"Starting sync process at {datetime.now()}")
        
        # Get recent topics
        topics = self.get_recent_topics(days=1)
        print(f"Found {len(topics)} recent topics")
        
        synced_count = 0
        for topic in topics:
            # Skip topics that are likely not technical content
            if any(word in topic['title'].lower() for word in ['meta', 'staff', 'admin', 'help', 'support']):
                continue
                
            # Skip RSS feed topics
            if topic['category_id'] in [60, 61]:  # RSS Feeds category
                continue
            
            print(f"Processing: {topic['title']}")
            
            # Get all posts in the topic
            posts = self.get_topic_posts(topic['id'])
            
            if len(posts) > 0:
                # Extract key insights
                content = self.extract_key_insights(posts)
                
                # Create wiki page
                title = f"Discussion:{topic['title']}".replace(' ', '_')
                if self.create_wiki_page(title, content):
                    synced_count += 1
                    print(f"Successfully synced: {title}")
                
        print(f"Sync completed. {synced_count} discussions synced.")
        return synced_count

# Configuration would come from environment variables or secrets
# DISCOURSE_URL = os.getenv('DISCOURSE_URL')
# WIKI_URL = os.getenv('WIKI_URL')
# API_KEY = os.getenv('DISCOURSE_API_KEY')

# Usage:
# sync = DiscourseToWikiSync(DISCOURSE_URL, WIKI_URL, API_KEY)
# sync.sync_recent_discussions()