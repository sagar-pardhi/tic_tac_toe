from django.urls import path
from game.views import game, index

urlpatterns = [
    ## other url routes
    path('', index),
    path('play/<room_code>', game),
]