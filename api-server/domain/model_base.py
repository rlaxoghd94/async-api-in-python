from typing import Any, Dict

from sqlalchemy.ext.declarative import as_declarative, declared_attr

class_registry: Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    """
    SQLAlchemy `declarative_base` objectified base class

    ALL orm model objects should inherit from THIS base class
    """
    id: Any
    __name__: str

    # Generate `__tablename__` automatically
    @declared_attr
    def __tablename__(self, cls) -> str:
        return cls.__name__.lower()
