from dataclasses import dataclass

from domain.user.dto.user_dto import UserDTO


@dataclass
class UserModel:
    user_id: int
    user_name: str
    user_email: str
    user_phone_no: str

    def to_dto(self) -> UserDTO:
        return UserDTO(
            user_id=self.user_id,
            user_name=self.user_name,
            user_email=self.user_email,
            user_phone_no=self.user_phone_no
        )
