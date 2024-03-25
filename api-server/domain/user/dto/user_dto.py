from pydantic import BaseModel


class UserDTO(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    user_phone_no: str
