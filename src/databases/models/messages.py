"""File contains a `Messages` ORM model, representing the `messages` table"""

from databases.observers.messages import MessagesObserver
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin


class MessagesModel(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """Database ORM Model for 'messages'"""

    # __connection__ = 'NAME'  # ? Optional for single-db setups
    __table__ = "messages"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]  # ? Prevents mass-assignment, i.e. Model(**data)
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    # __hidden__ = []  # ? Hides field from serialization as default


MessagesModel.observe(MessagesObserver())
