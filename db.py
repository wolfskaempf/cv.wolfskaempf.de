from enum import Enum
from pydantic import BaseModel


class Language(str, Enum):
    """Defines the available languages"""
    en = "en"
    de = "de"


class Element(BaseModel):
    """Objects of this type contain the translated text for an element on the site."""
    name: str
    content: dict[Language, str]


# For the purposes of this CV, using a real database would be a bit overkill
element_db: dict[str, Element] = {}
element_db["powered_by"] = Element(name="powered_by", content={
    "en": "This CV is built with FastAPI, Vue and Tailwind CSS",
    "de": "Dieses CV wurde mit FastAPI, Vue und Tailwind CSS erschaffen"
})
element_db["image_alt"] = Element(name="image_alt", content={
    "en": "Profile picture of Tom Wolfskämpf",
    "de": "Profilbild von Tom Wolfskämpf"
})
element_db["switch_language"] = Element(name="switch_language", content={
    "en": "Wechsle zu Deutsch",
    "de": "Switch to English"
})
element_db["application_as"] = Element(name="application_as", content={
    "en": "Application as Backend-Python-Developer",
    "de": "Bewerbung als Backend-Python-Entwickler"
})
element_db["trivia_header"] = Element(name="trivia_header", content={
    "en": "Trivia",
    "de": "Trivia"
})
