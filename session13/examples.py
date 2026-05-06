"""Session 13: minimal Django view and FastAPI app examples."""


# Django style view example (place in a Django views.py)
def django_index(request):
    from django.http import JsonResponse

    return JsonResponse({"message": "Hello from Django"})


# FastAPI example
def create_fastapi_app():
    try:
        from fastapi import FastAPI
    except Exception:
        return None
    app = FastAPI()

    @app.get("/")
    async def index():
        return {"message": "Hello from FastAPI"}

    return app


if __name__ == "__main__":
    app = create_fastapi_app()
    if app is None:
        print("Install fastapi/uvicorn to run the FastAPI example")
    else:
        print("Run with: uvicorn session13.examples:create_fastapi_app --reload")
