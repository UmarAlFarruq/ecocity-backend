from django.urls import path
from . views import *

urlpatterns = [

    path('',IndexView.as_view()),
    path('login',LoginView.as_view()),
    path('sign-up',SignUpView.as_view()),
    path("addpost",AddPostView.as_view()),
    path("profile",ProfileReadView.as_view()),
    path("profiledit",ProfileEditView.as_view())
]