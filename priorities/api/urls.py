# from articles.api.views import ArticleViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ArticleViewSet, base_name='articles')
# urlpatterns = router.urls

from django.urls import path

from .views import (
    PriorityListView,
    PriorityDetailView,
    PriorityCreateView,
    PriorityUpdateView,
    PriorityDeleteView
)

urlpatterns = [
    path('', PriorityListView.as_view()),
    path('create/', PriorityCreateView.as_view()),
    path('<pk>', PriorityDetailView.as_view()),
    path('<pk>/update/', PriorityUpdateView.as_view()),
    path('<pk>/delete/', PriorityDeleteView.as_view())
]
