# 🚀 Technical Assignment - Adapta
This repository contains three separate solutions for a technical assignment, divided by branch.


## 👋 Welcome!
I have intentionally "overdone" this assignment with explicit intent & purpose of showing how a more modern web-framework ([FastAPI](https://fastapi.tiangolo.com/))
can be better fit for the intended purpose (i.e. services/micro-services) than Django, which may be better suited for monolithic applications. 
It should also be mentioned, that it has *significantly* more throughput (higher [RPS](https://www.toucantoco.com/en/glossary/requests-per-second)), and faster response times.

❗ Please note, each solution has it's own `README.md` file with information specific to that branch and solution. 


## 📋 Solutions
1. Requested implementation: solving the assignment using the requested technologies (Django)
   - See branch: [feat/django](https://github.com/str00bs/TA_Adapta/tree/feat/django)
   - See URL(s):
      - UserApp - [Admin page](https://adapta1a.cloud.adapdr.me/admin)
      - UserApp - [API Root](https://adapta1a.cloud.adapdr.me/api)
      - MessagesApp - [Admin page](https://adapta1b.cloud.adapdr.me/admin)
      - MessagesApp - [API Root](https://adapta1b.cloud.adapdr.me/api)
2. Proposed implementation: solving the assignment using alternative technologies (FastAPI)
   - See branch: [feat/fastapi](https://github.com/str00bs/TA_Adapta/tree/feat/fastapi)
   - See URL(s):
      - Service page: [service/](https://adapta2.cloud.adapdr.me/)
      - Docs (Swagger): [service/docs](https://adapta2.cloud.adapdr.me/docs)
      - Alt-Docs: (ReDoc): [service/redoc](https://adapta2.cloud.adapdr.me/redoc)
      - OpenAPI Specification: [openapi.json](https://adapta2.cloud.adapdr.me/openapi.json)
3. Minified implementation: a minified version of 2, showing how it can be compressed/extended to fit a variety of use-cases.
   - See branch: [feat/fastapi-micro](https://github.com/str00bs/TA_Adapta/tree/feat/fastapi-micro)
   - See URL(s):
      - Service page: [service/](https://adapta3.cloud.adapdr.me/)
      - Docs (Swagger): [service/docs](https://adapta3.cloud.adapdr.me/docs)
      - Alt-Docs: (ReDoc): [service/redoc](https://adapta3.cloud.adapdr.me/redoc)
      - OpenAPI Specification: [service/openapi.json](https://adapta3.cloud.adapdr.me/openapi.json)
