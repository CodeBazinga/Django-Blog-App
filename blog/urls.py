from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name="create"),
    path('delete/<id>/', views.deletelist,name="delete"),
    path('update/<id>', views.updatelist,name="update"),
    # path('register/',views.registerPage,name="register"),
    path('allblogs/',views.displayBlog,name="display"),
    # path('login/',views.loginPage,name="login"),
    # path('logout/', views.logoutUser, name="logout"),

]
