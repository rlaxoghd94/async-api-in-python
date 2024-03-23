# Async API server in Python

The goal of this project is to simulate production environment that requires async-based api server in Python.

---

## Specifications

This project will use the following settings:

| Need            | Detailed selection |
|-----------------|--------------------|
| IDE             | Pycharm CE         |
| Language        | Python 3.10.13     |
| ASGI API Server | Uvicorn + FastAPI  |
| Auth            | RBAC               |
| Security        | JWT(Asym ECDSA)    |
| RDBMS           | H2                 |

and this project will be dockerized and tested via virtual machines

## TODO

Later on, if possible, implement all the followings:

- convert monolithic architecture into a microservice architecture
    - separate security logic into a standalone API Server that bypasses requests to the logic API Server
- attach an APM(Application Performance Monitoring) tool
    - e.g. prometheus + grafana
- implement global trace id logic across the entire cluster
    - for the application logging service and the application performance monitoring service
- test the entire system on CSP(Cloud Service Provider)
    - e.g AWS