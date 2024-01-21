from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from registration import views

from django.views.generic import TemplateView

index_view = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login_required(index_view), name="index"),
    # ・ログイン
    # ・ログアウト
    # ・パスワード変更
    # ・パスワード再発行
    path('', include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
]

handler500 = views.my_customized_server_error