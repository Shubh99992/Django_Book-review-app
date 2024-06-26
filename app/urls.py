from django.urls import include, path
from django.views.generic import TemplateView
from app.views import SignUpView, HomeView, BookDetailView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", HomeView.as_view(), name="home"),  # new
    path("book/<int:pk>/", BookDetailView.as_view(), name="book_details"),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    
]