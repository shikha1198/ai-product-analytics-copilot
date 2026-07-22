from app.core.config import settings
from app.core.logger import logger


def main():
    logger.info("=" * 60)
    logger.info(settings.APP_NAME)
    logger.info("Application Started Successfully")
    logger.info(f"Database: {settings.DATABASE_URL}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()