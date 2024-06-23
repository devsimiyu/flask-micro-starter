from flask import Flask, request, jsonify
from flask_cors import CORS
from ariadne import (
    graphql_sync,
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
    QueryType,
    MutationType
)
from ariadne.explorer import ExplorerPlayground
from resolvers import (
    get_user_list_resolver,
    get_user_details_resolver,
    create_user_resolver,
    update_user_resolver,
    delete_user_resolver
)

graphql_query = QueryType()
graphql_mutation = MutationType()

graphql_query.set_field('getUserList', get_user_list_resolver)
graphql_query.set_field('getUserDetails', get_user_details_resolver)
graphql_mutation.set_field('createUser', create_user_resolver)
graphql_mutation.set_field('updateUser', update_user_resolver)
graphql_mutation.set_field('deleteUser', delete_user_resolver)

graphql_type_defs = load_schema_from_path('schema.graphql')
graphql_explorer = ExplorerPlayground().html(None)
graphql_schema = make_executable_schema(
    graphql_type_defs,
    graphql_query,
    graphql_mutation,
    snake_case_fallback_resolvers
)

app = Flask(__name__)

CORS(app)

@app.route('/health-check')
def health_check():
    return 'hello world!'

@app.route('/graphql', methods = ['GET'])
def graphql_playground():
    return graphql_explorer, 200

@app.route('/graphql', methods = ['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(graphql_schema, data, context_value = request, debug = app.debug)
    status_code = 200 if success else 400
    return jsonify(result), status_code
