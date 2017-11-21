from django.conf.urls import url, include
import views as vi

vista = vi.views()

urlpatterns = [
    url(r'^$', vista.home),
]