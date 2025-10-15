"""
API Client for sentiment prediction
"""
import requests
from typing import Dict, Any, Optional
from src.config import Config


class APIClient:
    """Client for interacting with the sentiment analysis API"""
    
    def __init__(self, base_url: Optional[str] = None):
        """
        Initialize API client
        
        Args:
            base_url: Base URL of the API. If None, uses config default.
        """
        self.base_url = base_url or Config.get_api_url()
        self.timeout = Config.get_timeout()
    
    def check_health(self) -> Dict[str, Any]:
        """
        Check API health status
        
        Returns:
            Dict containing status information
        
        Raises:
            requests.RequestException: If the request fails
        """
        try:
            response = requests.get(
                f"{self.base_url}/",
                timeout=2
            )
            response.raise_for_status()
            return {
                "status": "connected",
                "status_code": response.status_code,
                "message": "API connectée avec succès"
            }
        except requests.Timeout:
            return {
                "status": "timeout",
                "status_code": None,
                "message": "Timeout de connexion à l'API"
            }
        except requests.ConnectionError:
            return {
                "status": "error",
                "status_code": None,
                "message": "Impossible de se connecter à l'API"
            }
        except Exception as e:
            return {
                "status": "error",
                "status_code": None,
                "message": f"Erreur: {str(e)}"
            }
    
    def predict_sentiment(self, text: str) -> Dict[str, Any]:
        """
        Predict sentiment of a text
        
        Args:
            text: Text to analyze
            
        Returns:
            Dict containing prediction results
            
        Raises:
            requests.RequestException: If the request fails
        """
        response = requests.post(
            f"{self.base_url}/predict",
            json={"text": text},
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()
    
    def explain_prediction(self, text: str) -> Dict[str, Any]:
        """
        Get LIME explanation for a prediction
        
        Args:
            text: Text to explain
            
        Returns:
            Dict containing explanation results
            
        Raises:
            requests.RequestException: If the request fails
        """
        response = requests.post(
            f"{self.base_url}/explain",
            json={"text": text},
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()
