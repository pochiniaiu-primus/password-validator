import os
import logging

import bcrypt

logging.basicConfig(
    filename="password_validator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class PasswordValidator:
    """
    A class to validate a user's password against a stored password.
    """

    def __init__(self, entered_password):
        self.entered_password = entered_password

    def hash_password(self, password):
        """
        Hashes the provided password using bcrypt.
        :param password: The plain text password to hash.
        :return: The hashed password.
        """
        salt = bcrypt.gensalt()
        password_bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password

    def check_password(self):
        """
        Checks whether the user-entered password matches the stored password.
        :return (bool): True if the password match, False otherwise.
        """
        stored_password = os.getenv("MY_PASSWORD")

        if stored_password is None:
            logging.error("Environment variable MY_PASSWORD is not set.")
            raise ValueError("Environment variable MY_PASSWORD is not set.")

        stored_hash = self.hash_password(stored_password)

        entered_password_bytes = self.entered_password.encode('utf-8')

        result = bcrypt.checkpw(entered_password_bytes, stored_hash)

        if result:
            logging.info("Login successful!")
        else:
            logging.warning("Login failed: Invalid password.")

        return result
