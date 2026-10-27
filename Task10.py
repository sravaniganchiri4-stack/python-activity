
# Student Email and Identifier Validation

import re

email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

errors = []

# Email validation
if not email:
    errors.append("Email is missing")
else:
    if email.count("@") != 1:
        errors.append("Email must contain exactly one @ symbol")
    else:
        username, domain = email.split("@")

        if not username:
            errors.append("Email username is missing")

        if not domain:
            errors.append("Email domain is missing")
        elif "." not in domain:
            errors.append("Email domain must contain a dot")

        if email.startswith(".") or email.endswith("."):
            errors.append("Email cannot start or end with a dot")

        if ".." in email:
            errors.append("Email contains consecutive dots")

        if not re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
            errors.append("Email contains invalid characters or format")

# Registration ID validation
# Required format: STU followed by 4 digits
if not reg_id:
    errors.append("Registration ID is missing")
elif not re.fullmatch(r"STU[0-9]{4}", reg_id):
    errors.append(
        "Registration ID must be STU followed by exactly 4 digits"
    )

# Display results
print("\n----- VALIDATION REPORT -----")

if errors:
    for error in errors:
        print("-", error)
    print("Status: INVALID")
else:
    print("Email: VALID")
    print("Registration ID: VALID")
    print("Status: ALL DETAILS VALID")
