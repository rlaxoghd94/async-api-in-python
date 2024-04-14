from typing import Any, Generic, Optional, Type, TypeVar, List, Union, Dict

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from domain.model_base import Base

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    SQLAlchemy-based CRUD operation base class
    """
    model: Type[ModelType]

    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD)

        :param model: SQLAlchemy model class
        """
        self.model = model

    def get(
            self,
            db: Session,
            id: Any
    ) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
            self,
            db: Session,
            *,
            skip: int = 0,
            limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(
            self,
            db: Session,
            *,
            obj_in: CreateSchemaType
    ) -> ModelType:
        obj_in_date = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_date)  # type: ignore

        db.add(db_obj)
        db.commit()

        db.refresh(db_obj)

        return db_obj

    def update(
            self,
            db: Session,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)

        update_data = None
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()

        db.refresh(db_obj)

        return db_obj

    def remove(
            self,
            db: Session,
            *,
            id: int
    ) -> ModelType:
        db_obj = db.query(self.model).get(id)

        db.delete(db_obj)
        db.commit()

        return db_obj
