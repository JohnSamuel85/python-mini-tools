import random
import string

def get_user_preferences():
    print("\n--- Password Generator ---")

    length = int(input("Enter password length (min 6): "))
    if length < 6:
        print("Password too short. Setting to 6 by default.")
        length = 6

    use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

    if not (use_upper or use_lower or use_digits or use_symbols):
        print("No options selected. Enabling all by default.")
        use_upper = use_lower = use_digits = use_symbols = True

    return length, use_upper, use_lower, use_digits, use_symbols


def build_character_pool(use_upper, use_lower, use_digits, use_symbols):
    pool = ""

    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    return pool


def generate_password(length, pool):
    password = ''.join(random.choice(pool) for _ in range(length))
    return password


def strength_check(password):
    strength = 0

    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if strength == 4:
        return "STRONG"
    elif strength == 3:
        return "MODERATE"
    else:
        return "WEAK"


def main():
    length, use_upper, use_lower, use_digits, use_symbols = get_user_preferences()
    pool = build_character_pool(use_upper, use_lower, use_digits, use_symbols)
    password = generate_password(length, pool)
    strength = strength_check(password)

    print("\n--- RESULT ---")
    print("Generated Password:", password)
    print("Password Strength:", strength)


if __name__ == "__main__":
    main()
