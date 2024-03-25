# ASGI Python Web API Server

Project directory details:

config

- Application configurations(local, dev, prod)

domain

- directory based on business models which contains:
    - DTO, entity, model
    - repository accessing infrastructure
    - domain-level service

infrastructure

- external infrastructure connectors

presentation

- HTTP controllers
- documents files for APIDocs if needed

service

- business logics that uses domain layer

util

- simple utilities
    - e.g. encryption util, datetime util