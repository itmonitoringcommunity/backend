# from articles.api.views import ArticleViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ArticleViewSet, base_name='articles')
# urlpatterns = router.urls

from django.urls import path

from .views import (
    MailListView,
    MailDetailView,
    MailCreateView,
    MailUpdateView,
    MailDeleteView
)

urlpatterns = [
    path('', MailListView.as_view()),
    path('create/', MailCreateView.as_view()),
    path('<pk>', MailDetailView.as_view()),
    path('<pk>/update/', MailUpdateView.as_view()),
    path('<pk>/delete/', MailDeleteView.as_view())
]
