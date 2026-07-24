from app.database.database import Base
from app.database.database import engine

# Import ALL models
from app.database.models import User
from app.database.models import Event


def main():

    print("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    print("✅ Database created successfully!")


if __name__ == "__main__":
    main()