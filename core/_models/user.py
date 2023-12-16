from pydantic import ConfigDict, BaseModel, Field, EmailStr
from typing import Optional
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class User(BaseModel):
    uuid: Optional[PyObjectId] = Field(alias="_id",default=None)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    model_config = ConfigDict(extra='ignore',use_enum_values=True,json_schema_extra={
            "example": {
                "first_name": "Zain",
                "last_name": "Raza",
                "email": "jdoe@example.com"
            }
        })
    