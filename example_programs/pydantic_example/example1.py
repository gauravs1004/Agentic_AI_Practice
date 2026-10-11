from pydantic import BaseModel, EmailStr, PositiveInt, ValidationError

# create venv, activate venv, pip3 install pydantic

class GeminiResponse(BaseModel):
    text: str
    tokens: PositiveInt
    success: str
    email: EmailStr

try:
    response1 = GeminiResponse(
        text="Python is a Prpgramming Language",
        tokens="100",
        success="true",
        email="abhinav@hello.com"
    )

    print(response1)
except ValidationError as e:
    print({"error":e})
