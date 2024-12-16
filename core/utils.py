"""
External Library: python-barcode
Source: https://python-barcode.readthedocs.io/en/stable/
"""

from random import choice
from string import digits, ascii_letters
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.http import HttpRequest
from django.conf import settings
from core.services import add_login_code, update_login_code
from django.conf import settings

SENDER = settings.DEFAULT_FROM_EMAIL
SENDER_EMAIL = "dev.freddoe@gmail.com"
SENDER_NAME = "Sterioms - Sterilization Information Management System"
DIGITS = "1234567890"
LETTERS_DIGITS = ascii_letters + digits


def generate_token():
    return "".join([choice(LETTERS_DIGITS) for i in range(25)])


def absolute_media_url(request: HttpRequest, media_url: str):
    return request.build_absolute_uri(media_url)


def generate_code(length: int):
    return "".join([choice(DIGITS) for i in range(length)])


# Initialize Brevo API client
def initialize_brevo_client():
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key["api-key"] = settings.BREVO_API_KEY
    return sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )


# Function to send an email
def send_login_code_brevo(receiver, old_code=None, length: int = 6):
    api_instance = initialize_brevo_client()

    subject = "Sterioms Account Sign In Code"
    code = generate_code(length)
    message = f"""
    Hello {receiver.name},


    Use this code to sign into your account:

                {code}

    The code expires in 20 minutes.


    _______________________________________________

    Sterilization Information Management System
    Sterioms
    _______________________________________________
    """

    # Prepare the email content
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": receiver.email}],
        sender={"email": SENDER_EMAIL, "name": SENDER_NAME},
        subject=subject,
        text_content=message,
    )

    try:
        # Send the email
        response = api_instance.send_transac_email(send_smtp_email)
    except ApiException as e:
        return None
    else:
        if old_code:
            update_login_code({"code": code}, instance=old_code)
        else:
            add_login_code({"employee": receiver.pk, "code": code})
        return response
