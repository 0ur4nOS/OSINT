Profile Generator (Sock Puppet)

A simple Python CLI tool to generate coherent fictional profiles for testing, demos, and prototyping. It outputs gender, first/last name, age (or age band), nationality, localized job title, date/place of birth, and a plausible Gmail address. Exports to JSON and/or CSV.

Important: This tool generates synthetic data for lawful, non-deceptive uses. It does not create real email accounts.
Features

    Interactive CLI with an option to randomize all parameters when “common parameters = No”.

    Localized content per country:

        Countries: France (FR), United States (US), Spain (ES).

        Job titles localized to each language: FR (French), US (English), ES (Spanish).

    Country-specific date formats:

        US: MM/DD/YYYY

        FR/ES: DD/MM/YYYY

    Retirement rule:

        If age>63, the job becomes “Retired” (localized) and the profile includes a “previous_job” field with the former job.

    Plausible Gmail address generator:

        ASCII-only local-part (accents removed), 6–30 chars.

        Common patterns: firstname.lastname, f.lastname, firstname+last initial, with optional year/digits.

        No availability check; no account creation.

    Export options:

        JSON (UTF-8, pretty-printed)

        CSV (UTF-8; semicolon delimiter by default)

Requirements

    Python 3.8+

Installation

    Copy generator.py into a working directory.

    (Optional) Create and activate a virtual environment:

        python -m venv .venv

        Windows: .venv\Scripts\activate

        macOS/Linux: source .venv/bin/activate

No external dependencies required.
Usage

    Run:

        python generator.py

    Workflow:

        Enter how many profiles to generate.

        Choose whether to set common parameters (gender, nationality, age) for all:

            1 = Yes: Provide once; used for all profiles.

            2 = No: No more questions; each profile is randomized (gender/country/age).

        Profiles are printed in a clean, boxed layout.

        Optionally export to JSON/CSV.

Example session

    How many profiles to generate? > 10

    Do you want to set common parameters for all?

        Yes

        No

        2

    (10 varied profiles are printed)

    Do you want to export the profiles?

        JSON

        CSV

        Both

        None

        3

    JSON filename (default: profiles.json) >

    CSV filename (default: profiles.csv) >

Output schema

Each profile includes:

    gender: Masculin | Féminin

    nationality: France | United States | Spain

    first_name

    last_name

    age

    date_of_birth: US=MM/DD/YYYY; FR/ES=DD/MM/YYYY

    place_of_birth

    job: localized per country

    previous_job (only when age>63)

    email: plausible Gmail address (string only)

Configuration

    Countries and datasets:

        Edit the DATA constant in generator.py to add or adjust:

            female_first_names, male_first_names, last_names

            birth_places

            jobs (localized language)

            age_bands

    Email format:

        Tweak build_gmail_localpart to enforce specific patterns (e.g., firstname.lastname) or avoid digits.

        Ensure the local-part remains 6–30 characters after slugification.

    CSV delimiter:

        Default ; (semicolon) for broader locale compatibility; change to , (comma) if preferred.

    Date formatting:

        Adjust format_dob_by_country to add rules for new countries.

    Retiree label:

        retired_label provides localized strings. You can make it gender-aware (e.g., FR: Retraité/Retraitée; ES: Jubilado/Jubilada).

Non-interactive/batch mode (optional)

    For full automation, add CLI flags (e.g., --count, --country, --gender, --age or --age-band, --export {json,csv,both}, --out-json, --out-csv) and bypass prompts accordingly.

    Alternatively, wrap main() with defaults or expose a function that returns a list of profiles directly.

Ethics and limitations

    Do not use generated data to impersonate real people, deceive, or defraud.

    Gmail addresses are strings only; they are not reserved and no account is created.

    Lists aim for plausibility, not demographic/statistical accuracy.

    Comply with laws, privacy rules, and providers’ Terms of Service.

Project structure

    generator.py

        DATA (names, places, localized jobs, age bands)

        Input helpers

        Gmail local-part builder

        Field generators (names, dates, places, jobs)

        Country-specific date formatting

        Retiree logic (age>63 -> job “Retired”, with previous_job)

        Profile formatter and exporters

        Interactive main loop

Roadmap

    CLI arguments for full batch automation.

    More countries with localized datasets.

    Optional synthetic photo generation (AI-generated faces) and photo_path field.

    Deterministic runs via --seed.

    Configurable email policy (force separators, disallow digits, etc.).

    Gender-aware retiree labels for FR/ES.

License

Intended for educational and experimental use. If you publish or distribute, include a license (MIT/Apache-2.0/GPL) and ensure compliance with applicable laws and Terms of Service.
Disclaimer

This repository provides tools for generating synthetic test data. Use responsibly and transparently. The authors are not responsible for misuse.
