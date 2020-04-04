# from articles.api.views import ArticleViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ArticleViewSet, base_name='articles')
# urlpatterns = router.urls

from django.urls import path

from .views import (
    StateListView,
    StateDetailView,
    StateCreateView,
    StateUpdateView,
    StateDeleteView
)

urlpatterns = [
    path('', StateListView.as_view()),
    path('create/', StateCreateView.as_view()),
    path('<pk>', StateDetailView.as_view()),
    path('<pk>/update/', StateUpdateView.as_view()),
    path('<pk>/delete/', StateDeleteView.as_view())
]
