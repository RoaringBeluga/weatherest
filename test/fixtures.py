from _pytest.fixtures import fixture
from weatherest.Api import Weatherest

@fixture
def city_info():
    # We should put the code that fetches test data here
    # Maybe get those from YAML file, or a database, or...
    return {
               'name': 'Mountain View',
               'region': 'CA',
                'country': 'US',
                'lat': 37.3861,
                'lon': -122.0838
    }


@fixture
def data_by_city(city_info):
    eggs = Weatherest('3366b579242d65b6b3dff0ce0e155d8b')
    result = eggs.current_weather_city(city_info['name'], region=city_info['region'], country=city_info['country']).json()
    yield result
    print('Finished the test')
    result = None
    return None
