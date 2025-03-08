from password_validator import PasswordValidator

if __name__ == "__main__":
    user_input = input("Enter your password: ").strip()
    validator = PasswordValidator(user_input)

    if validator.check_password():
        print("Access granted!")
    else:
        print("Access denied!")
