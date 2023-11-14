import json
import os

import allure
import pytest
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from curlify import to_curl
from dotenv import load_dotenv
from requests import sessions

from restful_booker_api_diploma.data import new_booking

load_dotenv()
auth_payload = {'username': os.getenv('username'), 'password': os.getenv('password')}
base_url = os.getenv('base_url')


def retrieve_request(full_url, method, **kwargs):
    with sessions.Session() as session:
        response = session.request(method=method, url=full_url, **kwargs)

        message = to_curl(response.request)
        allure.attach(
            body=message.encode('utf8'),
            name='Request cURL',
            attachment_type=AttachmentType.TEXT,
            extension='txt',
        )
        try:
            allure.attach(
                body=json.dumps(response.json(), indent=4).encode('utf8'),
                name='Response JSON',
                attachment_type=AttachmentType.JSON,
                extension='json',
            )
        except:
            allure.attach(
                body=response.content,
                name='Response',
                attachment_type=AttachmentType.TEXT,
                extension='txt',
            )

    return response


def booking_api(url, method, **kwargs):
    full_url = base_url + url

    with step(f'Send request {method.upper()} {full_url}'):
        response = retrieve_request(full_url, method, **kwargs)

    return response


@pytest.fixture(scope='function', autouse=False)
def authenticate_user():
    response = booking_api(url='/auth', method='post', data=auth_payload)

    return response.json()['token']


@pytest.fixture(scope='function', autouse=False)
def create_booking():
    headers = {
        'Content-Type': 'application/json',
    }

    response = booking_api(
        url='/booking', method='post', data=new_booking, headers=headers
    )

    return response.json()['bookingid']
