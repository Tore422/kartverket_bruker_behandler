class User:

    def __init__(self, name, date_of_birth, phone_number, email_address):
        self.name = name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.email_address = email_address

    def __str__(self) -> str:
        return f"{self.name}, {self.date_of_birth}, {self.phone_number}, {self.email_address}"
    