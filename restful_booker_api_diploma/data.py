import json

sort_by_name = {'firstname': 'Jim', 'lastname': 'Brown'}
new_booking = json.dumps(
    {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
        "additionalneeds": "Breakfast",
    }
)
update_booking = json.dumps(
    {
        "firstname": "James",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {"checkin": "2018-01-02", "checkout": "2019-01-03"},
        "additionalneeds": "Dinner",
    }
)
