from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional


class Settings(BaseSettings):
    
    # Model provider configuration
    llm_provider: str = "openai"  # "openai", "gemini", "ollama"
    api_key: Optional[str] = None
    api_base: str = "https://api.deepseek.com/v1"
    
    # Gemini configuration
    gemini_api_key: Optional[str] = None
    gemini_model_name: str = "gemini-1.5-pro"
    
    # Ollama configuration
    ollama_base_url: str = "http://localhost:11434"
    ollama_model_name: str = "llama3"
    
    # Model configuration
    model_name: str = "deepseek-chat"
    temperature: float = 0.7
    max_tokens: int = 2000
    
    # MongoDB configuration
    mongodb_uri: str = "mongodb://mongodb:27017"
    mongodb_database: str = "manus"
    mongodb_username: Optional[str] = None
    mongodb_password: Optional[str] = None
    
    # Redis configuration
    redis_host: str = "redis"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: Optional[str] = None
    
    # Sandbox configuration
    sandbox_address: Optional[str] = None
    sandbox_image: Optional[str] = None
    sandbox_name_prefix: Optional[str] = None
    sandbox_ttl_minutes: Optional[int] = 30
    sandbox_network: Optional[str] = None  # Docker network bridge name
    sandbox_chrome_args: Optional[str] = ""
    sandbox_https_proxy: Optional[str] = None
    sandbox_http_proxy: Optional[str] = None
    sandbox_no_proxy: Optional[str] = None
    
    # Search engine configuration
    search_provider: Optional[str] = "bing"  # "baidu", "google", "bing"
    google_search_api_key: Optional[str] = None
    google_search_engine_id: Optional[str] = None
    
    # Auth configuration
    auth_provider: str = "password"  # "password", "none", "local"
    password_salt: Optional[str] = None
    password_hash_rounds: int = 10
    password_hash_algorithm: str = "pbkdf2_sha256"
    local_auth_email: str = "admin@example.com"
    local_auth_password: str = "admin"
    
    # Email configuration
    email_host: Optional[str] = None  # "smtp.gmail.com"
    email_port: Optional[int] = None  # 587
    email_username: Optional[str] = None
    email_password: Optional[str] = None
    email_from: Optional[str] = None
    
    # JWT configuration
    jwt_secret_key: str = "your-secret-key-here"  # Should be set in production
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_token_expire_days: int = 7
    
    # MCP configuration
    mcp_config_path: str = "/etc/mcp.json"
    
    # Logging configuration
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
        
    def validate(self):
        """Validate configuration settings"""
        provider = self.llm_provider.lower()
        if provider == "openai" and not self.api_key:
            raise ValueError("API key is required for OpenAI provider")
        if provider == "gemini" and not self.gemini_api_key:
            raise ValueError("Gemini API key is required for Gemini provider")
        # Ollama doesn't strictly require an API key by default

@lru_cache()
def get_settings() -> Settings:
    """Get application settings"""
    settings = Settings()
    settings.validate()
    return settings 
