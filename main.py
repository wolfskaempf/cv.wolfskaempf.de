from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Language(str, Enum):
    en = "en"
    de = "de"


class Element(BaseModel):
    """Objects of this type contain the translated text for an element on the site."""
    name: str
    content: dict[Language, str]


# For the purposes of this CV, using a separate database would be a bit overkill
element_db: dict[str, Element] = {}
element_db["powered_by"] = Element(name="powered_by", content={
    "en": "This CV is built with FastAPI and Vue",
    "de": "Dieses CV wurde mit FastAPI und Vue erschaffen"
})


@app.get("/elements/{language}/{element_name}")
async def get_element(language: Language, element_name: str):
    return {element_db[element_name].content[language]}
