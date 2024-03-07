"""ICAR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.log),
    path('login_post',views.login_post),
    path('admin_home',views.admin_home),
    path('add_fuel',views.add_fuel),
    path('add_fuel_post',views.add_fuel_post),
    path('view_fuel',views.view_fuel),
    path('fuel_update/<id>',views.fuel_update),
    path('fuel_update_post/<id>',views.fuel_update_post),
    path('fuel_delete/<id>',views.fuel_delete),
    path('view_complaint',views.view_complaint),
    path('send_reply/<id>',views.send_reply),
    path('send_reply_post/<id>',views.send_reply_post),
    path('view_feedback',views.view_feedback),
    path('view_user',views.view_user),
    path('block_user/<id>',views.block_user),
    path('unblock_user/<id>',views.unblock_user),
    path('view_company',views.view_company),
    path('approve_company/<id>', views.approve_company),
    path('reject_company/<id>', views.reject_company),
    path('view_approved_company',views.view_approved_company),

    path('user_req',views.user_req),
    path('view_transaction_status/<id>',views.view_transaction_status),
    path('logout',views.logout),


#................................................................................. COMPANY MODULE
    path('company_home',views.company_home),
    path('company_register',views.company_register),
    path('company_register_post',views.company_register_post),
    path('view_profile',views.view_profile),
    path('add_user',views.add_user),
    path('add_user_post',views.add_user_post),
    path('view_users',views.view_users),
    path('update_user/<id>',views.update_user),
    path('update_user_post/<id>',views.update_user_post),
    path('delete_user/<id>',views.delete_user),
    path('change_password',views.change_password),
    path('change_password_post',views.change_password_post),

#..................................................................................USER MODULE
    path('android_login',views.android_login),
    path('android_view_profile',views.android_view_profile),
    path('android_send_feedback',views.android_send_feedback),
    path('android_view_route',views.android_view_route),
    path('android_add_route',views.android_add_route),
    path('android_update_route',views.android_update_route),
    path('android_update_routes',views.android_update_routes),
    path('android_delete_route',views.android_delete_route),
    path('android_view_user_request',views.android_view_user_request),
    path('android_accept_request',views.android_accept_request),
    path('android_reject_request',views.android_reject_request),
    path('android_view_reply',views.android_view_reply),
    path('android_send_complaint',views.android_send_complaint),
    path('android_view_uploaded_request',views.android_view_uploaded_request),
    path('android_view_request_status',views.android_view_request_status),
    path('android_send_request',views.android_send_request),
    path('android_offline_payment',views.android_offline_payment),
    path('android_online_payment',views.android_online_payment),

]
