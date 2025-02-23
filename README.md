# 🚀 Technical Assignment - Adapta - Django
This branch provides a Django implementation as required.

## ❗ Notes
1. This is not an I can recommend, from my perspective Django should only be used for monolithic applications.
2. The assignment requires the 'apps' to be runable/buildable separately, meaning they need separate django 'projects',
   effectively making this a pseudo-mono-repo
   - [App 1](src/app_1) - Users
   - [App 2](src/app_2) - Messages
3. Not included:
   - Testing has been omitted for this implementation, but is already showed on the two other solutions.
   - Resources has been omitted for this implementation, but is already showed on the two other solutions.


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
