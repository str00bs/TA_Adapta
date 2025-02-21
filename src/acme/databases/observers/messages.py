"""File contains Messages model observer"""

from masoniteorm.models import Model


class MessagesObserver:
    def creating(self, message: Model):
        """
        Handle the Messages "creating" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass

    def created(self, message: Model):
        """
        Handle the Messages "created" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass

    def saving(self, message: Model):
        """
        Handle the Messages "saving" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass

    def saved(self, message: Model):
        """
        Handle the Messages "saved" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass

    def updating(self, message: Model):
        """
        Handle the Messages "updating" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass

    def updated(self, message: Model):
        """
        Handle the Messages "updated" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass

    def booted(self, message: Model):
        """
        Handle the Messages "booted" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        return message

    def booting(self, message: Model):
        """
        Handle the Messages "booting" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass

    def hydrating(self, message: Model):
        """
        Handle the Messages "hydrating" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass

    def hydrated(self, message: Model):
        """
        Handle the Messages "hydrated" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass

    def deleting(self, message: Model):
        """
        Handle the Messages "deleting" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass

    def deleted(self, message: Model):
        """
        Handle the Messages "deleted" event.

        Args:
            message (masoniteorm.models.Model): Messages model.
        """
        pass
