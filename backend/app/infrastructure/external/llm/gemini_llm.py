from typing import List, Dict, Any, Optional
import google.generativeai as genai
from app.domain.external.llm import LLM
from app.core.config import get_settings
import logging
import asyncio

logger = logging.getLogger(__name__)

class GeminiLLM(LLM):
    def __init__(self):
        settings = get_settings()
        genai.configure(api_key=settings.gemini_api_key)
        self._model_name = settings.gemini_model_name or "gemini-1.5-pro"
        self.model = genai.GenerativeModel(self._model_name)
        self._temperature = settings.temperature
        self._max_tokens = settings.max_tokens
        logger.info(f"Initialized Gemini LLM with model: {self._model_name}")
    
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
        """Send chat request to Gemini API"""
        
        # Convert messages to Gemini format
        contents = []
        for msg in messages:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({"role": role, "parts": [msg["content"]]})
            
        try:
            generation_config = {
                "temperature": self._temperature,
                "max_output_tokens": self._max_tokens,
            }
            
            # Handle tools if provided
            gemini_tools = []
            if tools:
                for tool in tools:
                    if "function" in tool:
                        func = tool["function"]
                        gemini_tools.append({
                            "function_declarations": [{
                                "name": func["name"],
                                "description": func["description"],
                                "parameters": func["parameters"]
                            }]
                        })

            response = await asyncio.to_thread(
                self.model.generate_content,
                contents,
                generation_config=generation_config,
                tools=gemini_tools if gemini_tools else None
            )
            
            return {
                "role": "assistant",
                "content": response.text
            }
            
        except Exception as e:
            logger.error(f"Error calling Gemini API: {str(e)}")
            raise e
