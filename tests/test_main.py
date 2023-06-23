from main import get_weather
import requests
import pytest


class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data


@pytest.mark.parametrize(
    'city, json_data, status_code, expected_result',
    [
        ('Moscow', {'main': {'temp': 20}}, 200,
         {'city': 'Moscow', 'temperature': 20}),
        ('FakeCity', {'message': 'city not found'}, 404,
         {'city': 'city not found', 'temperature': 'city not found'})
    ],
    ids=[
        'returns_temperature',
        'city not found'
        ]
)
def test__get_weather(city, json_data, status_code, expected_result):
    response = MockResponse(status_code, json_data)
    requests.get = lambda url: response

    result = get_weather(city)

    assert result == expected_result
