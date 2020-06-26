from flask import Response
from LearnSmart.backend.database.models.Topic import Topic
from flask_restful import Resource


# This creates an endpoint which accepts GET request.
class TopicsApi(Resource):
    def get(self):
        topics = Topic.objects().to_json()
        return Response(topics, mimetype="application/json", status=200)
