# from articles.api.views import ArticleViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ArticleViewSet, base_name='articles')
# urlpatterns = router.urls

from django.urls import path

from .views import (
    BTypeListView,
    BTypeDetailView,
    BTypeCreateView,
    BTypeUpdateView,
    BTypeDeleteView
)

urlpatterns = [
    path('', BTypeListView.as_view()),
    path('create/', BTypeCreateView.as_view()),
    path('<pk>', BTypeDetailView.as_view()),
    path('<pk>/update/', BTypeUpdateView.as_view()),
    path('<pk>/delete/', BTypeDeleteView.as_view())
]
