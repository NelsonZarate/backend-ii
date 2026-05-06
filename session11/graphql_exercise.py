"""Session 11: simple Strawberry GraphQL example."""
import strawberry
from strawberry.asgi import GraphQL

@strawberry.type
class User:
    id: int
    name: str

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        return User(id=id, name="John Doe")

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

if __name__ == "__main__":
    print("Mount `graphql_app` in an ASGI server, e.g. FastAPI or use `uvicorn` with ASGI wrapper.")
