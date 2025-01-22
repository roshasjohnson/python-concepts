# Step 1: Define the custom exception
class InvalidAgeError(Exception):
    

    def __str__(self):
        return f" Age is not valide "

# Step 2: Use the custom exception
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    print(f"Age is set to {age}")

# Test the custom exception
try:
    1/0
except InvalidAgeError as e:
    print(e)
