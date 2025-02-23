"""File contains Users model observer"""

import hashlib

from api.schema import MessagesSchema
from masoniteorm.models import Model


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
        )
        user.messages.create(message.model_dump())

    def saving(self, user: Model):
        """
        Handle the Users "saving" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def saved(self, user: Model):
        """
        Handle the Users "saved" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def updating(self, user: Model):
        """
        Handle the Users "updating" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        # ? TODO: Hashing should 'ideally' be re-done here, but is omitted for time
        pass

    def updated(self, user: Model):
        """
        Handle the Users "updated" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def booted(self, user: Model):
        """
        Handle the Users "booted" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        return user

    def booting(self, user: Model):
        """
        Handle the Users "booting" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def hydrating(self, user: Model):
        """
        Handle the Users "hydrating" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def hydrated(self, user: Model):
        """
        Handle the Users "hydrated" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def deleting(self, user: Model):
        """
        Handle the Users "deleting" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

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
