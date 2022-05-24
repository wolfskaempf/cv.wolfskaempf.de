from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from db import Language
from db import element_db
from db import experience_db_de, experience_db_en
from db import education_db_de, education_db_en
from db import volunteering_db_de, volunteering_db_en
from db import trivia_db_de, trivia_db_en


app = FastAPI()


@app.get("/elements/{language}")
async def get_element(language: Language):
    """Builds a language-kit for the specified language"""
    language_kit: dict[str, str] = {}
    for key, value in element_db.items():
        language_kit[key] = value.content[language]

    return language_kit


@app.get("/experiences/{language}")
async def get_experience(language: Language):
    """Returns the pre-sorted entries of the corresponding list"""
    if language == Language.en:
        return experience_db_en
    elif language == Language.de:
        return experience_db_de

@app.get("/education/{language}")
async def get_education(language: Language):
    """Returns the pre-sorted entries of the corresponding list"""
    if language == Language.en:
        return education_db_en
    elif language == Language.de:
        return education_db_de


@app.get("/volunteering/{language}")
async def get_education(language: Language):
    """Returns the pre-sorted entries of the corresponding list"""
    if language == Language.en:
        return volunteering_db_en
    elif language == Language.de:
        return volunteering_db_de


@app.get("/trivia/{language}")
async def get_trivia(language: Language):
    """Returns the pre-sorted entries of the corresponding list"""
    if language == Language.en:
        return trivia_db_en
    elif language == Language.de:
        return trivia_db_de


# If none of the API routes match, serve the static content that makes up out Vue app
app.mount('/', StaticFiles(directory='public', html=True))
