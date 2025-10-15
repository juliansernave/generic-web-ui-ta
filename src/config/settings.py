import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    base_url: str = os.getenv("BASE_URL", "https://www.saucedemo.com")
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"
    default_timeout_ms: int = int(os.getenv("DEFAULT_TIMEOUT_MS", "5000"))


settings = Settings()
