from pydantic import BaseModel
# from typing import Optional

class UserRequestModel(BaseModel):
    username: str
    email: str
    # email: Optional[str] = None

class UserResponseModel(UserRequestModel):
    id: int
    username: str
    email: str