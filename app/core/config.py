from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()


class Settings:
    """
    Centralized application configuration.
    Reads values from the .env file.
    """

    APP_NAME = os.getenv(
        "APP_NAME",
        "AI Product Analytics Copilot"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///analytics.db"
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )

    ANTHROPIC_API_KEY = os.getenv(
        "ANTHROPIC_API_KEY"
    )


# Create a single settings object
settings = Settings()