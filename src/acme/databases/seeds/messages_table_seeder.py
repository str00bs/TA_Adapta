"""MessagesTableSeeder Seeder."""

from random import choice
from uuid import uuid4

import psycopg2.extras
from api.schema import MessagesSchema, UsersType
from databases.models import MessagesModel, UsersModel
from faker import Faker
from masoniteorm.seeds import Seeder


class MessagesTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        # ? Required because postgres likes to be 'unique'.
        psycopg2.extras.register_uuid()

        staff_ids = UsersModel.where("type_", UsersType.staff).get().pluck("uuid")
        employee_ids = UsersModel.where("type_", UsersType.employee).get().pluck("uuid")

        for _ in range(0, 20):
            fake = Faker()

            message_schema = MessagesSchema(
                uuid=uuid4(),
                title=fake.sentence(nb_words=5),
                content=fake.paragraph(nb_sentences=5),
                from_id=choice(staff_ids),
                to_id=choice(employee_ids),
            )

            MessagesModel.create(message_schema.model_dump())
