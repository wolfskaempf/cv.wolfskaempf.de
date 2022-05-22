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


class Experience(BaseModel):
    """Objects of this type contain all attributes of one piece of experience"""
    language: Language
    company: str
    title: str
    start_date: str
    end_date: str
    description: str


class Education(BaseModel):
    """Objects of this type contain all attributes of one piece of education"""
    language: Language
    institute: str
    title: str
    start_date: str
    end_date: str
    description: str


# For the purposes of this CV, using a real database would be a bit overkill
# Since all elements are well-defined through pydantic, connecting a database later is no issue
element_db: dict[str, Element] = {}
element_db["powered_by"] = Element(name="powered_by", content={
    "en": "This CV is built with FastAPI, Vue and Tailwind CSS.",
    "de": "Dieses CV wurde mit FastAPI, Vue und Tailwind CSS erschaffen."
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
    "en": """Hi! 👋 I'm Tom and I'm 25 years old. I'm passionate about accessible education, public health, stopping climate change
    and using Python to improve the world.
    </br></br>
    Since 2015 I have been developing web applications using Python on a voluntary basis, amongst others for the 
    <a href = "https://eyp.org/" target = "_blank">European Youth Parliament</a>, where I've also been a member of the board
    of the German national committee between 2016 and 2018.
    </br></br>
    To date, my largest project <a href = "https://stats.eyp.org/" target = "_blank">GA Statistics</a> has been used to 
    visualise debates and voting procedures at over 250 events in 40 different countries. During the pandemic it was
    an essential tool for the continued operation of the events of the European Youth Parliament.
    </br></br>
    During my computer science studies at the University of Augsburg I've been tutor for Computer Science 
    (C and Java 8) and mentored the one-week programming courses.""",

    "de": """Hi! 👋 Mein Name ist Tom und ich bin 25 Jahre alt. Ich begeistere mich für gerechte Bildungschancen, öffentliche Gesundheit, 
    das Fortschreiten der Klimakatastrophe aufzuhalten und wie man die Welt mit Python ein kleines Stückchen besser machen kann.
    </br></br>
    Seit 2015 entwickle ich ehrenamtlich Webanwendungen mit Python, unter anderem für das 
    <a href = "https://eyp.de/" target = "_blank">Europäische Jugendparlament</a>, dessen deutschen Vorstand ich von 2016 bis 2018 
    angehörte.
    </br></br>
    Mein größtes Projekt <a href = "https://stats.eyp.org/" target = "_blank">GA Statistics</a> wurde seit 2015 auf über 
    250 Veranstaltungen in 40 verschiedenen Ländern dafür eingesetzt, Debatten und Abstimmungen zu visualisieren und 
    ermöglichte während der Covid-19-Pandemie das digitale Weiterführen der Vollversammlungen des Europäischen 
    Jugendparlaments.
    </br></br>
    Während meines Informatikstudiums an der Universität Augsburg war ich Tutor für Informatik (C und Java 8)
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

experience_db_de: list[Experience] = []
experience_db_de.append(Experience(
    language=Language.de,
    company="Volkshochschule Diepholz",
    title="Tutor für Englisch und Deutsch",
    start_date="September 2013",
    end_date="Juli 2016",
    description="Als Tutor für Englisch und Deutsch unterrichtete ich im Rahmen des Bildungs- und Teilhabepakets des Landes Niedersachsen an Real- und Grundschulen. Der Großteil meiner Kurse waren Englischkurse für Realschüler in der Sekundarstufe I. Mein Auftraggeber war die Volkshochschule Diepholz."
))
experience_db_de.append(Experience(
    language=Language.de,
    company="Foodora GmbH",
    title="Fahrradkurier",
    start_date="Februar 2018",
    end_date="Juli 2018",
    description="Als Fahrradkurier lieferte ich Kunden ihr bestelltes Essen von verschiedenen Restaurants in Augsburg direkt bis an die Wohnungstür. Schnelle Lieferungen und ein hohes Maß an Kundenfreundlichkeit waren die Prioritäten meiner Tätigkeit."
))
experience_db_de.append(Experience(
    language=Language.de,
    company="Universität Augsburg",
    title="Tutor für Informatik",
    start_date="Oktober 2017",
    end_date="Mai 2019",
    description="Als Tutor für Informatik leitete ich wöchentlich eine Übungsgruppe, in der 30 Studierende die Grundlagen des Programmierens sowie die mathematischen Grundlagen der Informatik kennen lernten. Zudem korrigierte ich zusammen mit den anderen Tutoren die Prüfungen der Studierenden."
))
experience_db_de.append(Experience(
    language=Language.de,
    company="Radiologie im Zentrum GbR",
    title="Werkstudent in der Radiologie",
    start_date="November 2018",
    end_date="August 2019",
    description="""In der radiologischen Gemeinschaftspraxis „Radiologie im Zentrum GbR“ 
    führte ich MRT-Untersuchungen an Patienten mit Knie-, Schulter- sowie HWS-, BWS- und LWS-Problemen durch. 
    Ich betreute die Patienten von ihrer Ankunft bis hin zur Untersuchung, bei der ich mithilfe des MRT 
    „Symphony“ von Siemens die Bilder für die Grundlage des ärztlichen Befunds erstellte. 
    Im Empfangsbereich sorgte ich für die Vorbereitung der Patienten auf die Untersuchung, 
    verwaltete die Patientenakten und erstellte ihre Fallakten. Zudem kümmerte ich mich um den Versand der 
    fertigen Befunde."""
))
experience_db_de.append(Experience(
    language=Language.de,
    company="Europäisches Jugendparlament",
    title="Webentwickler / Beratung zu Webentwicklung",
    start_date="Juni 2015",
    end_date="August 2020",
    description="""Als eine meiner diversen Tätigkeiten beim Europäischen Jugendparlament (EJP) visualisierte ich 
    die Debatten und Abstimmungen der Vollversammlungen und automatisierte zeitaufwändige interne Prozesse bei
    einer gleichzeitigen Verbesserung der Ergebnisqualität.
    </br></br>
    Mein größtes Projekt <a href = "https://stats.eyp.org/" target = "_blank">GA Statistics</a> wurde seit 2015 auf über 
    250 Veranstaltungen in 40 verschiedenen Ländern dafür eingesetzt, Debatten und Abstimmungen zu visualisieren und 
    ermöglichte während der Covid-19-Pandemie das digitale Weiterführen der Vollversammlungen des Europäischen 
    Jugendparlaments.
    </br></br>
    Zuletzt beriet ich hauptsächlich die Projektmanager des Internationalen Büros des EJP darin, 
    ihre Wünsche in eine verbindliche Sprache zu übersetzen, die auch von extern beschäftigten 
    Webentwicklern verstanden wird.
    """
))
experience_db_de.append(Experience(
    language=Language.de,
    company="Radiologie Augsburg Friedberg ÜBAG",
    title="Werkstudent in der Radiologie",
    start_date="August 2019",
    end_date="heute",
    description="""Ich nehme mir viel Zeit für unsere Patienten, erstelle eine detaillierte Anamnese 
    mit Ihnen und optimiere die Sequenzen und Parameter der MRT-Untersuchung auf die Bedürfnisse des Patienten
    und der Untersuchung. Mit viel Freude erarbeite ich gemeinsam mit unseren Doktoren und Medizinprofessoren
    die tomographische Wissensgrundlage mit Hilfe derer die optimale medizinische Versorgung für die Patienten
    ausgearbeitet wird.
    </br></br>
    Neben der technischen Durchführung der MRT-Untersuchungen von Köpfen und Wirbelsäulen an Siemens Avanto und
    Vida gehört auch die Abrechnung und das Verabreichen des Kontrastmittels zu meinen Aufgaben.
    """
))

experience_db_en: list[Experience] = []
experience_db_en.append(Experience(
    language=Language.en,
    company="Volkshochschule Diepholz",
    title="Tutor for English and German",
    start_date="September 2013",
    end_date="July 2016",
    description="""I teach English and German to individuals and small groups as 
    part of the Bildungs und Teilhabepaket (Education and Participation Package) 
    funded by the Federal Republic of Germany.
    """
))
experience_db_en.append(Experience(
    language=Language.en,
    company="Foodora GmbH",
    title="Bike Courier",
    start_date="February 2018",
    end_date="July 2018",
    description="""What is it like to work in an app-based economy? To gather some first-hand experience, 
    I worked with foodora as a bike courier. I deliver food and beverages by bike while an app guides me 
    through my workday.
    """
))
experience_db_en.append(Experience(
    language=Language.en,
    company="University of Augsburg",
    title="Computer Science Tutor",
    start_date="October 2017",
    end_date="May 2019",
    description="""During my time as a computer science tutor, I lead my students onto a successful path 
    by teaching them the practical parts of computer science in courses about C and Java 8. By building a 
    strong community amongst the students in my courses, I helped them stay on track with their studies 
    and appreciate the benefits peer-to-peer-education in them.
    """
))
experience_db_en.append(Experience(
    language=Language.en,
    company="Radiologie im Zentrum GbR",
    title="MRI Operator",
    start_date="November 2018",
    end_date="August 2019",
    description="""At Radiologie im Zentrum Augsburg I ensured the best possible treatment for my spine, 
    shoulder and knee patients by taking the time to build a detailed overview of their case history and 
    new symptoms and then conducting the MRI examination to best suit their needs. Working with our 
    doctors and medical professors, it was a pleasure to be serving our community by building the 
    foundation of knowledge that allows our patients to recieve the optimal medical care, based on 
    tomographic evidence."""
))
experience_db_en.append(Experience(
    language=Language.en,
    company="European Youth Parliament",
    title="Web Developer / Web Development Advisor",
    start_date="June 2015",
    end_date="August 2020",
    description="""As one of my various involvements with the European Youth Parliament (EYP) 
    I helped bring data to life and turn it into knowledge about communities and processes. 
    My most widely established project was already used at several hundred events in 40 different countries.
    It visualises and manages discussions and facilitates democratic voting processes of plenaries of the 
    European Youth Parliament. In the last two years at the EYP I mainly advised our project managers on 
    other web development projects, helping them translate their wishes into a language the web developers 
    will understand.
    """
))
experience_db_en.append(Experience(
    language=Language.en,
    company="Radiologie Augsburg Friedberg ÜBAG",
    title="MRI Operator",
    start_date="August 2019",
    end_date="today",
    description="""I go above and beyond for my patients by taking the time to build a detailed overview 
    of their case history and new symptoms and then optimising the MRI examination to best suit their needs. 
    Working with our doctors and medical professors, it is a pleasure to be serving our community by 
    building the foundation of knowledge that allows our patients to recieve the optimal medical care, 
    based on tomographic evidence.
    
    </br></br>My main area of work is conducting neurological MRI scans of brains 
    and spines on Siemens MRIs, as well as medical accounting and administering contrast agent during the 
    examinations.
    """
))


education_db_en: list[Education] = []
education_db_en.append(Education(
    language=Language.en,
    institute="Europaschule Gymnasium Graf-Friedrich-Schule Diepholz",
    title="Abitur (Grade: 1,8)",
    start_date="2007",
    end_date="2015",
    description="""
    """
))
education_db_en.append(Education(
    language=Language.en,
    institute="University of Augsburg",
    title="Computer Science and Multimedia, B. Sc.",
    start_date="2016",
    end_date="2018",
    description="In 2018 I changed my major to the newly introduced Medical Information Science, B. Sc."
))
education_db_en.append(Education(
    language=Language.en,
    institute="University of Augsburg",
    title="Medical Information Science, B. Sc.",
    start_date="2018",
    end_date="2020",
    description="Due to the Covid-19 pandemic, this major is unfinished for now."
))


education_db_de: list[Education] = []
education_db_de.append(Education(
    language=Language.de,
    institute="Europaschule Gymnasium Graf-Friedrich-Schule Diepholz",
    title="Abitur (Note: 1,8)",
    start_date="2007",
    end_date="2015",
    description="""
    """
))
education_db_de.append(Education(
    language=Language.de,
    institute="Universität Augsburg",
    title="Informatik und Multimedia, B. Sc.",
    start_date="2016",
    end_date="2018",
    description="2018 wechselte ich zu dem neu eingeführten Studiengang Medizinische Informatik, B. Sc."
))
education_db_de.append(Education(
    language=Language.de,
    institute="Universität Augsburg",
    title="Medizinische Informatik, B. Sc.",
    start_date="2018",
    end_date="2020",
    description="Auf Grund der Covid-19-Pandemie schloss ich dieses Studium bisher nicht ab."
))

# Reversing the lists in place to get reverse chronological order.
# Why not create the list in this order to begin with?
# This is done to maintain future compatibility with a real database, where the natural order would
# also be chronological, based on the later primary keys being larger
experience_db_de.reverse()
experience_db_en.reverse()
