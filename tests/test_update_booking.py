import allure
import jsonschema
from allure_commons._allure import step
from allure_commons.types import Severity

from restful_booker_api_diploma.utils import load_schema
from tests.conftest import booking_api
from restful_booker_api_diploma.data import update_booking


@allure.feature('Update Booking')
@allure.title('Update Booking: Status code is 200')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_update_booking_status_code_is_200(authenticate_user, create_booking):
    booking_id = create_booking
    auth = authenticate_user
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={auth}',
    }

    response = booking_api(
        url=f'/booking/{booking_id}',
        method='put',
        data=update_booking,
        headers=headers,
    )

    with step('Status code is 200'):
        assert (
            response.status_code == 200
        ), f"Status code {response.status_code} is incorrect"


@allure.feature('Update Booking')
@allure.title('Update Booking: Response schema is valid')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_update_booking_response_schema_is_valid(authenticate_user, create_booking):
    schema = load_schema('update_booking.json')
    booking_id = create_booking
    auth = authenticate_user
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={auth}',
    }

    response = booking_api(
        url=f'/booking/{booking_id}',
        method='put',
        data=update_booking,
        headers=headers,
    )

    with step('Response schema is valid'):
        jsonschema.validate(response.json(), schema)


@allure.feature('Update Booking')
@allure.title('Update Booking: Response data is valid')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_update_booking_reponse_data_is_valid(authenticate_user, create_booking):
    booking_id = create_booking
    auth = authenticate_user
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={auth}',
    }

    response = booking_api(
        url=f'/booking/{booking_id}',
        method='put',
        data=update_booking,
        headers=headers,
    )

    with step('Assert data is valid'):
        assert response.json()['firstname'] == 'James'
        assert response.json()['lastname'] == 'Smith'
        assert response.json()['totalprice'] == 200
        assert response.json()['depositpaid'] is False
        assert response.json()['bookingdates'] == {
            "checkin": "2018-01-02",
            "checkout": "2019-01-03",
        }
        assert response.json()['additionalneeds'] == 'Dinner'
