from django.urls import path

from basicapp import views

app_name = 'basicapp'

urlpatterns = [

    path('',views.SchoolList.as_view(), name="list"),
    path('<int:pk>/',views.SchoolDetails.as_view(), name="detail"),
    path('create/',views.CreateSchoolView.as_view(), name="create"),
    path('update/<int:pk>',views.SchoolUpdateView.as_view(), name="update"),
    path('delete/<int:pk>',views.SchoolDeleteView.as_view(), name="delete"),

]
