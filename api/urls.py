from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    UserCreateView,
    UserDetailView,
    AnimeListView,
    BookmarkListView,
    BookmarkDetailView,
    WatchHistoryListView,
    ReviewListView,
    ReviewDetailView,
)

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", UserCreateView.as_view(), name="user_create"),
    path("profile/", UserDetailView.as_view(), name="user_detail"),
    path("anime/", AnimeListView.as_view(), name="anime_list"),
    path("bookmarks/", BookmarkListView.as_view(), name="bookmark_list"),
    path(
        "bookmarks/<str:anime_id>/detail/",
        BookmarkDetailView.as_view(),
        name="bookmark_detail_by_id",
    ),
    path("bookmarks/<int:pk>/", BookmarkDetailView.as_view(), name="bookmark_detail"),
    path("history/", WatchHistoryListView.as_view(), name="watch_history_list"),
    path("reviews/", ReviewListView.as_view(), name="review_list"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review_detail"),
]
