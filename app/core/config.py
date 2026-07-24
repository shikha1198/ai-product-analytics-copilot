from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    """
    Centralized application configuration.
    """

    def __init__(self):
        self.APP_NAME = os.getenv(
            "APP_NAME",
            "AI Product Analytics Copilot"
        )

        self.DATABASE_URL = os.getenv(
            "DATABASE_URL",
            "sqlite:///analytics.db"
        )

        self.OPENAI_API_KEY = os.getenv(
            "OPENAI_API_KEY"
        )

        self.ANTHROPIC_API_KEY = os.getenv(
            "ANTHROPIC_API_KEY"
        )


settings = Settings()