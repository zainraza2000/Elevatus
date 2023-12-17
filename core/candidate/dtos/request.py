from typing import Optional,List
from core._utils.enums import Gender
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from bson import ObjectId


class CandidateUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    career_level: Optional[str] = None
    job_major: Optional[str] = None
    years_of_experience: Optional[int] = None
    degree_type: Optional[str] = None
    skills: Optional[List[str]] = None
    nationality: Optional[str] = None
    city: Optional[str] = None
    salary: Optional[int] = None
    gender: Optional[Gender] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        use_enum_values=True,
        extra='ignore',
        json_schema_extra={
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
        }
    )