from django.urls import path
from .views import Home, About, MotoCreate, MotoDetail, MotoDelete, RecordCreate, RecordDelete, RecordPartAssoc, RecordUpdate, PartsList, MotoStatusUpdate, TechCreate

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('motorcycles/', MotoCreate.as_view(), name='moto_show'),
    path('motorcycle/<int:pk>/', MotoDetail.as_view(), name='moto_detail'),
    path('motorcycle/<int:pk>/delete/', MotoDelete.as_view(), name='moto_delete'),
    path('motorcycle/<int:pk>/<int:user_pk>/', RecordCreate.as_view(), name='record_create'),
    path('motorcycle/record/<int:pk>/delete/', RecordDelete.as_view(), name='record_delete'),
    path('record/<int:pk>/update/', RecordUpdate.as_view(), name='record_update'),
    path('parts/', PartsList.as_view(), name='parts_list'),
    path('record/<int:pk>/part/<int:part_pk>/', RecordPartAssoc.as_view(), name='record_part_assoc'),
    path('record/<int:pk>/status/<int:st>', MotoStatusUpdate.as_view(), name='moto_status'),
    path('technician/new/', TechCreate.as_view(), name='tech_create'),
    path('accounts/signup/', Home.as_view(), name='signup')
]