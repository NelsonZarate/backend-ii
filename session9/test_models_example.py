"""Session 9: illustrative pytest-django model test example."""
import pytest

# This is an illustrative example. It requires a Django settings/config to run.

@pytest.mark.skip(reason="Requires Django settings; example only")
def test_item_creation(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        from app.models import Item  # adjust to real model path
        item = Item.objects.create(name="Test", value=10)
        assert item.name == "Test"
        assert item.value == 10
