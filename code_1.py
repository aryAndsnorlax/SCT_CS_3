import string

def check_password(password: str) -> None:
    length = len(password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(ch in string.punctuation for ch in password)

    score = 0
    score += (length >= 8)
    score += has_upper
    score += has_lower
    score += has_digit
    score += has_special

    print("\nCriteria Met:")
    print(f"Length >= 8: {'Yes' if length >= 8 else 'No'}")
    print(f"Uppercase: {'Yes' if has_upper else 'No'}")
    print(f"Lowercase: {'Yes' if has_lower else 'No'}")
    print(f"Numbers: {'Yes' if has_digit else 'No'}")
    print(f"Special Characters: {'Yes' if has_special else 'No'}")

    return score == 5


def main():
    while True:
        password = input("Enter your password to test: ")
        if check_password(password):
            print("\nOverall Strength: Strong")
            break
        else:
            print("\nPassword not strong enough. Please try again.\n")


if __name__ == "__main__":
    main()
