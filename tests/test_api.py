import json

from common.api import ERROR_RESPONSE, CORRECT_RESPONSE, USER_CREATED
from common.validators import (EMAIL_REQUIRED, USERNAME_REQUIRED, PASSWORD_REQUIRED,
                               NOT_UNIQUE_USER)

TEST_USER_DATA = {
    'username': 'test_user_1',
    'email': 'mail01@mail.com',
    'password': 'password123'
}


async def test_set_value(cli):
    resp = await cli.get('/')
    assert resp.status == 200


async def test_create_user_empty_request(cli):
    resp = await cli.post('/api/user/')
    data = await resp.json()
    assert resp.status == 400
    assert data == ERROR_RESPONSE


async def test_create_user_success(setup_test_db, cli):
    user_data = json.dumps(TEST_USER_DATA)
    resp = await cli.post('/api/user/', data=user_data)
    resp_data = await resp.json()
    assert resp.status == 201
    CORRECT_RESPONSE['data'] = USER_CREATED
    assert resp_data == CORRECT_RESPONSE


async def test_create_user_miss_required_field(cli):
    test_user_data_1 = {
        'username': 'test_user_1',
        'password': 'password123'
    }
    test_user_data_2 = {
        'username': 'test_user_1',
        'email': 'mail011@mail.com',
    }
    test_user_data_3 = {
        'password': 'test_user_1',
        'email': 'mail011@mail.com',
    }
    user_data_1 = json.dumps(test_user_data_1)
    user_data_2 = json.dumps(test_user_data_2)
    user_data_3 = json.dumps(test_user_data_3)
    resp_1 = await cli.post('/api/user/', data=user_data_1)
    resp_2 = await cli.post('/api/user/', data=user_data_2)
    resp_3 = await cli.post('/api/user/', data=user_data_3)
    resp_data_1 = await resp_1.json()
    resp_data_2 = await resp_2.json()
    resp_data_3 = await resp_3.json()
    assert resp_1.status == 400
    assert resp_data_1 == {'error': EMAIL_REQUIRED}
    assert resp_2.status == 400
    assert resp_data_2 == {'error': PASSWORD_REQUIRED}
    assert resp_3.status == 400
    assert resp_data_3 == {'error': USERNAME_REQUIRED}


async def test_create_user_not_unique_email(setup_test_db, cli):
    user_data = json.dumps(TEST_USER_DATA)
    resp = await cli.post('/api/user/', data=user_data)
    resp_data = await resp.json()
    assert resp.status == 400
    assert resp_data == {'error': NOT_UNIQUE_USER}


async def test_drop_test_database(drop_test_db):
    print('All tables from test DB were dropped!')
