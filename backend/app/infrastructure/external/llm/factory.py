from app.core.config import get_settings
from app.infrastructure.external.llm.openai_llm import OpenAILLM
from app.infrastructure.external.llm.gemini_llm import GeminiLLM
from app.infrastructure.external.llm.ollama_llm import OllamaLLM
from app.domain.external.llm import LLM

def get_llm() -> LLM:
    """Factory function to get the configured LLM instance"""
    settings = get_settings()
    provider = settings.llm_provider.lower()
    
    if provider == "openai":
        return OpenAILLM()
    elif provider == "gemini":
        return GeminiLLM()
    elif provider == "ollama":
        return OllamaLLM()
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
