from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path("" , views.Index , name ="Index"),
    path("products" , views.ProductView.as_view() , name="products"),
    path("<int:pk>" , views.DetailProductView.as_view() , name="detail")
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)