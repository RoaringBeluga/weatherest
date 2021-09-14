from fixtures import *


def test_the_rest(data_by_city, city_info):
    """Test API response"""
    status, body = data_by_city
    assert body['name'] == city_info['name']


def test_coords(data_by_city, city_info):
    """Test returned coordinates"""
    status, body = data_by_city
    spam = body['coord']
    assert spam['lat'] == city_info['lat']
    assert spam['lon'] == city_info['lon']


def test_everything_ok(everything_but_the_kitchen_sink, city_info):
    status, body = everything_but_the_kitchen_sink
    assert status == 200


def test_everything_data(everything_but_the_kitchen_sink, city_info):
    status, body = everything_but_the_kitchen_sink
    assert body['lat'] == city_info['lat']
    assert body['lon'] == city_info['lon']