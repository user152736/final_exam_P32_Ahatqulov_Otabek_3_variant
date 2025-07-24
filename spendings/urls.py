from django.urls import path
from .views import home, create, view, update, delete

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('<int:card_id>view/', view, name='view'),
    path('<int:card_id>update/', update , name='update'),
    path('<int:card_id>delete/', delete , name='delete'),
]