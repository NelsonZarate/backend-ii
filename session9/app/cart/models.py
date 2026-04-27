from django.db import models


# Create your models here.
class Order(models.Model):
	cart = models.JSONField(default=dict, blank=True, null=True)
	total_price = models.DecimalField(max_digits=10, decimal_places=2)
	paid = models.BooleanField(default=False)
	updated_time = models.DateTimeField(auto_now=True)
	user_id = models.IntegerField()

	def __str__(self):
		return f"Order {self.pk} - user {self.user_id} - total {self.total_price}"


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	def __str__(self):
		return self.name