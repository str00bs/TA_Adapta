import hashlib

from masoniteorm.models import Model

from schema import MessagesSchema


class UsersObserver:
    def creating(self, user: Model):
        """
        Handle the Users "creating" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        # ? Hash password
        hasher = hashlib.new("sha512")
        hasher.update(f"{user.password}{user.salt}".encode("utf-8"))
        user.password = hasher.hexdigest()
        user.save()
        return user.fresh()

    def created(self, user: Model):
        """
        Handle the Users "created" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        message = MessagesSchema(
            title=f"Welcome to Adapta {user.name}!", content=f"Hi {user.name},\n\n"
        )  # type:ignore
        user.messages.create(message.model_dump())

    def deleted(self, user: Model):
        """
        Handle the Users "deleted" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        message = MessagesSchema(
            title=f"Goodbye {user.name}", content="Sad to see you go..."
        )  # type:ignore
        user.messages.create(message.model_dump())
