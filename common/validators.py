from db import get_user_by_email
from model import get_correct_fields


async def validate_registration(conn, data):
    username = data['username']
    password = data['password']
    email = data['email']

    if not username:
        return 'username is required'
    if not password:
        return 'password is required'
    if not email:
        return 'email is required'

    user = await get_user_by_email(conn, email)
    if user:
        return 'not unique email'


def clean_create_user_data(data):
    correct_fields = get_correct_fields()
    result = {}
    for attr_name in correct_fields:
        result[attr_name] = data.get(attr_name)
    return result
