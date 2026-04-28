from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    email: EmailStr # Using EmailStr from pydantic to validate email addresses ,  we can use str instead of EmailStr if we don't want to validate email addresses

new_user = User(name="Gaurav", age=30, email="gaurav@example.com")
print(new_user)


# we can also set default values for fields in the model, which allows us to create instances without providing all the information. For example, we can set a default value for the grade field in a Student model:
class Student(BaseModel):
    name: str
    age: int
    grade: int = 10  # Default value for grade is set to 10
    cgpa: float = Field(gt=0, lt=10)  # Using Field to set constraints on cgpa (must be between 0 and 10)

new_student = Student(name="Gaurav", age=30, cgpa=8.5) # Since grade has a default value, we can omit it when creating a new Student instance
print(new_student)

# We can also make fields optional by using the Optional type hint from the typing module. This allows us to create instances without providing values for those fields. For example, we can make the price field optional in a Car model:
class Car(BaseModel):
    brand: str
    price: Optional[int] = None
    model: str

new_car = Car(brand="Toyota", model="Camry")
print(new_car)