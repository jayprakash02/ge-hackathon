from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/',include("main.urls")),
]

test=[
path('test/',TemplateView.as_view(template_name='test.html'),name="test"),
]

urlpatterns+=test