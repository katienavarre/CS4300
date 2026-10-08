from behave import given, when, then
import django
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "movie_theater_booking.settings"
)
django.setup()

from django.test import Client


@given("the movie listing page is available")
def step_page_available(context):
    context.client = Client()


@when("I request the movie listing page")
def step_request_page(context):
    context.response = context.client.get("/")


@then("the page should respond successfully")
def step_page_successful(context):
    assert context.response.status_code == 200, (
        f"Expected status 200, but got {context.response.status_code}"
    )
