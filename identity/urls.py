# identity/urls.py
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = "identity"

urlpatterns = [
    # التسجيل والدخول
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # تسجيل الدخول برقم الجوال
    path("phone/", views.phone_login_request, name="phone_request"),
    path("phone/verify/", views.phone_login_verify, name="phone_verify"),

    # إعادة تعيين كلمة المرور
    path("password/reset/", auth_views.PasswordResetView.as_view(
        template_name="identityt/password_reset.html",
        email_template_name="identityt/password_reset_email.html",
        success_url=reverse_lazy("identity:password_reset_done")   # ✅ هنا التعديل
    ), name="password_reset"),

    path("password/reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="identityt/password_reset_done.html"
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="identityt/password_reset_confirm.html",
        success_url=reverse_lazy("identity:password_reset_complete")  # ✅ هنا كمان
    ), name="password_reset_confirm"),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="identityt/password_reset_complete.html"
    ), name="password_reset_complete"),
]
