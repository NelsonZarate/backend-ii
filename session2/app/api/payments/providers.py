
from app.api.payments.adapter import PaymentBaseAdapter


class MBWayPayment(PaymentBaseAdapter):
	async def pay(self, payload: dict) -> bool:
		# Simulate payment processing logic for MBWay
		print(f"Processing MBWay payment with payload: {payload}")
		return True

class PayPalPayment(PaymentBaseAdapter):
	async def pay(self, payload: dict) -> bool:
		# Simulate payment processing logic for PayPal
		print(f"Processing PayPal payment with payload: {payload}")
		return True