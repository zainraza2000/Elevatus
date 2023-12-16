from core._utils.enums import Gender
from typing import Optional, List
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]


class Candidate(BaseModel):
    uuid: Optional[PyObjectId] = Field(alias="_id", default=None)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    career_level: str = Field(...)
    job_major: str = Field(...)
    years_of_experience: int = Field(...)
    degree_type: str = Field(...)
    skills: List[str] = Field(...)
    nationality: str = Field(...)
    city: str = Field(...)
    salary: int = Field(...)
    gender: Gender = Field(...)
    model_config = ConfigDict(extra='ignore',use_enum_values=True,validate_assignment=True,json_schema_extra={
            "example": {
                "first_name": "test",
                "last_name": "zain",
                "email": "zain@example.com",
                "career_level": "string",
                "job_major": "string",
                "years_of_experience": 0,
                "degree_type": "string",
                "skills": [
                    "string"
                ],
                "nationality": "string",
                "city": "string",
                "salary": 0,
                "gender": "Male"
            }
        })
    