from django.conf.urls import url, include
from django.contrib import admin
from webapp import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
schema_view = get_swagger_view(title='Roman Rest Project API')

urlpatterns = [
    url(r'^rest/admin/', admin.site.urls),
    url(r'^rest/registration/$', views.CreateUserView.as_view()),
    url(r'^rest/rest-auth/', include('rest_auth.urls')),
    url(r'^rest/send_request/', views.SendRequest.as_view()),
    url(r'^rest/access/(?P<pk>[0-9]+)/$', views.AccessDetail.as_view()),
    url(r'^rest/all_requests/', views.AllRequests.as_view()),
    url(r'^rest/auth/', views.AuthView.as_view(), name='auth-view'),
    url(r'^rest/docs/', schema_view)
]
urlpatterns = format_suffix_patterns(urlpatterns)