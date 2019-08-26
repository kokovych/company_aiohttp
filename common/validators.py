from db import get_user_by_email
from model import get_correct_fields


EMAIL_REQUIRED = 'email is required'
USERNAME_REQUIRED = 'username is required'
PASSWORD_REQUIRED = 'password is required'
NOT_UNIQUE_USER = 'not unique email'


async def validate_registration(conn, data):
    username = data['username']
    password = data['password']
    email = data['email']

    if not username:
        return USERNAME_REQUIRED
    if not email:
        return EMAIL_REQUIRED
    if not password:
        return PASSWORD_REQUIRED

    user = await get_user_by_email(conn, email)
    if user:
        return NOT_UNIQUE_USER


def clean_create_user_data(data):
    correct_fields = get_correct_fields()
    result = {}
    for attr_name in correct_fields:
        result[attr_name] = data.get(attr_name)
    return result
