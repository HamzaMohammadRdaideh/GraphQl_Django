from django.urls import path
from django.urls.conf import include
from graphene_django.views import GraphQLView

urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True)),
]