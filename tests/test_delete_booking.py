import allure
from allure_commons._allure import step
from allure_commons.types import Severity

from tests.conftest import booking_api


@allure.title('Delete Booking: Status code is 201')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_delete_booking_with_valid_id(authenticate_user, create_booking):
    auth = authenticate_user
    booking_id = create_booking
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={auth}',
    }

    response = booking_api(
        url=f'/booking/{booking_id}',
        method='delete',
        headers=headers,
    )

    with step('Status code is 201'):
        assert (
            response.status_code == 201
        ), f"Status code {response.status_code} is incorrect"


@allure.title('Delete Booking: Status code is 405')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_delete_booking_with_invalid_id(authenticate_user):
    auth = authenticate_user
    booking_id = 'test'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={auth}',
    }

    response = booking_api(
        url=f'/booking/{booking_id}',
        method='delete',
        headers=headers,
    )

    with step('Status code is 405'):
        assert (
            response.status_code == 405
        ), f"Status code {response.status_code} is incorrect"
