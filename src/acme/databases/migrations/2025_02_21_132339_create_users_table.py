"""CreateUsersTable Migration."""

from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.uuid("uuid").primary()
            table.enum("type_", ["employee", "staff"])
            table.text("name")
            table.text("password", nullable=True)
            table.text("salt", nullable=True)

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
