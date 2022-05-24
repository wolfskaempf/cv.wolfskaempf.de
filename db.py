from enum import Enum
from datetime import date, datetime

from pydantic import BaseModel, validator


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


class Volunteering(BaseModel):
    """Objects of this type contain all attributes of one piece of volunteering"""
    language: Language
    organisation: str
    title: str
    start_date: str
    end_date: str
    description: str


class Trivia(BaseModel):
    """Objects of this type contain all attributes of one piece of trivia"""
    language: Language
    content: str


class PersonalData(BaseModel):
    """Objects of this type contain all personal data of a person"""
    name: str
    telephone: str  # We define it as a str because we want to include a + in the beginning as well as spacing
    email: str
    address_street: str
    address_zip: int
    address_city: str
    nationality: str
    date_of_birth: str

    @validator("date_of_birth", pre=True)
    def validate_date_of_birth(cls, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("The supplied date of birth could not be parsed into a valid date (DD-MM-YYYY).")
        return value

        # For the purposes of this CV, using a real database would be a bit overkill


# Since all elements are well-defined through pydantic, connecting a database later is no issue
element_db: dict[str, Element] = {}
element_db["powered_by"] = Element(name="powered_by", content={
    "en": "This CV is built with FastAPI, Vue and Tailwind CSS.",
    "de": "Dieses CV wurde mit FastAPI, Vue und Tailwind CSS erstellt."
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
    "en": """Hi! 👋 I'm Tom and I'm 25 years old. I'm passionate about accessible education, public health, climate justice
    and using Python to improve the world.
    <br><br>
    Since 2015 I have been developing web applications using Python on a voluntary basis, amongst others for the 
    <a href = "https://eyp.org/" target = "_blank">European Youth Parliament</a>, where I've also been a member of the board
    of the German national committee between 2016 and 2018.
    <br><br>
    To date, my largest project <a href = "https://stats.eyp.org/" target = "_blank">General Assembly Statistics</a> has been used to 
    visualise debates and voting procedures at over 250 events in 40 different countries. During the pandemic it was
    an essential tool for the continued operation of the events of the European Youth Parliament.
    <br><br>
    During my computer science studies at the University of Augsburg I've been tutor for Computer Science 
    (C and Java 8) and mentored the one-week programming courses.
    <br><br>
    At TEAM23 I'd love to implement projects with a sense of purpose, and thus follow up on the projects that TEAM23 has 
    has carried out so far. With Python as the tool of choice to create meaningful results, I'd be looking forward to
    toast to our first successful ventures at the next mountain hike.""",

    "de": """Hi! 👋 Mein Name ist Tom und ich bin 25 Jahre alt. Ich begeistere mich für gerechte Bildungschancen, öffentliche Gesundheit, 
    Klimagerechtigkeit und wie man die Welt mit Python ein kleines Stückchen besser machen kann.
    <br><br>
    Seit 2015 entwickle ich ehrenamtlich Webanwendungen mit Python, unter anderem für das 
    <a href = "https://eyp.de/" target = "_blank">Europäische Jugendparlament</a>, dessen deutschem Vorstand ich von 2016 bis 2018 
    angehörte.
    <br><br>
    Mein größtes Projekt <a href = "https://stats.eyp.org/" target = "_blank">General Assembly Statistics</a> wurde seit 2015 auf über 
    250 Veranstaltungen in 40 verschiedenen Ländern dafür eingesetzt, Debatten und Abstimmungen zu visualisieren und 
    ermöglichte während der Covid-19-Pandemie das digitale Weiterführen der Vollversammlungen des Europäischen 
    Jugendparlaments.
    <br><br>
    Während meines Informatikstudiums an der Universität Augsburg war ich Tutor für Informatik (C und Java 8)
    und betreute die jeweils einwöchigen Programmierkurse.
    <br><br>
    Bei TEAM23 möchte ich Projekte mit Sinn umsetzen und damit an die Projekte anschließen, die TEAM23 bisher 
    durchgeführt hat. Ich würde mich sehr freuen, mit Python als Werkzeug der Wahl wirkungsvolle Ergebnisse zu 
    erschaffen und als Teil des TEAM23 bei der nächsten Bergtour auf die ersten gemeinsamen Erfolge anzustoßen."""
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
element_db["personal_data_header"] = Element(name="personal_data_header", content={
    "en": "Personal data",
    "de": "Persönliche Daten"
})
element_db["born"] = Element(name="born", content={
    "en": "born",
    "de": "geb."
})
element_db["telephone"] = Element(name="telephone", content={
    "en": "Telephone",
    "de": "Mobil"
})
element_db["email"] = Element(name="email", content={
    "en": "Mail",
    "de": "E-Mail"
})
element_db["nationality"] = Element(name="nationality", content={
    "en": "Nationality",
    "de": "Staatsangehörigkeit"
})
element_db["personal_data_access_denied"] = Element(name="personal_data_access_denied", content={
    "en": """Personal data is only shown if you access this site with the name of your company inside the hash of the 
    URL""",
    "de": """Die Persönlichen Daten werden nur angezeigt, wenn du den Link mit dem Namen Deiner Firma im Hash der 
    URL aufrufst."""
})


experience_db_de: list[Experience] = []
experience_db_de.append(Experience(
    language=Language.de,
    company="Volkshochschule Diepholz",
    title="Tutor für Englisch und Deutsch",
    start_date="September 2013",
    end_date="Juli 2016",
    description="""Als Tutor für Englisch und Deutsch unterrichtete ich im Rahmen des Bildungs- und Teilhabepakets des 
    Landes Niedersachsen an Real- und Grundschulen. Der Großteil meiner Kurse waren Englischkurse für Realschüler:innen 
    in der Sekundarstufe I.
    <br><br>
    Während meiner Arbeit für das Bildungs- und Teilhabepaket nahm ich an einem mehrjährigen Wochenendkurs für die
    Basisqualifikation Pädagogik teil und wurde erfolgreich dafür zertifiziert."""
))
experience_db_de.append(Experience(
    language=Language.de,
    company="Foodora GmbH",
    title="Fahrradkurier",
    start_date="Februar 2018",
    end_date="Juli 2018",
    description="""Als Fahrradkurier bei Foodora lieferte ich Kund:innen ihr bestelltes Essen von verschiedenen 
    Restaurants in Augsburg direkt bis an die Wohnungstür."""
))
experience_db_de.append(Experience(
    language=Language.de,
    company="Universität Augsburg",
    title="Tutor für Informatik",
    start_date="Oktober 2017",
    end_date="Mai 2019",
    description="""Als Tutor für Informatik leitete ich wöchentlich eine Übungsgruppe, in der 30 Student:innen 
    die Grundlagen des Programmierens sowie die mathematischen Grundlagen der Informatik kennenlernten. 
    Zudem korrigierte ich zusammen mit den anderen Tutor:innen die Prüfungen der Student:innen.
    <br><br>
    Nachdem 2018 aufgrund der Einführung der DSGVO das bisherige universitäre Werkzeug zum präferenzbasierten 
    Verteilen der Übungsteilnehmer:innen vom Lehrstuhl für Theoretische Informatik offline genommen wurde, programmierte 
    ich <a href="https://www.youtube.com/watch?v=JM6i0Hb757A" target="_blank">Loki</a> (JavaFX 8), welches sowohl an der
     Universität Augsburg für die Verteilung der Student:innen auf die Informatiktutorien, als auch beim Europäischen 
     Jugendparlament für die Verteilung von Teilnehmer:innen an ihre präferierten Themenbereiche verwendet wurde."""
))
experience_db_de.append(Experience(
    language=Language.de,
    company="Radiologie im Zentrum GbR",
    title="Werkstudent in der Radiologie",
    start_date="November 2018",
    end_date="August 2019",
    description="""In der radiologischen Gemeinschaftspraxis „Radiologie im Zentrum GbR“ 
    führte ich MRT-Untersuchungen an Patient:innen mit Knie-, Schulter- sowie HWS-, BWS- und LWS-Problemen durch. 
    Ich betreute die Patient:innen von ihrer Ankunft bis hin zur Untersuchung, bei der ich mithilfe des MRT 
    „Symphony“ von Siemens die Bilder für die Grundlage des ärztlichen Befunds erstellte. 
    Im Empfangsbereich sorgte ich für die Vorbereitung der Patient:innen auf die Untersuchung, 
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
    <br><br>
    Mein größtes Projekt <a href = "https://stats.eyp.org/" target = "_blank">General Assembly Statistics</a> wurde seit
     2015 auf über 250 Veranstaltungen in 40 verschiedenen Ländern dafür eingesetzt, Debatten und Abstimmungen zu 
     visualisieren und ermöglichte während der Covid-19-Pandemie das digitale Weiterführen der Vollversammlungen des 
     Europäischen Jugendparlaments.
    <br><br>
    Zuletzt beriet ich hauptsächlich die Projektmanager:innen des Internationalen Büros des EJP darin, 
    ihre Wünsche in eine verbindliche Sprache zu übersetzen, die auch von extern beschäftigten 
    Webentwickler:innen verstanden wird.
    """
))
experience_db_de.append(Experience(
    language=Language.de,
    company="Radiologie Augsburg Friedberg ÜBAG",
    title="Werkstudent in der Radiologie",
    start_date="August 2019",
    end_date="heute",
    description="""Ich nehme mir viel Zeit für unsere Patient:innen, erstelle eine detaillierte Anamnese 
    mit ihnen und optimiere die Sequenzen und Parameter der MRT-Untersuchung auf die Bedürfnisse der Patient:innen
    und der Untersuchung. Mit viel Freude erarbeite ich gemeinsam mit unseren Doktor:innen und Medizinprofessoren
    die tomographische Wissensgrundlage mit Hilfe derer eine möglichst gute medizinische Versorgung für die 
    Patient:innen vorbereitet wird.
    <br><br>
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
    <br><br>
    As part of my involvement with the programme, I took part in a multi-year ongoing qualification course for basic 
    pedagogics and was certified for those abilities.
    """
))
experience_db_en.append(Experience(
    language=Language.en,
    company="Foodora GmbH",
    title="Bike Courier",
    start_date="February 2018",
    end_date="July 2018",
    description="""What is it like to work in an app-based economy? To gather some first-hand experience, 
    I worked with foodora as a bike courier. I delivered food and beverages by bike while an app guided me 
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
    <br><br>
    After the university's tool for preference based allocations had been discontinued in 2018 by the chair of 
    theoretical computer science due to new GDPR rules, I created 
    <a href="https://www.youtube.com/watch?v=JM6i0Hb757A" target="_blank">Loki</a> (JavaFX 8), which was used by 
    the University of Augsburg for the allocation of students to their computer science courses and by the 
    European Youth Parliament for the allocation of the hundreds of participants to their preferred topics.
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
    foundation of knowledge that allows our patients to receive the optimal medical care, based on 
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
    building the foundation of knowledge that allows our patients to receive the optimal medical care, 
    based on tomographic evidence.
    <br><br>
    My main area of work is conducting neurological MRI scans of brains 
    and spines on Siemens MRIs, as well as medical accounting and administering contrast agent during the 
    examinations.
    """
))

# Reversing the lists in place to get reverse chronological order.
# Why not create the list in this order to begin with?
# This is done to maintain future compatibility with a real database, where the natural order would
# also be chronological, based on the later primary keys being larger
experience_db_de.reverse()
experience_db_en.reverse()

education_db_en: list[Education] = []
education_db_en.append(Education(
    language=Language.en,
    institute="Europaschule Gymnasium Graf-Friedrich-Schule Diepholz",
    title="Abitur (Grade: 1.8)",
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
    description="Due to the Covid-19 pandemic, this major is not finished yet."
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
    description="Aufgrund der Covid-19-Pandemie ist dieses Studium bisher noch nicht abgeschlossen."
))

volunteering_db_en: list[Volunteering] = []
volunteering_db_en.append(Volunteering(
    language=Language.en,
    organisation="Fridays for Future",
    title="Web Developer and Organiser",
    start_date="August 2019",
    end_date="today",
    description="""To ensure that the Paris Climate Agreement of 2015 will be politically implemented, I organise
    political protests with Fridays for Future and have spoken with politicians, including those who represent us in the 
    European Parliament. As a group moderator I help create meetings with a productive and friendly environment.
    <br><br>
    I develop and run multiple web applications with Python, Django/Flask and Docker, that automate internal and 
    external 
    organisational procedures. External people who would like to support us can view tasks they could work on in a 
    <a href="https://github.com/wolfskaempf/helfffen" target="_blank">helpers portal</a>, where they can also directly 
    contact us if they choose to do a task. Internally, another app organises our 
    <a href="https://github.com/wolfskaempf/tops" target="_blank">topics of discussion</a> in a way, that ensures we 
    don't miss deadlines and thanks to the connected  
    <a href="https://github.com/wolfskaempf/elektronenhirn" target="_blank">chat bot</a> we will get notifications right
    where we see them.
    <br><br>
    With Docker and Ansible I also run various other web applications that allow privacy friendly online-collaboration
    since the start of the pandemic.
    """
))
volunteering_db_en.append(Volunteering(
    language=Language.en,
    organisation="European Youth Parliament Germany",
    title="Member of the Board",
    start_date="June 2016",
    end_date="June 2018",
    description="""As a member of the board of the European Youth Parliament (EYP) Germany, I was responsible for our 
    International Network and Member Management, as well as IT. I connected the 40 member countries of the EYP with each other, 
    mainly by organising the exchange of participants between countries and representing Germany at the international meetings of 
    the boards of the other 39 participating national committees.
    <br><br>
    Furthermore, I was responsible for managing our IT infrastructure and coordinating our internal communication strategy.
    To improve out internal processes, I developed multiple applications that improved the quality of the results significantly 
     and to this day automate time-intensive tasks.
    """
))
volunteering_db_en.append(Volunteering(
    language=Language.en,
    organisation="Tennis division of the Sports Community Diepholz of 1980 e.V.",
    title="Member of the Board",
    start_date="July 2013",
    end_date="January 2019",
    description="""As the youngest member of the board I was responsible for making our organisation more attractive for younger members
    and creating and maintaining our online presence."""
))
volunteering_db_en.append(Volunteering(
    language=Language.en,
    organisation="European Youth Parliament",
    title="Event Organiser",
    start_date="October 2014",
    end_date="October 2018",
    description="""As part of my engagement at the European Youth Parliament, I was a volunteer at over 40 multi-day
    events in different european cities. Depending on the event, my responsibilities ranged from group moderation,
     logistics and technical aspects or editorial work as part of the events social media."""
))

volunteering_db_de: list[Volunteering] = []
volunteering_db_de.append(Volunteering(
    language=Language.de,
    organisation="Fridays for Future",
    title="Webentwickler und Organisator",
    start_date="August 2019",
    end_date="heute",
    description="""Damit das Pariser Klimaabkommen von 2015 auch politisch umgesetzt wird, organisiere ich bei Fridays
    for Future Demonstrationen und führe Gespräche mit Politiker:innen, die uns unter anderem im Europäischen Parlament 
    repräsentieren. Als Gruppenmoderator sorge ich für produktive Treffen mit positiver Stimmung.
    <br><br>
    Ich entwickle und betreibe für FFF Webanwendungen mit Python, Django bzw. Flask, und Docker, mit denen interne und 
    externe Organisationsabläufe automatisiert werden. So können sich Menschen in einem 
    <a href="https://github.com/wolfskaempf/helfffen" target="_blank">Helfer:innenportal</a> bequem ansehen, welche 
    Aufgaben sie übernehmen könnten und haben die Möglichkeit sich direkt auf 
    der Seite bei uns zu melden. Intern organisiert eine andere Anwendung 
    <a href="https://github.com/wolfskaempf/tops" target="_blank">Tagesordnungspunkte</a> so, dass keine Fristen 
    verpasst werden und dank <a href="https://github.com/wolfskaempf/elektronenhirn" target="_blank">Chatbot</a> nichts 
    unter den Tisch fällt.
    <br><br>
    Mit Docker und Ansible betreibe ich für die Klimagerechtigkeitsbewegung noch diverse andere interne Webanwendungen, 
    die datenschutzfreundlich die digitale Zusammenarbeit seit Beginn der Covid-19-Pandemie ermöglichen.
    """
))
volunteering_db_de.append(Volunteering(
    language=Language.de,
    organisation="Europäisches Jugendparlament in Deutschland e.V.",
    title="Vorstandsmitglied",
    start_date="Juni 2016",
    end_date="Juni 2018",
    description="""Das Netzwerk des Europäischen Jugendparlaments (EJP) erstreckt sich über insgesamt 40 europäische 
    Länder, auch außerhalb der EU. Kernaufgabe meines Vorstandsressorts war es, den internationalen 
    Teilnehmer:innenaustausch zu organisieren und Deutschland auf den internationalen Treffen der Vorstände zu 
    repräsentieren.
    <br><br>
    Zudem war ich für die interne IT-Infrastruktur und unsere interne Kommunikationsstrategie verantwortlich. Um unsere 
    internen Prozesse zu verbessern, entwickelte ich Anwendungen, die die Ergebnisqualität deutlich anhoben und noch 
    heute zeitintensive Aufgaben automatisieren."""
))
volunteering_db_de.append(Volunteering(
    language=Language.de,
    organisation="Tennisabteilung der SG Diepholz von 1980 e.V.",
    title="Vorstandsmitglied",
    start_date="Juli 2013",
    end_date="Januar 2019",
    description="""Als das damals jüngstes Vorstandsmitglied gehörte es zu meinem Aufgabenbereich unseren Verein 
    attraktiver für junge Mitglieder zu machen. Ich erstellte und pflegte unsere Online-Präsenz."""
))
volunteering_db_de.append(Volunteering(
    language=Language.de,
    organisation="Europäisches Jugendparlament",
    title="Veranstaltungsorganisator",
    start_date="Oktober 2014",
    end_date="Oktober 2018",
    description="""Im Rahmen meines Engagements beim Europäischen Jugendparlament war ich ehrenamtlich auf über 
    40 mehrtägigen Veranstaltungen in verschiedenen europäischen Großstädten aktiv. Zu meinen Aufgaben gehörten je nach 
    Veranstaltung Gruppenmoderation, logistische und technische Organisation sowie redaktionelle Arbeit im Rahmen der 
    sozialen Medien der Veranstaltungen."""
))

trivia_db_en: list[Trivia] = []
trivia_db_en.append(Trivia(
    language=Language.en,
    content="This CV is built with FastAPI, Vue and Tailwind CSS."
))
trivia_db_en.append(Trivia(
    language=Language.en,
    content="""At the 36C3 I interpreted (translated) various talks,
     among them the legendary 
     <a href="https://media.ccc.de/v/36c3-10652-bahnmining_-_punktlichkeit_ist_eine_zier#l=eng&t=45" target="_blank">
     BahnMining-Talk</a> held by David Kriesel or a highly technical 
     <a href="https://media.ccc.de/v/36c3-10895-15_jahre_deutsche_telematikinfrastruktur_ti#l=eng"
     target="_blank">talk about the German health care system</a>, that really brought me to the edge of my 
     interpretation abilities."""
))
trivia_db_en.append(Trivia(
    language=Language.en,
    content="""I prefer tea over coffee, spring and autumn are the best seasons of the year and cats and dogs are 
    equally awesome."""
))
trivia_db_en.append(Trivia(
    language=Language.en,
    content="""I am passionate about cyber security. At 
    <a href="https://app.hackthebox.com/users/531118" target="_blank">HackTheBox</a>, a cyber-security 
    competition-platform, I am globally ranked #482, and on 
    <a href="https://tryhackme.com/p/wolfskto" target="_blank">TryHackMe</a>, a cyber-security learning-platform, 
    I am in the global top&nbsp3&nbsp%."""
))
trivia_db_en.append(Trivia(
    language=Language.en,
    content="""Using this 3D-printed 
    <a href="https://www.printables.com/de/model/62946-siemens-vida-mri-paper-holder" target="_blank">replacement part</a>, 
    that I designed for the 3 tesla MRI Siemens Vida, we have already saved a few thousand euros of repair costs,
    as the original part can only be purchased together with a technicians appointment."""
))

trivia_db_de: list[Trivia] = []
trivia_db_de.append(Trivia(
    language=Language.de,
    content="Dieses CV wurde mit FastAPI, Vue und Tailwind CSS erstellt."
))
trivia_db_de.append(Trivia(
    language=Language.de,
    content="""Auf dem 36C3 dolmetschte ich einige Vorträge, unter anderem den
    legendären <a href="https://media.ccc.de/v/36c3-10652-bahnmining_-_punktlichkeit_ist_eine_zier#l=eng&t=45"
    target="_blank">BahnMining-Vortrag</a> von David Kriesel oder einen hoch-technischen 
    <a href="https://media.ccc.de/v/36c3-10895-15_jahre_deutsche_telematikinfrastruktur_ti#l=eng"
    target="_blank">Talk über das deutsche Gesundheitswesen</a>, in dem ich wirklich an meine 
    dolmetscherischen Grenzen gebracht wurde."""
))
trivia_db_de.append(Trivia(
    language=Language.de,
    content="""Tee trinke ich lieber als Kaffee, Frühling und Herbst sind die besten Jahreszeiten, Katzen und Hunde sind
    gleichermaßen wunderbare Tiere."""
))
trivia_db_de.append(Trivia(
    language=Language.de,
    content="""Ich habe eine Leidenschaft für IT-Sicherheit. 
    Auf <a href="https://app.hackthebox.com/users/531118" target="_blank">HackTheBox</a>, einer 
    IT-Sicherheits-Wettbewerbs-Plattform bin ich im globalen Ranking auf Platz 482 und auf 
    <a href="https://tryhackme.com/p/wolfskto" target="_blank">TryHackMe</a>, einer IT-Sicherheits-Lernplattform bin 
    ich in den globalen Top 3&nbsp%."""
))
trivia_db_de.append(Trivia(
    language=Language.de,
    content="""Mit diesem 3D-gedruckten 
    <a href="https://www.printables.com/de/model/62946-siemens-vida-mri-paper-holder" target="_blank">Ersatzteil</a>, 
    das ich für das 3 Tesla MRT Siemens Vida entworfen habe, haben wir schon mehrere tausend Euro Reparaturkosten 
    gespart, da die Originalteile immer wieder zerbrachen und nur zusammen mit einem Technikereinsatz gekauft werden 
    konnten."""
))
