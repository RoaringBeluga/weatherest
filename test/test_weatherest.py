from fixtures import *


def test_the_rest(data_by_city, city_info):
    """Test API response"""
    assert data_by_city['name'] == city_info['name']


def test_coords(data_by_city, city_info):
    """Test returned coordinates"""
    spam = data_by_city['coord']
    assert spam['lat'] == city_info['lat']
    assert spam['lon'] == city_info['lon']

#
#
# def test_get_request():
#     bee = request_data()
#     assert bee.status_code == 200, f"Something's wromg! Status code is: [{bee.status_code}], expected: [200]"
#
#
# def test_response_city():
#     bee = request_data()
#     assert bee.json()['name'] == 'Mountain View', f"Wrong city name {bee.json()['name']}"
