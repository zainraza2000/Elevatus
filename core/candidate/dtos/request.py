from typing import Optional,List
from pydantic import  BaseModel, EmailStr,validator
from core._utils.enums import Gender



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