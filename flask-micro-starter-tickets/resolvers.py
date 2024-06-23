from ariadne import convert_kwargs_to_snake_case

def get_tickets_list_resolver(obj, info):
    return [{ 'id': '1234er', 'title': 'Hello ticket' }]

@convert_kwargs_to_snake_case
def get_tickets_details_resolver(obj, info, id):
    return { 'id': '1234er', 'title': 'Hello ticket' }

@convert_kwargs_to_snake_case
def create_ticket_resolver(obj, info, title, description):
    return { 'id': '1234er', 'title': title, 'description': description }

@convert_kwargs_to_snake_case
def update_ticket_resolver(obj, info, id, title, description):
    return { 'id': id, 'title': title, 'description': description }

@convert_kwargs_to_snake_case
def delete_ticket_resolver(obj, info, id):
    return f'Ticket {id} will deleted'
