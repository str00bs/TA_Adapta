"""File contains API schema used for `/api/messages` endpoints"""

from datetime import datetime
from uuid import UUID, uuid4

from api.schema.generic import MetaSchema
from faker import Faker
from pydantic import BaseModel, ConfigDict, Field

fake = Faker()


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
        None, description="When the message was deleted"
    )


class MessagesList(BaseModel):
    """Model for a `Messages` object"""

    model_config = ConfigDict(from_attributes=True)

    data: list[MessagesSchema]
    meta: MetaSchema
