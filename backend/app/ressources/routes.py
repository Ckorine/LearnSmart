from backend.app.ressources.authentification import SignupApi, LoginApi, LogoutApi, ChangePasswordApi
from backend.app.ressources.quizz import QuizApi, SinglechoiceApi
from backend.app.ressources.topics import TopicsApi
from backend.app.ressources.user import UserApi, ChangeUserDataApi, ScoreApi, LastRecordApi
from backend.app.ressources.quizz import QuizByTopicApi
from backend.app.ressources.upload import UploadApi, ShowUploads


# define the function to initialize the routes
def initialize_routes(api):
    api.add_resource(TopicsApi, '/api/topics')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(QuizApi, '/api/quiz')
    api.add_resource(QuizByTopicApi, '/api/quizbytopic/<topic_name>')
    api.add_resource(LogoutApi, '/api/auth/logout')
    # api.add_resource(SinglechoiceApi, '/api/singlechoice')
    api.add_resource(SinglechoiceApi, '/api/singlechoice/<topic_name>')
    api.add_resource(UserApi, '/api/userData')
    api.add_resource(ChangePasswordApi, '/api/auth/changePassword')
    api.add_resource(ChangeUserDataApi, '/api/changeUserData')
    api.add_resource(ScoreApi, '/api/score')

    api.add_resource(UploadApi, '/api/upload')
    api.add_resource(ShowUploads, '/api/showUploads')

    api.add_resource(LastRecordApi, '/api/lastrecord')
