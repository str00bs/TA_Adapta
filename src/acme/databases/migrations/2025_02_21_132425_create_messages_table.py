"""CreateMessagesTable Migration."""

from masoniteorm.migrations import Migration


class CreateMessagesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("messages") as table:
            table.uuid("uuid").primary()
            table.text("title")
            table.text("content")

            # fmt: off
            table.uuid("from_id").foreign("from_id") \
                .references("uuid").on("users") \
                .on_delete("cascade")
            table.uuid("to_id").foreign("to_id") \
                .references("uuid").on("users") \
                .on_delete("cascade")

            # fmt: on
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("messages")
