from sqlalchemy import Column, Integer, String

from domain.model_base import Base


class User(Base):
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(30), nullable=False)
    user_email = Column(String(30), nullable=False)
    user_phone_no = Column(String(20), nullable=False)
