from django.test import Client
from main_app.tests.utils import *

client = Client()

# HOMEPAGE / DASHBOARD VIEWS:

def test_view_homepage_get():
    response = client.get("/")
    assert response.status_code == 200


def test_view_dashboard_get():
    response = client.get("/dashboard/")
    assert response.status_code == 302


def test_view_dashboard_post():
    response = client.post("/dashboard/")
    assert response.status_code == 302


# USER VIEWS:

def test_view_login_get():
    response = client.get("/login/")
    assert response.status_code == 200


def test_view_login_post():
    response = client.post("/login/")
    assert response.status_code == 200


def test_view_register_get():
    response = client.get("/register/")
    assert response.status_code == 200


def test_view_register_post():
    response = client.post("/register/")
    assert response.status_code == 200


def test_view_logout_get():
    response = client.get("/logout/")
    assert response.status_code == 302


def test_view_logout_post():
    response = client.post("/logout/")
    assert response.status_code == 302


def test_view_password_change_get():
    response = client.get("/password_change/")
    assert response.status_code == 302


def test_view_password_change_post():
    response = client.post("/password_change/")
    assert response.status_code == 302


def test_view_password_change_done_get():
    response = client.get("/password_change/done/")
    assert response.status_code == 302


def test_view_password_change_done_post():
    response = client.post("/password_change/done/")
    assert response.status_code == 302


def test_view_password_reset_get():
    response = client.get("/password_reset/")
    assert response.status_code == 200


def test_view_user_panel_get():
    response = client.get("/userpanel/")
    assert response.status_code == 302


def test_view_user_panel_post():
    response = client.post("/userpanel/")
    assert response.status_code == 302
