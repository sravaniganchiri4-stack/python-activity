
# Password Policy Validation Engine

password = input("Enter a sample password: ")

errors = []
minimum_length = 8
prohibited = ["password", "admin", "1234"]

# Check minimum length
if len(password) < minimum_length:
    errors.append("Password must contain at least 8 characters")

# Check character categories
if not any(c.isupper() for c in password):
    errors.append("Add at least one uppercase letter")

if not any(c.islower() for c in password):
    errors.append("Add at least one lowercase letter")

if not any(c.isdigit() for c in password):
    errors.append("Add at least one digit")

if not any(not c.isalnum() for c in password):
    errors.append("Add at least one special character")

# Check repeated consecutive characters
if any(password[i] == password[i + 1]
       for i in range(len(password) - 1)):
    errors.append("Avoid consecutive repeated characters")

# Check prohibited substrings (case-insensitive)
for word in prohibited:
    if word in password.lower():
        errors.append("Contains prohibited substring: " + word)

# Display result
print("\n----- PASSWORD VALIDATION -----")

if errors:
    print("Password: INVALID")
    for error in errors:
        print("-", error)
else:
    print("Password: VALID")
    print("All password rules are satisfied.")
