import json

from apitherapy import api

access_token = "e099a9202a59936ca59629887464796af76c5359e9a33ce5938b1aad3e97bf10"

user_data = {
    'name': 'Joel Blows',
    'email': 'joe.blows@example.com',
    'gender': 'male',
    'status': 'active'
}

user_id = 0


def test_list_users():
    result = api.Api("https://gorest.co.in/public/v1", params=['name']) \
        .add_param('name', user_data['name']) \
        .query("/users")
    assert result.status_code == 200
    assert len(result.json()) > 0


def test_add_user():
    global user_id
    result = api.Api("https://gorest.co.in/public/v1") \
        .set_post_data(user_data) \
        .add_header("Authorization", "Bearer " + access_token) \
        .post_json('/users')
    data = result.json()['data']
    assert result.status_code == 201
    for key in user_data:
        assert data[key] == user_data[key]
    user_id = data['id']


def test_update_user():
    global user_id
    result = api.Api("https://gorest.co.in/public/v1", params=['name']) \
        .add_param('name', user_data['name']) \
        .query("/users")
    data = result.json()['data'][0]
    assert data['id'] == user_id
    updated_data = user_data.copy()
    updated_data['status'] = 'inactive'
    result = api.Api("https://gorest.co.in/public/v1") \
        .set_post_data(updated_data) \
        .add_header("Authorization", "Bearer " + access_token) \
        .put('/users' + '/' + str(user_id))
    assert result.status_code == 200


def test_delete_user():
    global user_id
    result = api.Api("https://gorest.co.in/public/v1", params=['name', 'email']) \
        .add_param("name", user_data['name']) \
        .add_header("Authorization", "Bearer " + access_token) \
        .query('/users').json()['data'][0]
    read_user_id = result['id']
    assert read_user_id == user_id
    result = api.Api("https://gorest.co.in/public/v1") \
        .add_header("Authorization", "Bearer " + access_token) \
        .delete('/users' + '/' + str(user_id))
    assert result.status_code == 204
