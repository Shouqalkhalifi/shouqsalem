from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import AccountCreationForm, AccountAuthenticationForm
from django.contrib.auth import logout

# دالة انشاء الحساب 
def register_view(request):
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "تم إنشاء الحساب بنجاح ✅")
            return redirect("identity:login")
    else:
        form = AccountCreationForm()
    return render(request, "identityt/register.html", {"form": form})


# دالة تسجيل الدخول 
def login_view(request):
    if request.method == "POST":
        form = AccountAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"مرحباً {user.username} 👋")
            return redirect("/")  # يمكن تغييره لصفحة رئيسية
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة ❌")
    else:
        form = AccountAuthenticationForm()
    return render(request, "identityt/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")  # يرجع المستخدم للصفحة الرئيسية بعد تسجيل الخروج
