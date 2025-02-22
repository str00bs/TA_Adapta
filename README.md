# 🚀 Technical Assignment - Adapta - FastAPI
This branch is an alternative *(strongly recommended)* implementation to [feat/django](https://github.com/str00bs/TA_Adapta/tree/feat/fastapi)

It is made to showcase how a framework with modular design, is neither slower nor more difficult to implement than one that is all-inclusive like Django is, 
and can be made into a minified format *(all the way to a single file...)*, intended for usage in a service/micro-service ecosystem without issues (see: [feat/fastapi-micro](https://github.com/str00bs/TA_Adapta/tree/feat/fastapi-micro))


## ❗ Notes
There are a few important things to note;
1. This example is generated using a customizeable [service template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) 
   to provide a quickstart/cookiecutter structure similar to that which is provided by a CLI like Django's static generator `manage.py`. 
2. ORM Models(++), API Schemas & Responses should supplied via packages through by an internal repository
   - Example: : `adapta-db`, `adapta-api-schemas` and `adapta-api-responses`
3. Seeding & migrations should normally never be done per service, but in one unified location
   - *But they have been added here, as it makes sense **specifically** for the assignment*
4. A CMS should be centrally managed and have access to a database-cluster used by **all** micro-services.
   - It has therefore been omitted, but messages can be viewed by calling `/api/messages` ...
5. Config can also *optionally* be made universal and supplied via a package as well
6. CI files (drone and deepsource) have been included as examples, but are not activated.
7. This implementation is intentionally verbose,

If you have any questions in regards to this, or other technical decisions made for the test, please ask!

## ⚙️ Setup & Run
❗ This repository uses [poetry](https://python-poetry.org/)

### Local
First setup the developer environment
1. Copy ENV file `cp dist.env src/.env`
   - ❗ A postgres database must be made available, and details filled in
2. Install dependencies `poetry install --all-extras`
3. Copy VSC resource files `cp resources/vscode .vscode`
   - It is highly recommended to install the `@recommended` extensions

You can now run the application by either:
1. Run with vsc config: Go to Run & Debug -> Run App
2. Run manually: `cd src && poetry run uvicorn main:app --reload`

### Docker
1. Copy ENV file `cp dist.env .env`
   - You do not need to make any changes to this file.
2. Copy compose file `cp local.docker-compose.yml docker-compose.yml`
3. Run it: `docker-compose up`

### Production
This requires traefik with docker-detection enabled and LetsEncrypt activated
1. Either import `dist.env` and fill in via interface, or `cp dist.env .env`
   - ❗ Details must be filled in
2. Either import `prod.docker-compose.yml` or copy it `cp prod.docker-compose.yml docker-compose.yml` 
3. Run `docker-compose up -d` and visit the configured domain address


## 🧑‍🔬 Testing
You can now test the application by either:
1. Run with vsc config: Go to Run & Debug -> Run Tests
2. Run manually: `poetry run pytest tests`


## 🧰 Resources
### General
General resources already provided for/with the application & repository.
- IDE Configurations: [VSCode](resources/vscode)
- Deployment Tools:
  - Dockerfile: [Dockerfile](Dockerfile)
  - Local compose file: [local.docker-compose.yml](local.docker-compose.yml)
  - Production compose file: [prod.docker-compose.yml](prod.docker-compose.yml)
### SDK Docs
- API Framework: [FastAPI](https://fastapi.tiangolo.com/)
  - Parent: [Starlette](https://www.starlette.io/)
  - Schema: [Pydantic](https://pydantic-docs.helpmanual.io/)
- Testing:
  - Runner: [Pytest](https://docs.pytest.org/en/6.2.x/)
- Database
  - ORM: [Masonite ORM](https://orm.masoniteproject.com/)
  - _Formerly known as/continuation of: [Orator](https://orator-orm.com/)_
- Validation & Settings
  - [Pydantic Settings](https://pydantic-docs.helpmanual.io/usage/settings/)