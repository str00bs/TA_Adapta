# 🚀 Technical Assignment - Adapta - Micro-fastapi
This branch is a minified version of [feat/fastapi](https://github.com/str00bs/TA_Adapta/tree/feat/fastapi)
It is made to showcase how a framework designe with micro-services in mind, can easily and quickly
be converted into a minified format, intended for usage in a service/micro-service ecosystem.

## ❗ Notes
There are a few important things to note;
1. ORM Models(++), API Schemas & Responses should supplied via packages through by an internal repository
   - Example: : `adapta-db`, `adapta-api-schemas` and `adapta-api-responses`
2. Config can also *optionally* be made universal and supplied via a package as well
3. Seeding & migrations should normally never be done per service, but in one unified location
   - *But they have been added here, as it makes sense **specifically** for the assignment*
4. Full docs should be supplied per service, but have been omitted due to time-constraints
5. A CMS should be centrally managed and have access to a database-cluster used by **all** micro-services.
   - It has therefore been omitted, but messages can be viewed by calling `/api/messages` ...
6. CI files (drone and deepsource) have been included as examples, but are not activated.

If you have any questions in regards to this, or other technical decisions made for the test, please ask!
