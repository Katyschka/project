from django.urls import path
from .import views

#  Здесь мы импортировали views и прописали путь наших представлений которые создали в файле views
urlpatterns=[
    path('', views.ArtListView.as_view(), name='home'),
    path('art/<int:pk>', views.ArtDetailView.as_view(), name='detail'),
]