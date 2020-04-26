# from articles.api.views import ArticleViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ArticleViewSet, base_name='articles')
# urlpatterns = router.urls

from django.urls import path

from .views import (
    AgentListView,
    AgentDetailView,
    AgentCreateView,
    AgentUpdateView,
    AgentDeleteView
)

urlpatterns = [
    path('', AgentListView.as_view()),
    path('create/', AgentCreateView.as_view()),
    path('<pk>', AgentDetailView.as_view()),
    path('<pk>/update/', AgentUpdateView.as_view()),
    path('<pk>/delete/', AgentDeleteView.as_view())
]
