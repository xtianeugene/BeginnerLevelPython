import re
from datetime import datetime

def get_input(prompt, required=True, validator=None, error_msg=None):
    """Helper function to get and validate user input"""
    while True:
        value = input(prompt).strip()
        if not value and required:
            print(" ⚠ This field is required. Try again. Please try again.")
            continue
        if validator and value:
            if not validator(value):
                print(f" ⚠{error_msg or 'Invalid input. Please try again.'}")
                continue
        return value


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def validate_phone(phone):
    return re.match(r"^\+?\d{9,15}$", phone.replace(" ", "")) is not None

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def collect_personal_info():
    print("\n" + "=" * 60)
    print(" SECTION 1: PERSONAL IDENTIFICATION & CONTACT INFORMATION")
    print("=" * 60)

    data = {}
    data["full_name"] = get_input("Full Name: ")
    data["id_number"] = get_input("National ID/ Passport/ Birth Cert No.: ")
    data["date_of_birth"] = get_input("Date of Birth (DD/MM/YYYY): ", validator=validate_date, error_msg="Use format DD/MM/YYYY (e.g., 15/08/2005).")
    data["gender"] = get_input("Gender(Male/ Female/ Other): ")
    data["marital_status"] = get_input("Marital Status(Single/ Married/ Other): ")
    data["nationality"] = get_input("Nationality: ")
    data["religion"] = get_input("Religion (optional): ", required=False)
    data["postal_address"] = get_input("Postal Address (e.g., P.O Box 123, Nairobi): ")
    data["physical_location"] = get_input("Physical Location (County/ Sub County): ")
    data["phone"] = get_input(" Mobile Phone Number: ", validator=validate_phone, error_msg="Enter a valid phone number(9-15 digits).")
    data["email"] = get_input(" Email Address: ", validator=validate_email, error_msg="Enter a valid email address().")
    data["disability"] = get_input("Any Disability/ Special Need? (describe or type 'None'): ")
    return data

def collect_academic_info():
    print("\n" + "=" * 60)
    print(" SECTION 2: ACADEMIC INFORMATION & COURSE SELECTION")
    print("=" * 60)

    data = {}
    data["school_name"] = get_input("Secondary School Name: ")
    data["school_years"] = get_input("Years Attended (e.g., 2018-2022): ")
    data["index_number"] = get_input("KCSE Index Number: ")
    data["exam_year"] = get_input("Year of KCSE Examination: ")
    data["mean_grade"] = get_input("Mean Grade / Result: ")

    #Post secondary information
    has_post_sec = get_input("Do you have post-secondary qualifications? (yes/no): ").lower()
    if has_post_sec in ("yes", "y"):
        data["post_sec_qualification"] = get_input("Qualification (e.g., Diploma in IT): ")
        data["post_sec_institution"] = get_input("Institution: ")
        data["post_sec_year"] = get_input("Year Obtained: ")
    else:
        data["post_sec_qualification"] = "None"

    data["first_choice"] = get_input("First Choice Programme: ")
    data["second_choice"] = get_input("Second Choice Programme (optional): ", required=False)
    data["third_choice"] = get_input("Third Choice Programme (optional): ", required=False)
    data["mode_of_study"] = get_input("Mode of Study (Full-time/ Part-time/ eLearning): ")
    data["campus"] = get_input("Preferred Campus: ")
    data["intake"] = get_input("Intake/ Academic Year (e.g., Sept 2025): ")
    return data

def collect_family_info():
    print("\n" + "=" * 60)
    print(" SECTION 3: FAMILY, EMERGENCY & FINANCIAL DETAILS")
    print("="*60)

    data = {}
    #Parent/ Guardian
    data["guardian_name"] = get_input("Parent/ Guardian Full Name: ")
    data["guardian_relationship"] = get_input("Relationship (e.g., Father): ")
    data["guardian_phone"] = get_input("Parent/ Guardian Phone: ", validator=validate_phone, error_msg="Enter a valid phone number. ")
    data["guardian_occupation"] = get_input("Parent/ Guardian Occupation: ")
    data["guardian_alive"] = get_input("Is Guardian Alive? (yes/no): ")

    #Next of kin
    data["next_of_kin_name"] = get_input("Next of Kin Full Name: ")
    data["next_of_kin_relationship"] = get_input("Next of kin Relationship: ")
    data["next_of_kin_phone"] = get_input("Next of kin Phone: ", validator=validate_phone, error_msg="Enter a valid phone number. ")

    #Emergency contact
    data["emergency_name"] = get_input("Emergency Contact Name: ")
    data["emergency_phone"] = get_input("Emergency Contact Phone: ", validator=validate_phone, error_msg="Enter a valid phone number.")

    #Financing
    data["financing"] = get_input("How will studies be funded? (Self/ Parents/ HELB/ Sponsorship): ")
    return data

def collect_declaration():
    print("\n" + "=" * 60)
    print(" SECTION 4: DECLARATION & ATTACHMENTS")
    print("="*60)

    data = {}
    data["heard_about"] = get_input("How did you learn about the university? (optional): ", required=False)
    data["hobbies"] = get_input("Hobbies/ Sports Interests (optional): ", required=False)
    data["relatives_attended"] = get_input("Any relatives who attended this institution? (name or 'None'): ")

    print("\n--- Required Attachments (confirm you have them) ---")
    data["has_certificates"] = get_input("Copies of Certificates/ Transcripts? (yes/ no): ")
    data["has_id_copy"] = get_input("Copy of National ID/ Birth Certificate? (yes/ no): ")
    data["has_photos"] = get_input("Passport-sized Photographs? (yes/ no): ")
    data["has_payment_proof"] = get_input("Proof of Application Fee Payment? (yes/ no): ")

    print("\n--- Declaration ---")
    print("By typing 'yes', you confirm that all information provided is true")
    print("and accurate to the best of your knowledge.")
    data["declaration_accepted"] = get_input("Do you accept the declaration? (yes/ no): ")
    if data["declaration_accepted"].lower() in ("yes", "y"):
        data["signature"] = get_input("Type your full name as digital signature: ")
        data["declaration_date"] = datetime.now().strftime("%d/%m/%Y")
    else:
        data["signature"] = "NOT SIGNED"
        data["declaration_date"] = "N/A"
        print("You must accept the declaration to complete registration.")
        return data


def display_summary(all_data):
    print("\n" + "=" * 60)
    print(" REGISTRATION SUMMARY")
    print("=" * 60)
    for section, fields in all_data.items():
        print(f"\n--- {section} ---")
        for key, value in fields.items():
            label = key.replace("_", " ").title()
            print(f" {label} : {value if value else 'N/A'}")
        print("\n" + "=" * 60)
        print("✔ Registration form completed succesfully!")
        print("=" * 60)

def main():
    print("\n" + "=" * 60)
    print(" UNIVERSITY ENTRY REGISTRATION FORM")
    print("=" * 60)
    print("Please fill in all required fields. Type 'None' if not applicable.")

    all_data = {}
    all_data["Personal Information"] = collect_personal_info()
    all_data["Academic Information"] = collect_academic_info()
    all_data["Family & Financial Details"] = collect_family_info()
    all_data["Declaration & Attachments"] = collect_declaration()

    display_summary(all_data)

if __name__ == "__main__":
    main()