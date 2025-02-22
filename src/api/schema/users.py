"""File contains API schema used for `/api/users` endpoints"""

from datetime import datetime
from enum import Enum
from secrets import token_urlsafe
from uuid import UUID, uuid4

from faker import Faker
from pydantic import BaseModel, ConfigDict, Field, SecretStr

from api.schema.generic import MetaSchema

fake = Faker()


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
