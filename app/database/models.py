from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import JSON

from app.database.database import Base


class User(Base):
    """
    Stores user information.
    """

    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    signup_date = Column(
        DateTime,
        nullable=False
    )

    country = Column(
        String,
        nullable=False
    )

    device_type = Column(
        String,
        nullable=False
    )

    plan = Column(
        String,
        nullable=False
    )


class Event(Base):
    """
    Stores every user action performed inside the product.
    """

    __tablename__ = "events"

    event_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False
    )

    event_name = Column(
        String,
        nullable=False
    )

    event_timestamp = Column(
        DateTime,
        nullable=False
    )

    feature_name = Column(
        String,
        nullable=False
    )

    device_type = Column(
        String,
        nullable=False
    )

    country = Column(
        String,
        nullable=False
    )

    event_properties = Column(
    JSON,
    nullable=True
)
    