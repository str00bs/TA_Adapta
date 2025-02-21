"""UsersTableSeeder Seeder."""

import hashlib
from os import getenv
from secrets import token_urlsafe
from uuid import uuid4

import psycopg2.extras
from api.schema import UsersSchema, UsersType
from databases.models import UsersModel
from faker import Faker
from masoniteorm.seeds import Seeder


class UsersTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        # ? Required because postgres likes to be 'unique'.
        psycopg2.extras.register_uuid()

        # ? Email admin :)
        hasher = hashlib.new("sha512")
        password = getenv("AUTH_PASSWORD", "admin")
        salt = token_urlsafe(128)
        hasher.update(f"{password}{salt}".encode("utf-8"))

        user = UsersSchema(
            uuid="39a5dd0e-bc8d-4000-8561-ba78d1fd1456",
            type=UsersType.staff,
            name="Adapta Admin",
            password=hasher.hexdigest(),
            salt=salt,
        )
        UsersModel.create(user.model_dump())

        # ? Create Staff
        staff = []
        for _ in range(1, 3):
            fake = Faker()
            hasher = hashlib.new("sha512")

            password = token_urlsafe(16)
            salt = token_urlsafe(128)
            hasher.update(f"{password}{salt}".encode("utf-8"))

            user_schema = UsersSchema(
                uuid=uuid4(),
                name=fake.name(),
                type=UsersType.staff,
                password=hasher.hexdigest(),
                salt=salt,
            )

            secrets = user_schema.get_secrets()
            staff_member = user_schema.model_dump()

            staff_member.update(secrets)
            staff.append(staff_member)

        UsersModel.bulk_create(staff)

        # ? Create Employees
        employees = []
        for _ in range(1, 20):
            fake = Faker()
            hasher = hashlib.new("sha512")

            password = token_urlsafe(16)
            salt = token_urlsafe(128)
            hasher.update(f"{password}{salt}".encode("utf-8"))

            user_schema = UsersSchema(
                uuid=uuid4(),
                name=fake.name(),
                type=UsersType.employee,
                password=hasher.hexdigest(),
                salt=salt,
            )

            secrets = user_schema.get_secrets()
            employee = user_schema.model_dump()

            employee.update(secrets)
            employees.append(employee)

        UsersModel.bulk_create(employees)
