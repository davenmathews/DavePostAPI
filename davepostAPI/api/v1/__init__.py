from flask import Blueprint
from flask_restplus import Api

from davepostAPI.api.v1.auth import auth_ns
from davepostAPI.api.v1.posts import posts_ns
from davepostAPI.api.v1.users import users_ns

# initiate blueprint
api_v1_blueprint = Blueprint('apiV1', __name__, url_prefix='/api/v1')

# initiate api
api_v1 = Api(api_v1_blueprint)

# api configurations
api_v1.catch_all_404s = True

# register namespaces related to this api
api_v1.add_namespace(auth_ns)
api_v1.add_namespace(posts_ns)
api_v1.add_namespace(users_ns)

# register extensions
