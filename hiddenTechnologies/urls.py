from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

]
urlpatterns += [
    path('', RedirectView.as_view(url='/admin/', permanent=True)),
]

