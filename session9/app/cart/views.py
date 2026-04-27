from django.shortcuts import render,redirect
from django.http import HttpResponse

from .form import AddToCartForm
from .models import Product

def create_sample_products():
	if Product.objects.count() == 0:
		print("Creating sample products...")  # 👈 debug
		Product.objects.create(name="Product A", price=10.00)
		Product.objects.create(name="Product B", price=20.00)
		Product.objects.create(name="Product C", price=30.00)

def product_list(request):
	create_sample_products()
	products = Product.objects.all()
	print("TOTAL PRODUCTS:", products.count())  # 👈 debug
	form = AddToCartForm()
	return render(request, "cart/product_list.html", 
		{"products": products, "form": form})

def add_to_cart(request, product_id):
	if request.method == "POST":
		form = AddToCartForm(request.POST)
		if form.is_valid():
			quantity = form.cleaned_data["quantity"]

			cart = request.session.get("cart", {})
			product_id = str(product_id)
			cart[product_id] = cart.get(product_id, 0) + quantity
			request.session["cart"] = cart
			return redirect("product_list")
	else:
		return HttpResponse("Invalid request method.", status=400)
	
def view_cart(request):
	cart = request.session.get("cart", {})
	products = Product.objects.filter(pk__in=cart.keys())

	cart_items = []
	total_price = 0

	for product in products:
		quantity = cart.get(str(product.pk), 0)
		item_total = product.price * quantity

		cart_items.append({
			"product": product,
			"quantity": quantity,
			"item_total": item_total,
		})

		total_price += item_total

	return render(request, "cart/view_cart.html", {
		"cart_items": cart_items,
		"total_price": total_price
	})
