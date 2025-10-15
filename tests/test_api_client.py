"""
Unit tests for API Client
"""
import pytest
from unittest.mock import Mock, patch
from src.api_client import APIClient
from src.config import Config


class TestAPIClient:
    """Test suite for APIClient"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.client = APIClient()
    
    def test_init_with_default_url(self):
        """Test initialization with default URL"""
        client = APIClient()
        assert client.base_url == Config.API_URL
        assert client.timeout == Config.API_TIMEOUT
    
    def test_init_with_custom_url(self):
        """Test initialization with custom URL"""
        custom_url = "http://custom-api.com"
        client = APIClient(base_url=custom_url)
        assert client.base_url == custom_url
    
    @patch('src.api_client.requests.get')
    def test_check_health_success(self, mock_get):
        """Test successful health check"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        
        result = self.client.check_health()
        
        assert result["status"] == "connected"
        assert result["status_code"] == 200
        assert "succès" in result["message"].lower()
    
    @patch('src.api_client.requests.get')
    def test_check_health_timeout(self, mock_get):
        """Test health check timeout"""
        from requests import Timeout
        mock_get.side_effect = Timeout()
        
        result = self.client.check_health()
        
        assert result["status"] == "timeout"
        assert "timeout" in result["message"].lower()
    
    @patch('src.api_client.requests.get')
    def test_check_health_connection_error(self, mock_get):
        """Test health check connection error"""
        from requests import ConnectionError
        mock_get.side_effect = ConnectionError()
        
        result = self.client.check_health()
        
        assert result["status"] == "error"
        assert "connecter" in result["message"].lower()
    
    @patch('src.api_client.requests.post')
    def test_predict_sentiment_success(self, mock_post):
        """Test successful sentiment prediction"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "sentiment": "positive",
            "confidence": 0.95,
            "polarity": "positive"
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response
        
        result = self.client.predict_sentiment("I love this!")
        
        assert result["sentiment"] == "positive"
        assert result["confidence"] == 0.95
        mock_post.assert_called_once()
    
    @patch('src.api_client.requests.post')
    def test_predict_sentiment_error(self, mock_post):
        """Test sentiment prediction error"""
        from requests import RequestException
        mock_post.side_effect = RequestException("API Error")
        
        with pytest.raises(RequestException):
            self.client.predict_sentiment("Test text")
    
    @patch('src.api_client.requests.post')
    def test_explain_prediction_success(self, mock_post):
        """Test successful LIME explanation"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "explanation": "Test explanation",
            "image": "base64_image_data"
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response
        
        result = self.client.explain_prediction("Test text")
        
        assert "explanation" in result
        assert "image" in result
        mock_post.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
