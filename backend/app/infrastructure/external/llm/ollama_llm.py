from typing import List, Dict, Any, Optional
import httpx
from app.domain.external.llm import LLM
from app.core.config import get_settings
import logging
import json

logger = logging.getLogger(__name__)

class OllamaLLM(LLM):
    def __init__(self):
        settings = get_settings()
        self.base_url = settings.ollama_base_url or "http://localhost:11434"
        self._model_name = settings.ollama_model_name or "llama3"
        self._temperature = settings.temperature
        self._max_tokens = settings.max_tokens
        logger.info(f"Initialized Ollama LLM with model: {self._model_name} at {self.base_url}")
    
    @property
    def model_name(self) -> str:
        return self._model_name
    
    @property
    def temperature(self) -> float:
        return self._temperature
    
    @property
    def max_tokens(self) -> int:
        return self._max_tokens
    
    async def ask(self, messages: List[Dict[str, str]],
                tools: Optional[List[Dict[str, Any]]] = None,
                response_format: Optional[Dict[str, Any]] = None,
                tool_choice: Optional[str] = None) -> Dict[str, Any]:
        """Send chat request to Ollama API"""
        
        payload = {
            "model": self._model_name,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": self._temperature,
                "num_predict": self._max_tokens
            }
        }
        
        if response_format and response_format.get("type") == "json_object":
            payload["format"] = "json"
            
        if tools:
            # Ollama supports tools in newer versions
            payload["tools"] = tools

        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    f"{self.base_url}/api/chat",
                    json=payload
                )
                response.raise_for_status()
                result = response.json()
                
                return result["message"]
                
        except Exception as e:
            logger.error(f"Error calling Ollama API: {str(e)}")
            raise e
