from django.urls import path

from . import views

urlpatterns = [
    path("", views.product_list, name="index"),
	path("products/", views.product_list, name="product_list"),
	path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
	path("view/", views.view_cart, name="view_cart"),
]