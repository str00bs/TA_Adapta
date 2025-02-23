# 🚀 Technical Assignment - Adapta - Django
This branch provides the requested Django implementation.

However:
- It specifically (and django in general) **requires** multiple architectural and python anti-patterns and style-guide violations.
   - Django cannot be ran as a 'true' micro-service as it requires a prescribed structure, or significant work-a-rounds.
   - You should never duplicate code, entities (models), tables or databases. (Ref: [SSOT](https://en.wikipedia.org/wiki/Single_source_of_truth))
   - etc...
- This is not an implementation I can recommend or stand behind, as I believe Django should only ever be used for monolithic applications and/or low-performance applications.

Therefore, it intentionally shortened down as much as possible with references, descriptions (and alternatives) to show an understanding of the relevant concepts & methodologies.

## ❗ Notes
1. This is effectively a pseudo [monorepo](https://monorepo.tools/#what-is-a-monorepo) but without clean separations due to django limitations.
   - [App 1](src/app_1) - Users
   - [App 2](src/app_2) - Messages
2. The welcome and goodbye messages on database events `users.created` and `users.deleted` is clearly intended to use django-signaks as a stand-in for model observers.
   - This would require an(other) anti-pattern of duplicating the `users` table (i.e. `profiles`) via an 'extension' (one-to-one relationship)
   - It's as simple as adding HTTP call to the respective events [ref](https://dev.to/codewitgabi/django-signals-15l3) but since the same functionality exists in 2+3, this        anti-pattern is intentionally replaced with this explanation.
   - You can see it being cleanly implemented on database events for both solution 2 and 3 using model observers.
3. Tests have been omitted, as they would functionally be identical as for solution 2 and 3, but using django's wrapped `unittest` over `pytest`.
   - You would just use `unittest.TestCase.setUp` and `unittest.TestCase.tearDown` over `pytest.fixture`'s

## ⚙️ Setup & Run
❗ This repository uses [poetry](https://python-poetry.org/)

### Local
First setup the developer environment
1. Copy ENV file `cp dist.env src/app_1/.env && cp dist.env src/app_2/.env`
   - ❗ A postgres database must be made available, and details filled in
2. Install dependencies `poetry install --all-extras`
3. Run specific app manually:
   - App_1: `cd src/app_1 && python manage.py runserver`
   - App_2: `cd src/app_2 && python manage.py runserver`

### Docker (Recommended)
1. Copy ENV file `cp dist.env .env`
   - You do not need to make any changes to this file.
2. Copy compose file `cp local.docker-compose.yml docker-compose.yml`
3. Run it: `docker-compose up`
   - App_1 will be made available on `localhost:8080`
     - Admin path: `localhost:8080/admin`
     - API path: `localhost:8080/api`
   - App_2 will be made available on `localhost:8081`
     - Admin path: `localhost:8081/admin`
     - API path: `localhost:8081/api`

### Production
This requires traefik with docker-detection enabled and LetsEncrypt activated
1. Copy over env file: `cp dist.env .env`
   - ❗ Details must be filled in
2. Copy compose file `cp prod.docker-compose.yml docker-compose.yml` 
3. Run `docker-compose up -d` and visit the configured domain addresses
