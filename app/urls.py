from django.urls import include, path
from app.views import CommunityView, ExploreBooksView, SignUpView, HomeView, BookDetailView, UserProfileView, follow_user, unfollow_user, FollowingView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", HomeView.as_view(), name="home"),  # new
    path("book/<int:pk>/", BookDetailView.as_view(), name="book_details"),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    path("explore/", ExploreBooksView.as_view(), name='explore_books'),
    path("friends/<str:username>/", FollowingView.as_view(),name='friends' ),
    
    path('profile/<str:username>/', UserProfileView.as_view(), name='user_profile'),
    path('follow/<str:username>/', follow_user, name='follow_user'),
    path('unfollow/<str:username>/', unfollow_user, name='unfollow_user'),
    path('community/', CommunityView.as_view(), name='community'),
    
    
    
]