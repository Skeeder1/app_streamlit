"""
Configuration module for Twitter Sentiment Analyzer
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration"""
    
    # API Configuration
    API_URL = os.getenv("API_URL", "http://localhost:8003")
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))
    
    # Application Settings
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    MAX_TWEET_LENGTH = int(os.getenv("MAX_TWEET_LENGTH", "280"))
    DEFAULT_EXAMPLES_COUNT = int(os.getenv("DEFAULT_EXAMPLES_COUNT", "5"))
    
    # Page Configuration
    PAGE_TITLE = "Twitter Sentiment Analyzer"
    PAGE_ICON = "🐦"
    LAYOUT = "wide"
    
    # Theme Colors
    PRIMARY_COLOR = "#0ea5e9"
    SECONDARY_COLOR = "#1e293b"
    ACCENT_COLOR = "#ec8f1a"
    
    # Examples
    TWEET_EXAMPLES = [
        "I love this product! It's amazing! 😍",
        "This is the worst experience ever. Very disappointed.",
        "The weather is nice today.",
        "I'm not sure how I feel about this...",
        "Absolutely fantastic! Best day of my life! 🎉"
    ]
    
    @classmethod
    def get_api_url(cls) -> str:
        """Get the API URL"""
        return cls.API_URL
    
    @classmethod
    def get_timeout(cls) -> int:
        """Get the API timeout"""
        return cls.API_TIMEOUT
