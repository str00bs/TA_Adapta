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
