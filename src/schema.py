"""File contains API Schema"""

from datetime import datetime
from enum import Enum
from secrets import token_urlsafe
from uuid import UUID, uuid4

from faker import Faker
from pydantic import BaseModel, ConfigDict, Field, SecretStr

fake = Faker()


# ? Generic
class ResponseSchema(BaseModel):
    """Generic response model"""

    detail: str


class MetaSchema(BaseModel):
    """Generic meta model"""

    count: int = Field(..., description="Total number of items in the list")
    current_page: int = Field(..., description="Current page of the list")
    next_page: int | None = Field(..., description="Next page of the list")
    previous_page: int | None = Field(..., description="Previous page of the list")


# ? Messages
class MessagesSchema(BaseModel):
    """Contains API Schema for a `Messages` object"""

    model_config = ConfigDict(from_attributes=True)

    # ? Public fields
    uuid: UUID = Field(
        description="Unique IDentifier",
        default_factory=uuid4,
    )
    title: str = Field(
        ..., description="Message title", examples=[fake.sentence(nb_words=5)]
    )
    content: str = Field(
        ..., description="Message content", examples=[fake.paragraph(nb_sentences=5)]
    )

    from_id: UUID = Field(
        description="Sender ID",
        default_factory=uuid4,
        examples=["39a5dd0e-bc8d-4000-8561-ba78d1fd1456"],  # ? Adapta Admin
    )
    to_id: UUID = Field(
        description="Recipient ID",
        default_factory=uuid4,
    )

    # ? Excluded fields
    created_at: datetime | None = Field(
        None, description="When the message was created"
    )
    updated_at: datetime | None = Field(
        None, description="When the message was last updated"
    )
    deleted_at: datetime | None = Field(
        None, description="When the message was deleted", exclude=True
    )


class MessagesList(BaseModel):
    """Model for a `Messages` object"""

    model_config = ConfigDict(from_attributes=True)

    data: list[MessagesSchema]
    meta: MetaSchema


# ? User
class UsersType(str, Enum):
    employee = "employee"
    staff = "staff"


class UsersSchema(BaseModel):
    """Contains API Schema for a `Users` object"""

    model_config = ConfigDict(from_attributes=True)

    # ? Public fields
    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)
    type: UsersType | None = Field(
        UsersType.employee,
        description="Users type",
    )

    name: str = Field(fake.name(), description="Users name")

    # ? Secret fields
    password: SecretStr | str | None = Field(
        token_urlsafe(16), description="Users password", exclude=True
    )
    salt: SecretStr | str | None = Field(
        token_urlsafe(128),
        description="Salt for password",
        exclude=True,
    )

    # ? Excluded fields
    created_at: datetime | None = Field(None, description="When the user was created")
    updated_at: datetime | None = Field(
        None, description="When the user was last updated"
    )
    deleted_at: datetime | None = Field(
        None, description="When the user was deleted", exclude=True
    )

    def get_secrets(self):
        """Return a copy of the model with secrets"""
        return {
            "password": self.password.get_secret_value(),
            "salt": self.salt.get_secret_value(),
        }


class UsersList(BaseModel):
    """Model for a `Users` object"""

    model_config = ConfigDict(from_attributes=True)

    data: list[UsersSchema]
    meta: MetaSchema
