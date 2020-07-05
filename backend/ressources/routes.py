from backend.ressources.authentification import SignupApi, LoginApi, LogoutApi
from backend.ressources.quizz import QuizApi, SinglechoiceApi
from backend.ressources.topics import TopicsApi
from backend.ressources.quizz import QuizByTopicApi


# define the function to initialize the routes
def initialize_routes(api):
    api.add_resource(TopicsApi, '/api/topics')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(QuizApi, '/api/quiz')
    api.add_resource(QuizByTopicApi, '/api/quizbytopic/<topic_name>')
    api.add_resource(LogoutApi, '/api/auth/logout')
    #api.add_resource(SinglechoiceApi, '/api/singlechoice')
    api.add_resource(SinglechoiceApi, '/api/singlechoice/<topic_name>')
