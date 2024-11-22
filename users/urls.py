from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
        path('', views.index, name='index'),
        path('signup/', views.signup, name='signup'),
        path('buyer/dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
        path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),
        # path('login/', views.login, name='login'),
        # path('dashboard/', views.dashboard, name="dashboard"),
        # path('edit-profile/', views.edit_profile, name="edit_profile"),
        # path('upload-profile-picture/', views.upload_profile_picture, name='upload_profile_picture'),
        # path('change-email/', views.change_email, name='change_email'),
        # path('change-password/', views.change_password, name='change_password'),
        # path('delete-account/', views.delete_account, name='delete_account'),
        # path('logout/', views.logout, name='logout'),
]