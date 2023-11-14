import allure
import jsonschema
from allure_commons._allure import step
from allure_commons.types import Severity

from restful_booker_api_diploma.utils import load_schema
from tests.conftest import booking_api
from restful_booker_api_diploma.data import new_booking


@allure.title('Create Booking: Status code is 200')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_create_booking_status_code_200():
    headers = {
        'Content-Type': 'application/json',
    }

    response = booking_api(
        url='/booking', method='post', data=new_booking, headers=headers
    )

    with step('Status code is 200'):
        assert (
            response.status_code == 200
        ), f"Status code {response.status_code} is incorrect"


@allure.title('Create Booking: Response schema is valid')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_create_booking_response_schema_is_valid():
    schema = load_schema('create_booking.json')
    headers = {
        'Content-Type': 'application/json',
    }

    response = booking_api(
        url='/booking', method='post', data=new_booking, headers=headers
    )

    with step('Response schema is valid'):
        jsonschema.validate(response.json(), schema)


@allure.title('Create Booking: Response data is valid')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_create_booking_response_data_is_valid():
    headers = {
        'Content-Type': 'application/json',
    }

    response = booking_api(
        url='/booking', method='post', data=new_booking, headers=headers
    )

    with step('Assert data is valid'):
        assert response.json()['booking']['firstname'] == 'Jim'
        assert response.json()['booking']['lastname'] == 'Brown'
        assert response.json()['booking']['totalprice'] == 111
        assert response.json()['booking']['depositpaid'] is True
        assert response.json()['booking']['bookingdates'] == {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01",
        }
        assert response.json()['booking']['additionalneeds'] == 'Breakfast'
