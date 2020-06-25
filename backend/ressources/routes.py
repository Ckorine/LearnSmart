from backend.ressources.authentification import SignupApi, LoginApi
from backend.ressources.topics import TopicsApi


# define the function to initialize the routes
def initialize_routes(api):
    api.add_resource(TopicsApi, '/api/topics')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')