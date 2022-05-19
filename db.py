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
element_db["glance_header"] = Element(name="glance_header", content={
    "en": "At a glance",
    "de": "Auf einen Blick"
})
element_db["glance_copy"] = Element(name="glance_copy", content={
    "en": """Hi! 👋 I'm Tom, 25 years old. I graduated in 2015 with an Abitur-grade of 1.8 and have been living in 
    Augsburg since 2016.
    </br></br>
    Since 2015 I have been developing web applications using Python on a voluntary basis, amongst others for the 
    <a href="https://eyp.org/" target="_blank">European Youth Parliament</a>, where I've also been a member of the board of the German national committee between 
    2016 and 2018.
    </br></br>
    To date, my largest project <a href="https://stats.eyp.org/" target="_blank">GA Statistics</a> has been used to 
    visualise debates and voting procedures at over 250 events in 40 different countries. During the pandemic it was
    an essential tool for the continued operation of the events of the European Youth Parliament.
    </br></br>
    During my computer science studies at the University of Augsburg I have been tutor for Computer Science 1 and 2
    (C and Java 8) and mentored the one-week programming courses.""",

    "de": """Hi! 👋 Ich bin Tom, 25 Jahre alt, schloss 2015 mein Abitur mit der Note 1,8 ab und lebe seit 2016 in Augsburg.
    </br></br>
    Seit 2015 entwickle ich ehrenamtlich Webanwendungen mit Python, unter anderem für das 
    <a href="https://eyp.de/" target="_blank">Europäische Jugendparlament</a>, dessen Vorstand ich von 2016 bis 2018 
    angehörte.
    </br></br>
    Mein größtes Projekt <a href="https://stats.eyp.org/" target="_blank">GA Statistics</a> wurde seit 2015 auf über 
    250 Veranstaltungen in 40 verschiedenen Ländern dafür eingesetzt, Debatten und Abstimmungen zu visualisieren und 
    ermöglichte während der Covid-19-Pandemie das digitale Weiterführen der Vollversammlungen des Europäischen 
    Jugendparlaments.
    </br></br>
    Während meines Informatikstudiums an der Universität Augsburg war ich Tutor für Informatik 1 und 2 (C und Java 8)
    und betreute die jeweils einwöchigen Programmierkurse."""
})
element_db["experience_header"] = Element(name="experience_header", content={
    "en": "Experience",
    "de": "Erfahrung"
})
element_db["volunteering_header"] = Element(name="volunteering_header", content={
    "en": "Volunteering Experience",
    "de": "Ehrenamtliche Erfahrung"
})
element_db["education_header"] = Element(name="education_header", content={
    "en": "Education",
    "de": "Ausbildung"
})
element_db["trivia_header"] = Element(name="trivia_header", content={
    "en": "Trivia",
    "de": "Trivia"
})
