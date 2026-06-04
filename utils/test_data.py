from faker import Faker

fake = Faker()

class TestData:

    @staticmethod
    def registration_user():
        return {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "username": fake.user_name(),
            "email": fake.email(),
            "phone_number": fake.msisdn()[:10],
            "address": fake.address().replace("\n", ", "),
            "password": "Test@12345",
            "confirm_password": "Test@12345"
        }