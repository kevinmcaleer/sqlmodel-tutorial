from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):  
    id: int | None = Field(default=None, primary_key=True)  
    name: str  
    secret_name: str  
    age: int | None = None  

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str # Password Hash
    age: int | None = None