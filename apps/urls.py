from django.conf.urls.static import static
from django.urls import path

from apps.views import UserListVeiw,UserUpdateView ,UserDeleteView

from root.settings import MEDIA_URL, MEDIA_ROOT
urlpatterns = [
                path('',UserListVeiw.as_view(), name='users'),
                path('update/<int:pk>', UserUpdateView.as_view(), name='update_user'),
                path('update/<int:pk>', UserDeleteView.as_view(), name='delete_user'),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT)



