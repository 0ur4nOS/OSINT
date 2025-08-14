#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
import csv
import re
import unicodedata
from datetime import date, timedelta
from pathlib import Path

# ===============================
# Data (localized jobs)
# ===============================

DATA = {
    "France": {
        "female_first_names": [
            "Emma","Olivia","Camille","Marie","Chloé","Jeanne","Lucie","Léa","Manon","Sarah",
            "Charlotte","Inès","Lola","Zoé","Jade","Anaïs","Claire","Julie","Pauline","Alice",
            "Elisa","Eva","Nina","Maëlle","Lou","Adèle","Ambre","Romane","Noémie","Amandine",
            "Alicia","Victoire","Agathe","Héloïse","Coline","Capucine","Roxane","Mila","Lina","Ava",
            "Élise","Eléna","Jeanne","Clémence","Élodie","Aurélie","Margo","Salomé","Candice","Mathilde"
        ],
        "male_first_names": [
            "Lucas","Thomas","Hugo","Gabriel","Louis","Paul","Antoine","Nathan","Julien","Maxime",
            "Arthur","Romain","Adrien","Victor","Théo","Enzo","Noé","Ethan","Mathis","Baptiste",
            "Alexis","Quentin","Léo","Pierre","Simon","Benjamin","Nicolas","Martin","Guillaume","Raphaël",
            "Sacha","Jules","Clément","Samuel","Tristan","Kylian","Yohan","Matteo","Gaspard","Noah",
            "Évan","Timothée","Amaury","César","Diego","Hadrien","Valentin","Thibault","Florian","Kevin"
        ],
        "last_names": [
            "Martin","Bernard","Dubois","Durand","Moreau","Lefevre","Leroy","Roux","Petit","Richard",
            "Simon","Michel","Garcia","Laurent","Lefebvre","Fournier","Roussel","Lopez","Dupont","Faure",
            "Caron","Gauthier","Lambert","Henry","Bonnet","Robin","Girard","Mathieu","Masson","Marchand",
            "Nicolas","Colin","Guillaume","Meyer","Perez","Fontaine","Chevalier","Rousseau","Blanchard","Vidal",
            "Dupuis","Guerin","Muller","Leclerc","Lefort","Martel","Barbier","Pruvost","Brun","Perrot",
            "Renard","Boutin","Schneider","Baron","Hebert","Roy","Huet","Gonzalez","Morin","Philippe"
        ],
        "birth_places": [
            "Paris","Marseille","Lyon","Toulouse","Nice","Nantes","Strasbourg","Montpellier","Bordeaux","Lille",
            "Rennes","Reims","St-Étienne","Toulon","Le Havre","Grenoble","Dijon","Angers","Nîmes","Villeurbanne",
            "Clermont-Ferrand","Saint-Denis","Brest","Limoges","Tours"
        ],
        "jobs": [
            "Ingénieur logiciel","Développeur web","Analyste de données","Chef de projet","Infirmier",
            "Professeur des écoles","Comptable","Designer graphique","Consultant","Commercial",
            "Responsable marketing","Technicien réseau","Architecte","Juriste","Médecin","Pharmacien",
            "Community manager","Designer UX","Product owner","Ingénieur data","Boulanger",
            "Électricien","Plombier","Chef de produit","Journaliste","Photographe","Coach sportif",
            "Chef cuisinier","Avocat","Notaire","Contrôleur de gestion","Chargé de communication",
            "Statisticien","Ingénieur systèmes","Administrateur systèmes","Analyste cybersécurité",
            "Ingénieur QA","Ergonome","Orthophoniste","Kinésithérapeute","Chargé RH"
        ],
        "age_bands": {
            "15-24": (15, 24),
            "25-34": (25, 34),
            "35-44": (35, 44),
            "45-54": (45, 54),
            "55-64": (55, 64),
            "65-80": (65, 80)
        }
    },
    "United States": {
        "female_first_names": [
            "Emma","Olivia","Ava","Sophia","Isabella","Mia","Charlotte","Amelia","Harper","Evelyn",
            "Abigail","Emily","Elizabeth","Sofia","Avery","Ella","Scarlett","Grace","Chloe","Victoria",
            "Riley","Aria","Lily","Aubrey","Zoey","Penelope","Nora","Hannah","Layla","Lillian",
            "Addison","Eleanor","Natalie","Luna","Savannah","Brooklyn","Zoe","Leah","Stella","Hazel",
            "Violet","Aurora","Bella","Claire","Skylar","Lucy","Paisley","Anna","Caroline","Genesis"
        ],
        "male_first_names": [
            "Liam","Noah","William","James","Benjamin","Elijah","Oliver","Lucas","Mason","Logan",
            "Alexander","Ethan","Jacob","Michael","Daniel","Henry","Jackson","Sebastian","Aiden","Matthew",
            "Samuel","David","Joseph","Carter","Owen","Wyatt","John","Jack","Luke","Jayden",
            "Dylan","Grayson","Levi","Isaac","Gabriel","Julian","Mateo","Anthony","Jaxon","Lincoln",
            "Joshua","Christopher","Andrew","Theodore","Caleb","Ryan","Asher","Nathan","Thomas","Leo"
        ],
        "last_names": [
            "Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez",
            "Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin",
            "Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson",
            "Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Green",
            "Adams","Baker","Nelson","Carter","Mitchell","Roberts","Turner","Phillips","Campbell","Parker",
            "Evans","Edwards","Collins","Stewart","Morris","Rogers","Reed","Cook","Morgan","Bailey"
        ],
        "birth_places": [
            "New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia","San Antonio","San Diego","Dallas","San Jose",
            "Austin","Jacksonville","Fort Worth","Columbus","Charlotte","San Francisco","Indianapolis","Seattle","Denver","Washington",
            "Boston","El Paso","Nashville","Detroit","Portland"
        ],
        "jobs": [
            "Software Engineer","Web Developer","Data Analyst","Product Manager","Nurse","Teacher","Accountant","Graphic Designer",
            "Marketing Manager","Sales Representative","Network Engineer","Systems Administrator","Cybersecurity Analyst",
            "Mechanical Engineer","Electrical Engineer","Physician","Pharmacist","Journalist","Chef","Photographer",
            "Personal Trainer","Lawyer","Financial Analyst","Consultant","UX Designer","Data Engineer","QA Engineer",
            "Project Manager","Operations Manager","HR Specialist","Construction Worker","Electrician","Plumber","Truck Driver",
            "Barista","Retail Associate","Content Writer","Social Media Manager","Research Scientist","Biostatistician"
        ],
        "age_bands": {
            "15-24": (15, 24),
            "25-34": (25, 34),
            "35-44": (35, 44),
            "45-54": (45, 54),
            "55-64": (55, 64),
            "65-80": (65, 80)
        }
    },
    "Spain": {
        "female_first_names": [
            "Lucia","Sofia","Martina","Paula","Julia","Valeria","Alba","Carmen","Laura","Sara",
            "Claudia","Daniela","Irene","Aitana","Vega","Noa","Nerea","Lola","Elena","Marina",
            "Candela","Triana","Ana","Carla","Vera","Olivia","Marta","Emma","Laia","Adriana",
            "Ines","Andrea","Alicia","Carlota","Rocio","Jimena","Mia","Lia","Ariadna","Alejandra",
            "Blanca","Ainhoa","Eva","Isabel","Beatriz","Angela","Pilar","Teresa","Sonia","Belen"
        ],
        "male_first_names": [
            "Hugo","Martin","Lucas","Mateo","Leo","Daniel","Pablo","Alejandro","Adrian","Diego",
            "Javier","Mario","Bruno","Sergio","Nicolas","Marcos","Manuel","David","Ivan","Ruben",
            "Jorge","Alvaro","Oscar","Raul","Gonzalo","Iker","Eric","Enzo","Pedro","Jaime",
            "Antonio","Carlos","Fernando","Rafael","Victor","Samuel","Julian","Marco","Gael","Unai",
            "Xavier","Hector","Andres","Cristian","Juan","Alberto","Tomas","Emilio","Miguel","Ignacio"
        ],
        "last_names": [
            "Garcia","Martinez","Lopez","Sanchez","Gonzalez","Perez","Rodriguez","Fernandez","Gomez","Diaz",
            "Hernandez","Munoz","Jimenez","Romero","Alonso","Gutierrez","Navarro","Torres","Dominguez","Vazquez",
            "Ramos","Ruiz","Blanco","Molina","Ortega","Delgado","Castro","Cruz","Morales","Herrera",
            "Rubio","Santana","Nunez","Ibanez","Vidal","Rey","Leon","Cabrera","Bautista","Gallardo",
            "Soler","Esteban","Benitez","Vicente","Carmona","Martin","Santos","Lorenzo","Pardo","Rivas",
            "Aguilar","Marquez","Vega","Calvo","Carrasco","Campos","Prieto","Pena","Cano","Castillo"
        ],
        "birth_places": [
            "Madrid","Barcelona","Valencia","Sevilla","Zaragoza","Malaga","Murcia","Palma","Las Palmas","Bilbao",
            "Alicante","Cordoba","Valladolid","Vigo","Gijon","Hospitalet","La Coruna","Granada","Elche","Oviedo",
            "Tarragona","Santander","San Sebastian","Badajoz","Salamanca"
        ],
        "jobs": [
            "Ingeniero de software","Desarrollador web","Analista de datos","Product manager","Enfermera","Profesor",
            "Contable","Diseñador gráfico","Responsable de marketing","Comercial","Ingeniero de redes",
            "Administrador de sistemas","Analista de ciberseguridad","Ingeniero mecánico","Ingeniero eléctrico",
            "Médico","Farmacéutico","Periodista","Chef","Fotógrafo","Entrenador personal","Abogado",
            "Analista financiero","Consultor","Diseñador UX","Ingeniero de datos","QA engineer",
            "Project manager","Operaciones","RRHH","Electricista","Fontanero","Conductor","Camarero",
            "Dependiente","Community manager","Investigador","Bioestadístico"
        ],
        "age_bands": {
            "15-24": (15, 24),
            "25-34": (25, 34),
            "35-44": (35, 44),
            "45-54": (45, 54),
            "55-64": (55, 64),
            "65-80": (65, 80)
        }
    }
}

GENDERS = ["Masculin", "Féminin"]

# ===============================
# Input utilities
# ===============================

def input_choice(prompt, choices):
    print(prompt)
    for i, c in enumerate(choices, 1):
        print(f"{i}. {c}")
    while True:
        raw = input("> ").strip()
        if raw.isdigit():
            idx = int(raw)
            if 1 <= idx <= len(choices):
                return choices[idx - 1]
        for c in choices:
            if raw.lower() == c.lower():
                return c
        print("Invalid input. Try again.")

def input_age_or_band(nationality):
    bands = list(DATA[nationality]["age_bands"].keys())
    print("Enter an exact age or pick an age band?")
    print("1. Exact age (integer)")
    print("2. Age band (e.g., 25-34)")
    while True:
        choice = input("> ").strip()
        if choice == "1":
            while True:
                raw_age = input("Age (15 to 80) > ").strip()
                if raw_age.isdigit():
                    age = int(raw_age)
                    if 15 <= age <= 80:
                        return age
                print("Invalid age. Enter an integer between 15 and 80.")
        elif choice == "2":
            band = input_choice("Choose a band:", bands)
            low, high = DATA[nationality]["age_bands"][band]
            return random.randint(low, high)
        else:
            print("Invalid choice. Type 1 or 2.")

# ===============================
# Gmail helpers (plausible address)
# ===============================

def slugify_name(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "", s)
    return s

def pick_separator() -> str:
    return random.choice([".", "_", ""])

def random_digits(n=2) -> str:
    import string
    return "".join(random.choices(string.digits, k=n))

def build_gmail_localpart(first_name: str, last_name: str, birth_year: int = None) -> str:
    f = slugify_name(first_name)
    l = slugify_name(last_name)
    sep = pick_separator()

    candidates = [
        f"{f}{sep}{l}",
        f"{f[0]}{sep}{l}",
        f"{f}{l}",
        f"{l}{sep}{f}",
    ]
    if birth_year:
        candidates += [
            f"{f}{sep}{l}{birth_year}",
            f"{f}{birth_year}",
            f"{l}{birth_year}",
        ]
    for _ in range(3):
        candidates.append(f"{f}{sep}{l}{random_digits(random.choice([1,2,3]))}")
        candidates.append(f"{f}{random_digits(2)}")
        candidates.append(f"{l}{random_digits(2)}")

    seen, uniq = set(), []
    for c in candidates:
        if 6 <= len(c) <= 30 and c not in seen:
            seen.add(c)
            uniq.append(c)
    return random.choice(uniq) if uniq else (f"{f}{l}{random_digits(3)}")[:30]

# ===============================
# Field generation
# ===============================

def random_birthdate_from_age(age):
    today = date.today()
    days_old = age * 365 + random.randint(-183, 183)
    dob = today - timedelta(days=days_old)
    if dob >= today:
        dob = today - timedelta(days=age * 365 + random.randint(1, 365))
    return dob

def pick_name(nationality, gender):
    d = DATA[nationality]
    if gender.lower().startswith("f"):
        first = random.choice(d["female_first_names"])
    else:
        first = random.choice(d["male_first_names"])
    last = random.choice(d["last_names"])
    return first, last

def pick_birth_place(nationality):
    return random.choice(DATA[nationality]["birth_places"])

def pick_job(nationality):
    return random.choice(DATA[nationality]["jobs"])

def format_dob_by_country(nationality, dob):
    # US: MM/DD/YYYY, others: DD/MM/YYYY
    if nationality == "United States":
        return dob.strftime("%m/%d/%Y")
    return dob.strftime("%d/%m/%Y")

def retired_label(nationality, gender=None):
    """
    Localized 'Retired' label.
    If you want gender-specific labels (FR/ES), pass gender and adapt below.
    """
    if nationality == "France":
        # Optionally: return "Retraitée" if gender starts with 'f'
        return "Retraité"
    if nationality == "Spain":
        # Optionally: return "Jubilada" if gender starts with 'f'
        return "Jubilado"
    return "Retired"

# ===============================
# Profile and export
# ===============================

def generate_profile(gender=None, nationality=None, age=None):
    # If parameters are None, ask the user (used only when "common params = Yes")
    if gender is None:
        gender = input_choice("Choose a gender:", GENDERS)
    if nationality is None:
        nationality = input_choice("Choose a nationality:", list(DATA.keys()))
    if age is None:
        age = input_age_or_band(nationality)

    first_name, last_name = pick_name(nationality, gender)
    dob = random_birthdate_from_age(age)
    birth_place = pick_birth_place(nationality)
    selected_job = pick_job(nationality)  # may become previous_job if retired
    birth_year = dob.year

    # Email
    localpart = build_gmail_localpart(first_name, last_name, birth_year)
    email = f"{localpart}@gmail.com"

    # Retiree logic
    if age > 63:
        job = retired_label(nationality, gender=gender)
        previous_job = selected_job
    else:
        job = selected_job
        previous_job = None

    profile = {
        "gender": gender,
        "nationality": nationality,
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "date_of_birth": format_dob_by_country(nationality, dob),
        "place_of_birth": birth_place,
        "job": job,
        "email": email
    }
    if previous_job:
        profile["previous_job"] = previous_job

    return profile

def format_profile(profile, index=None, width=22):
    header = f"Profile #{index}" if index is not None else "Generated profile"
    sep = "-" * (width + 28)
    lines = [
        sep,
        f"{header}",
        sep,
        f"{'Gender':<{width}}: {profile['gender']}",
        f"{'Nationality':<{width}}: {profile['nationality']}",
        f"{'First name':<{width}}: {profile['first_name']}",
        f"{'Last name':<{width}}: {profile['last_name']}",
        f"{'Age':<{width}}: {profile['age']}",
        f"{'Date of birth':<{width}}: {profile['date_of_birth']}",
        f"{'Place of birth':<{width}}: {profile['place_of_birth']}",
        f"{'Job':<{width}}: {profile['job']}",
    ]
    if "previous_job" in profile and profile["previous_job"]:
        label = "Previous job"
        if profile["nationality"] == "France":
            label = "Ancien métier"
        elif profile["nationality"] == "Spain":
            label = "Trabajo anterior"
        lines.append(f"{label:<{width}}: {profile['previous_job']}")
    lines.append(f"{'Email':<{width}}: {profile['email']}")
    lines.append(sep)
    return "\n".join(lines)

def print_profile(profile, index=None):
    print(format_profile(profile, index=index))

def export_json(profiles, path):
    path = Path(path)
    path.write_text(json.dumps(profiles, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] JSON exported -> {path.resolve()}")

def export_csv(profiles, path):
    path = Path(path)
    if not profiles:
        print("[!] Nothing to export.")
        return
    headers = list(profiles[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter=";")
        writer.writeheader()
        writer.writerows(profiles)
    print(f"[OK] CSV exported -> {path.resolve()}")

# ===============================
# Main loop (console)
# ===============================

def main():
    print("=== Profile Generator ===")
    # Count
    while True:
        raw = input("How many profiles to generate? > ").strip()
        if raw.isdigit() and int(raw) >= 1:
            n = int(raw)
            break
        print("Please enter an integer >= 1.")

    # Common params?
    print("Do you want to set common parameters (gender, nationality, age) for all?")
    print("1. Yes")
    print("2. No")
    while True:
        choice = input("> ").strip()
        if choice in ("1", "2"):
            break
        print("Type 1 or 2.")

    profiles = []

    if choice == "1":
        # Ask once, then generate without re-asking
        gender = input_choice("Choose a gender:", GENDERS)
        nationality = input_choice("Choose a nationality:", list(DATA.keys()))
        age = input_age_or_band(nationality)
        for i in range(1, n + 1):
            p = generate_profile(gender=gender, nationality=nationality, age=age)
            profiles.append(p)
            print_profile(p, index=i)
    else:
        # No more questions: randomize each profile
        for i in range(1, n + 1):
            gender = random.choice(GENDERS)
            nationality = random.choice(list(DATA.keys()))
            low, high = random.choice(list(DATA[nationality]["age_bands"].values()))
            age = random.randint(low, high)
            p = generate_profile(gender=gender, nationality=nationality, age=age)
            profiles.append(p)
            print_profile(p, index=i)

    # Export
    print("Do you want to export the profiles?")
    print("1. JSON")
    print("2. CSV")
    print("3. Both")
    print("4. None")
    while True:
        exp = input("> ").strip()
        if exp in ("1", "2", "3", "4"):
            break
        print("Type 1, 2, 3 or 4.")

    if exp in ("1", "3"):
        fname = input("JSON filename (default: profiles.json) > ").strip() or "profiles.json"
        export_json(profiles, fname)
    if exp in ("2", "3"):
        fname = input("CSV filename (default: profiles.csv) > ").strip() or "profiles.csv"
        export_csv(profiles, fname)

    print("Done.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")

