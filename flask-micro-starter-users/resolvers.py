from ariadne import convert_kwargs_to_snake_case

def get_user_list_resolver(obj, info):
    return [
        {
            'id': '1234er',
            'first_name': 'new user first name',
            'last_name': 'new user last name',
            'email': 'mail@example.org',
            'role': 'ADMIN'
        }
    ]

@convert_kwargs_to_snake_case
def get_user_details_resolver(obj, info, id):
    return {
        'id': id,
        'email': 'new@mail.com',
        'first_name': 'new user first name',
        'last_name': 'new user last name',
        'role': 'ADMIN'
    }

@convert_kwargs_to_snake_case
def create_user_resolver(obj, info, email, first_name, last_name, role):
    return {
        'id': '1234er',
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'role': role
    }

@convert_kwargs_to_snake_case
def update_user_resolver(obj, info, id, email, first_name, last_name, role):
    return {
        'id': id,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'role': role
    }

@convert_kwargs_to_snake_case
def delete_user_resolver(obj, info, id):
    return f'User {id} will be deleted'
