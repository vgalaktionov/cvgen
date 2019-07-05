from pydantic import EmailStr, UrlStr
from pydantic.dataclasses import dataclass

from typing import Optional, List


@dataclass(unsafe_hash=True)
class Personalia:
    phone: str
    address: str
    nationality: str
    email: EmailStr


@dataclass
class Job:
    title: str
    industry: str
    dates: str
    description: Optional[str]


@dataclass
class Education:
    diploma: str
    institution: str
    dates: str
    description: str


@dataclass
class Activity:
    title: str
    organization: str
    dates: str
    description: str


@dataclass
class Project:
    title: str
    description: str
    link: Optional[UrlStr]


@dataclass
class Skill:
    category: str
    keywords: List[str]


@dataclass
class CV:
    name: str
    blurb: str
    personalia: Personalia
    experience: List[Job]
    education: List[Education]
    skills: List[Skill]
    projects: List[Project]
    activities: List[Activity]
