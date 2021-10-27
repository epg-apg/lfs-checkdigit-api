import json


def test_number(client):
    response = client.get('/number/123')
    expected_json = dict(input=123, checkDigit=6)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/587156')
    expected_json = dict(input=587156, checkDigit=8)
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

    response = client.get('/number/4026845')
    expected_json = dict(input=4026845, checkDigit=3)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/7897890')
    expected_json = dict(input=7897890, checkDigit=4)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/7351353')
    expected_json = dict(input=7351353, checkDigit=7)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/978014102662')
    expected_json = dict(input=978014102662, checkDigit=6)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/400638133393')
    expected_json = dict(input=400638133393, checkDigit=1)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/1234567890128')
    expected_json = dict(input=1234567890128, checkDigit=6)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/9780521425575')
    expected_json = dict(input=9780521425575, checkDigit=0)
    assert json.loads(response.data) == expected_json

    response = client.get('/number/9781405322274')
    expected_json = dict(input=9781405322274, checkDigit=8)
    assert json.loads(response.data) == expected_json
