import json
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

c = Contact("Srikanth", "9059057000", "contact@srikanthtechnologies.com")
print(json.dumps(c.__dict__)) # Convert object to dict before conversion to JSON