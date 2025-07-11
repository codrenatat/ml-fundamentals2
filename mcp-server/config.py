import os
import dotenv

dotenv.load_dotenv()

class Config:
    """Configuration class to manage environment variables and settings"""
    
    def __init__(self):
        self.openai_api_key = self._get_required_env("OPENAI_API_KEY")
        self.alpha_vantage_api_key = self._get_required_env("ALPHA_VANTAGE_API_KEY")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        self.max_tokens = int(os.getenv("MAX_TOKENS", "1000"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
    
    def _get_required_env(self, key: str) -> str:
        """Get required environment variable or raise error"""
        value = os.getenv(key)
        if not value:
            raise ValueError(f"{key} environment variable is required")
        return value
