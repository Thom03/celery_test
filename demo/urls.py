from django.conf.urls import url
from . import views

app_name = 'demo'

urlpatterns = [
	url(r'^index/$', views.index, name="index"),
	url(r'^test_page/$', views.test_page, name="test_page"),
	# url(r'^quick_test/$', views.quick_test, name="quick_test"),
	url(r'^start_test/$', views.start_test, name="start_test"),
]