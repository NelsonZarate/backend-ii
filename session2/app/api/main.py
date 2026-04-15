from fastapi import FastAPI
from pydantic import BaseModel

from app.api.payments.adapter import PaymentBaseAdapter
from app.api.payments.factory import PaymentProviderFactory
from ..schemas.models import PaymentRequest

def create_app() -> FastAPI:
	app = FastAPI()

	@app.get("/")
	def read_root():
		return {"message": "Hello from FastAPI in Docker 🚀"}

	@app.post("/pay")
	async def pay(payload: PaymentRequest):
		provider:PaymentBaseAdapter = PaymentProviderFactory().get_provider(payload.payment_method)
		await provider.pay(payload=payload.payment_payload)
		return {"message": f"Payment processed for {payload.email}"}

	@app.get("/message")
	def get_message():
		return {"message": "This is a simple message from the API."}

	return app

app = create_app()
