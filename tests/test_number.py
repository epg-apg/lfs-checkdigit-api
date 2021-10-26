import json


def test_number(client):
    response = client.get('/number/123')
    expected_json = dict(input=123, checkDigit=6)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/000000587156')
    expected_json = dict(input=587156, checkDigit=8)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/1234')
    expected_json = dict(input=1234, checkDigit=8)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/587313')
    expected_json = dict(input=587313, checkDigit=5)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/7897890')
    expected_json = dict(input=7897890, checkDigit=4)
    assert json.loads(response.data) == expected_json