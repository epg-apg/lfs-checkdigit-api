import json


def test_number(client):
    response = client.get('/number/1234')

    expected_json = dict(input=1234, checkDigit=2)

    assert json.loads(response.data) == expected_json
