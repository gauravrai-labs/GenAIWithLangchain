from typing import TypedDict

class UserProfile(TypedDict):
    name: str
    age: int
    email: str
    is_active: bool

person1 = UserProfile(name = "Gaurav", age = 30, email = "gaurav@example.com", is_active = True)
