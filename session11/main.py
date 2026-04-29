import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

users = []

@strawberry.type
class User:
    id: int
    name: str
@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        return User(id=id, name="John Doe")
    
    @strawberry.field
    def users(self) -> list[User]:
        return users

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name:str) -> User:
        new_user = User(id=len(users)+1 , name=name)
        users.append(new_user)
        return new_user



schema = strawberry.Schema(query=Query , mutation=Mutation)
graphql_app = GraphQL(schema)
app = FastAPI()
app.add_route("/graphql", graphql_app)
