# from articles.api.views import ArticleViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ArticleViewSet, base_name='articles')
# urlpatterns = router.urls

from django.urls import path

from .views import (
    BulletinListView,
    BulletinDetailView,
    BulletinCreateView,
    BulletinUpdateView,
    BulletinDeleteView,
    BulletinSendView
)

urlpatterns = [
    path('', BulletinListView.as_view()),
    path('create/', BulletinCreateView.as_view()),
    path('<pk>', BulletinDetailView.as_view()),
    path('<pk>/update/', BulletinUpdateView.as_view()),
    path('<pk>/delete/', BulletinDeleteView.as_view()),

    path('<pk>/send/', BulletinSendView.as_view())
]
