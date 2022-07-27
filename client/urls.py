from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_request_view),
    path('logout', views.user_logout),
    path('profile/<str:username>', views.get_client_profile),
    path('create_account/', views.create_client_view),
    path("delete_account/<str:username>", views.delete_client_view)
]