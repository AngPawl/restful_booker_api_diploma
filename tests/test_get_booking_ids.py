import allure
import jsonschema
from allure_commons._allure import step
from allure_commons.types import Severity

from restful_booker_api_diploma.utils import load_schema
from tests.conftest import booking_api
from restful_booker_api_diploma.data import sort_by_name


@allure.title('Get Booking IDs by name: Status code is 200')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_get_booking_ids_by_name_status_code_is_200():
    response = booking_api(url='/booking', method='get', params=sort_by_name)

    with step('Status code is 200'):
        assert (
            response.status_code == 200
        ), f"Status code {response.status_code} is incorrect"


@allure.title('Get Booking IDs by name: Response schema is valid')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_get_booking_ids_by_name_response_schema_is_valid():
    schema = load_schema('get_booking_ids.json')

    response = booking_api(url='/booking', method='get', params=sort_by_name)

    with step('Response schema is valid'):
        jsonschema.validate(response.json(), schema)
