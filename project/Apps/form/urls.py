from django.urls import path
from .views import SubscriberViews

urlpatterns = [
    path("view", SubscriberViews.form_view),
    path("list/sub", SubscriberViews.list_subscriber),
    path("save/sub", SubscriberViews.save_subscriber),
]
