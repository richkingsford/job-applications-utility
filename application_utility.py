"""Dependency-free helpers for job-application workflows."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PROFILE = ROOT / "profile.json"
REQUIRED = {"identity": ["legal_name", "email", "phone", "city_state", "resume_path"], "work_authorization": ["authorized_us", "requires_sponsorship"], "education": ["highest_level"]}
ASHBY_FIELDS = {"legal_name": "Legal Name*", "email": "Email Address*", "phone": "Mobile Number*", "city_state": "Location - City and State of Residence", "resume": "Resume*", "authorized_us": "Are you legally authorized to work in the United States?", "requires_sponsorship": "Will you now or in the future require sponsorship for employment visa status?", "highest_education": "Please share your highest level of education completed", "earliest_start_date": "What is your earliest preferred start date if hired?", "salary_alignment": "Does the posted salary or hourly pay range align with your expectations?"}

def load_profile():
    if not PROFILE.exists():
        raise SystemExit("Missing profile.json; copy profile.example.json and fill it locally.")
    return json.loads(PROFILE.read_text(encoding="utf-8"))

def validate_profile():
    profile = load_profile(); missing = []
    for section, keys in REQUIRED.items():
        for key in keys:
            if profile.get(section, {}).get(key) in (None, ""): missing.append(f"{section}.{key}")
    if missing:
        print("Missing required profile fields:\n" + "\n".join(f"- {x}" for x in missing)); return 1
    print("Profile structure is valid; personal values were not displayed."); return 0

def main(argv):
    command = argv[1] if len(argv) > 1 else "help"
    if command == "validate-profile": return validate_profile()
    if command == "ashby-fields": print(json.dumps(ASHBY_FIELDS, indent=2)); return 0
    print("Commands: validate-profile | ashby-fields"); return 0

if __name__ == "__main__": raise SystemExit(main(sys.argv))
