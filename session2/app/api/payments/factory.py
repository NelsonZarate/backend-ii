from app.api.payments.adapter import PaymentBaseAdapter
from ast import match_case

from app.api.payments.providers import MBWayPayment, PayPalPayment


class PaymentProviderFactory:
	REGISTRY: dict[str, type[PaymentBaseAdapter]] = {
		"mbway": MBWayPayment,
		"paypal": PayPalPayment
	}
	def get_provider(self, provider_name: str) -> PaymentBaseAdapter:
		provider = self.REGISTRY.get(provider_name.lower(), None)
		if not provider:
			raise ValueError(f"Unsupported payment provider: {provider_name}")
		return provider()