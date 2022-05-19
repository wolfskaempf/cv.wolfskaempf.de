from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from db import element_db, Language

app = FastAPI()


@app.get("/elements/{language}")
async def get_element(language: Language):
    """Builds a language-kit for the specified language"""
    language_kit: dict[str, str] = {}
    for key, value in element_db.items():
        language_kit[key] = value.content[language]

    return language_kit


# If none of the API routes match, serve the static content that makes up out Vue app
app.mount('/', StaticFiles(directory='public', html=True))
