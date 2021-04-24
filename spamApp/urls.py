from django.urls import path

from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('spam/', spam, name='spam'),
    path('spam_create/',spam_create, name='spam_create')
]