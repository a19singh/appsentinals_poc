from django.urls import path
from . import views

urlpatterns = [
    path(
        'fetch_user',
        views.PlatformUserListView.as_view({
            'get': 'list'
        })
    ),
    path(
        'create_user',
        views.PlatformUserView.as_view({
            'post': 'create'
        })
    ),
    path(
        'fetch_user/<int:pk>',
        views.PlatformUserView.as_view({
            'get': 'retrieve'
        })
    )
]
