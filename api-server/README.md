# ASGI Python Web API Server

Project directory details:

config

- Application configurations(local, dev, prod)

domain

- DTO, entity, model
- repository accessing infrastructure

infrastructure

- external infrastructure connectors

presentation

- HTTP controllers
    - may use domain.dto
- documents files for APIDocs

service

- business logics that uses domain layer

util

- simple utilities
    - e.g. encryption tools, datetime tools