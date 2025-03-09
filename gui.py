import tkinter as tk

from password_validator import PasswordValidator


class GUI:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Password Validator")
        self.root.geometry("280x200")
        self.root.config(padx=10, pady=10)

        self.label = tk.Label(self.root, text="Enter your password:")
        self.label.pack()

        self.password_entry = tk.Entry(self.root, width=35, show="*")
        self.password_entry.pack()

        # Create a BooleanVar to track the state of the "Show password" checkbox.
        self.show_password = tk.BooleanVar(value=False)
        self.show_password_checkbox = tk.Checkbutton(
            self.root,
            text="Show password",
            variable=self.show_password,
            command=self.toggle_password
        )
        self.show_password_checkbox.pack()

        # Instantiate PasswordValidator once and store it.
        self.validator = PasswordValidator()
        self.validate_button = tk.Button(
            self.root, text="Validate", width=30,
            command=lambda: self.validator.check_password(self.password_entry.get().strip()),
            highlightthickness=0
        )
        self.validate_button.pack()

        self.exit_button = tk.Button(
            self.root, text="Exit", width=30,
            command=self.root.quit, highlightthickness=0)

        self.exit_button.pack()

    def toggle_password(self):
        """
        Toggle the password visibility based on the checkbox's state
        """

        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
