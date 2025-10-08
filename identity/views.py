from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import AccountCreationForm, AccountAuthenticationForm
from django.contrib.auth import logout
from django.conf import settings
from .models import Account
import random
from django.contrib.sites.shortcuts import get_current_site
try:
    from allauth.socialaccount.models import SocialApp
except Exception:  # allauth may not be installed in some envs
    SocialApp = None

# دالة انشاء الحساب 
def register_view(request):
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "تم إنشاء الحساب بنجاح ✅")
            # بعد التسجيل مباشرة: إذا وُجد next نعيد التوجيه له، وإلا الرئيسية
            next_url = request.GET.get("next") or request.POST.get("next")
            return redirect(next_url or "/")
    else:
        form = AccountCreationForm()
    return render(request, "identityt/register.html", {"form": form})


# دالة تسجيل الدخول 
def login_view(request):
    # إذا كان المستخدم مسجلاً الدخول بالفعل، لا نعرض صفحة الدخول
    if request.user.is_authenticated:
        next_url = request.GET.get("next")
        return redirect(next_url or "/")

    if request.method == "POST":
        form = AccountAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # تفعيل تذكرني: إن لم يُحدد، تنتهي الجلسة عند إغلاق المتصفح
            remember = request.POST.get("remember")
            if not remember:
                request.session.set_expiry(0)  # تنتهي بإغلاق المتصفح
            # في حالة التحديد نتركها بالإعداد الافتراضي SESSION_COOKIE_AGE
            messages.success(request, f"مرحباً {user.username} 👋")
            # احترم معامل next إن كان موجوداً
            next_url = request.GET.get("next") or request.POST.get("next")
            return redirect(next_url or "/")  # يمكن تغييره لصفحة رئيسية
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة ❌")
    else:
        form = AccountAuthenticationForm()

    # جهّز قائمة المزودين الموجود لهم SocialApp في الموقع الحالي
    social_providers = []
    if SocialApp is not None:
        try:
            site = get_current_site(request)
            apps = SocialApp.objects.filter(sites=site)
            social_providers = [app.provider for app in apps]
        except Exception:
            social_providers = []

    return render(request, "identityt/login.html", {"form": form, "social_providers": social_providers})


def logout_view(request):
    logout(request)
    return redirect("/")  # يرجع المستخدم للصفحة الرئيسية بعد تسجيل الخروج


# =========================
# تسجيل الدخول برقم الجوال (OTP)
# =========================
def _normalize_ksa(msisdn: str) -> str | None:
    if not msisdn:
        return None
    p = ''.join(ch for ch in msisdn if ch.isdigit())
    if p.startswith('966') and len(p) == 12:
        return '+' + p
    if p.startswith('05') and len(p) == 10:
        return '+966' + p[1:]
    if p.startswith('5') and len(p) == 9:
        return '+966' + p
    return None


def phone_login_request(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        phone_raw = request.POST.get('phone', '').strip()
        phone = _normalize_ksa(phone_raw)
        if not phone:
            messages.error(request, 'الرجاء إدخال رقم جوال سعودي صحيح')
            return render(request, 'identityt/phone_login_request.html')

        # اصنع رمز تحقق عشوائي مكوّن من 6 أرقام
        code = f"{random.randint(0, 999999):06d}"
        # خزّن في الجلسة لمدة خطوة واحدة
        request.session['otp_phone'] = phone
        request.session['otp_code'] = code

        # إرسال الرمز عبر مزوّد SMS لاحقاً، الآن في وضع التطوير نعرضه للتجربة
        if settings.DEBUG:
            messages.info(request, f"رمز التحقق (للتجربة): {code}")

        return redirect('identity:phone_verify')

    return render(request, 'identityt/phone_login_request.html')


def phone_login_verify(request):
    if request.user.is_authenticated:
        return redirect('/')

    phone = request.session.get('otp_phone')
    if not phone:
        return redirect('identity:phone_request')

    if request.method == 'POST':
        code = request.POST.get('code', '').strip()
        if code and code == request.session.get('otp_code'):
            # نجح التحقق: أنشئ/اجلب مستخدم واربط الهاتف
            user = Account.objects.filter(phone=phone).first()
            if not user:
                # أنشئ اسم مستخدم افتراضي فريد
                base = 'user' + phone[-4:]
                uname = base
                i = 1
                while Account.objects.filter(username=uname).exists():
                    i += 1
                    uname = f"{base}{i}"
                user = Account.objects.create(username=uname, phone=phone)

            login(request, user)
            # نظّف الجلسة
            request.session.pop('otp_phone', None)
            request.session.pop('otp_code', None)
            messages.success(request, 'تم تسجيل الدخول برقم الجوال')
            next_url = request.GET.get('next') or request.POST.get('next')
            return redirect(next_url or '/')
        else:
            messages.error(request, 'رمز التحقق غير صحيح')

    return render(request, 'identityt/phone_login_verify.html', { 'phone': phone })
