"""File contains a `Users` ORM model, representing the `users` table"""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin

from databases.observers.users import UsersObserver


class UsersModel(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """Database ORM Model for 'users'"""

    # __connection__ = 'NAME'  # ? Optional for single-db setups
    __table__ = "users"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]  # ? Prevents mass-assignment, i.e. Model(**data)
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    # __hidden__ = []  # ? Hides field from serialization as default

    @has_many("uuid", "from_id")
    def messages(self):
        from databases.models.messages import MessagesModel

        return MessagesModel

    def get_sent(self):
        """Helper method to get sent messages"""
        from databases.models.messages import MessagesModel

        return MessagesModel.where("from_id", self.uuid).get()

    def gte_received(self):
        """Helper method to get received messages"""
        from databases.models.messages import MessagesModel

        return MessagesModel.where("to_id", self.uuid).get()


UsersModel.observe(UsersObserver())
