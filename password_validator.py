import logging
import os
from tkinter import messagebox

import bcrypt

logging.basicConfig(
    filename="password_validator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class PasswordValidator:
    """
    A class to validate a user's password against a stored password.
    The stored password is loaded from the env variable once and hashed.
    """

    def __init__(self):
        stored_password = os.getenv("MY_PASSWORD")

        if stored_password is None:
            logging.error("Environment variable MY_PASSWORD is not set.")
            raise ValueError("Environment variable MY_PASSWORD is not set.")

        # Hash the stored password once and store it in an instance variable.
        self.stored_hash = self.hash_password(stored_password)

    def hash_password(self, password: str) -> bytes:
        """
        Hashes the provided password using bcrypt.
        :param password: The plain text password to hash.
        :return: The hashed password as bytes.
        """
        salt = bcrypt.gensalt()  # Generate a random salt.
        try:
            password_bytes = password.encode('utf-8')
        except Exception as e:
            messagebox.showerror("Error", f"Encoding failed: {e}")
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password

    def check_password(self, entered_password: str) -> bool:
        """
        Checks whether the user-entered password matches the stored password.
        :param entered_password: The password input by the user.
        :return (bool): True if the password matches, False otherwise.
        """

        if not entered_password:
            messagebox.showwarning("Warning", "No password provided.")
            return False

        entered_password_bytes = entered_password.encode('utf-8')

        result = bcrypt.checkpw(entered_password_bytes, self.stored_hash)

        if result:
            messagebox.showinfo("Access granted!", "Access granted!")
            logging.info("Login successful!")
        else:
            messagebox.showwarning("Warning", "Login failed: Invalid password.")
            logging.warning("Login failed: Invalid password.")

        return result
