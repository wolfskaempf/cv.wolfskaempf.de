import os

from fastapi import FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles

from db import Language, PersonalData
from db import education_db_de, education_db_en
from db import element_db
from db import experience_db_de, experience_db_en
from db import trivia_db_de, trivia_db_en
from db import volunteering_db_de, volunteering_db_en

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


@app.get("/personal_data")
async def get_personal_data(secret: str):
    """
    Returns personal data from environment variables, so that this sensitive data does not need
    to be stored inside of git
    """
    if secret is not None and secret.lower() == os.environ.get("CV_PERSONAL_DATA_SECRET"):
        personal_data = PersonalData(
            name=os.environ.get("CV_NAME"),
            telephone=os.environ.get("CV_TELEPHONE"),
            email=os.environ.get("CV_EMAIL"),
            address_street=os.environ.get("CV_ADDRESS_STREET"),
            address_zip=os.environ.get("CV_ADDRESS_ZIP"),
            address_city=os.environ.get("CV_ADDRESS_CITY"),
            nationality=os.environ.get("CV_NATIONALITY"),
            date_of_birth=os.environ.get("CV_DATE_OF_BIRTH"),
        )
        return personal_data
    else:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You did not supply the secret needed to access the personal data on this CV.",
        )


# If none of the API routes match, serve the static content that makes up out Vue app
app.mount('/', StaticFiles(directory='public', html=True))
