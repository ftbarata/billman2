from django.shortcuts import render, redirect
from billman2.authmanager.helper_functions import _login, _logout
from .models import Service, BillingHistory, OperationHistory, CustomerDetails
from .helper_functions import decimal_to_brz
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm

def login(request):
    if request.method == 'POST':
        if request.method == 'POST':
            if _login(request):
                remote_addr = request.META['REMOTE_ADDR']
                return render(request, 'core/home.html', {'remote_addr':remote_addr})
            else:
                context = {'error_message': 'Acesso negado. Verifique seu login e senha.'}
                return render(request, 'core/login.html', context)

    else:
        return render(request, 'core/login.html')


def logout(request):
    _logout(request)
    return render(request,'core/login.html', {'status_message':'Você foi deslogado.'})


def home(request):
    if request.user.is_authenticated:
        remote_addr = request.META['REMOTE_ADDR']
        return render(request, 'core/home.html', {'remote_addr':remote_addr})
    else:
        return redirect('login')


def services(request):
    if request.user.is_authenticated:
        remote_addr = request.META['REMOTE_ADDR']
        services_queryset = Service.objects.all().filter(customer__email=request.user).order_by('count')
        services_list = []
        if len(services_list) > 0:
            total = 0
            for i in services_queryset:
                services_list.append((i.description, i.unit_price, i.count, (decimal_to_brz(i.unit_price) * i.count)))
                total += (decimal_to_brz(i.unit_price) * i.count)

            return render(request, 'core/services.html', {'remote_addr': remote_addr, 'services_queryset': services_list})
        else:
            return render(request, 'core/services.html', {'remote_addr': remote_addr, 'status_message': 'Não há serviços ativos/contratados atualmente.'})
    else:
        return redirect('login')


def history(request):
    if request.user.is_authenticated:
        remote_addr = request.META['REMOTE_ADDR']
        operation_history_queryset = OperationHistory.objects.all().filter(customer__email=request.user).order_by('-date')
        if operation_history_queryset.exists():
            return render(request, 'core/history.html', {'remote_addr': remote_addr, 'history_queryset': operation_history_queryset})
        else:
            return render(request, 'core/history.html',{'remote_addr': remote_addr, 'status_message': 'Ainda não há registros de operações.'})
    else:
        return redirect('login')


def payments(request):
    if request.user.is_authenticated:
        remote_addr = request.META['REMOTE_ADDR']
        payments_queryset = BillingHistory.objects.all().filter(customer__email=request.user).order_by('-date')
        if payments_queryset.exists():
            return render(request, 'core/payments.html',{'remote_addr': remote_addr, 'history_queryset': payments_queryset})
        else:
            return render(request, 'core/payments.html',{'remote_addr': remote_addr, 'status_message': 'Ainda não há registro financeiro.'})
    else:
        return redirect('login')


def profile(request):
    remote_addr = request.META['REMOTE_ADDR']
    if request.user.is_authenticated:
        if request.method == 'POST':
            customer = CustomerDetails.objects.get(email=request.user)
            created_at = customer.created_at
            updated_at = customer.updated_at
            form_instance = ProfileForm(request.POST, request.FILES, instance=customer)
            if form_instance.is_valid():
                print('teste')
                form_instance.save()
            else:
                print(form_instance.errors)

            return render(request, 'core/profile.html', {'remote_addr': remote_addr, 'updated_at':updated_at, 'created_at': created_at, 'form': form_instance})
        else:
            try:
                customer = CustomerDetails.objects.get(email=request.user)
            except ObjectDoesNotExist:
                customer = CustomerDetails.objects.create(email=request.user)
            finally:
                form_instance = ProfileForm(instance=CustomerDetails.objects.get(email=request.user))

                created_at = customer.created_at
                updated_at = customer.updated_at
                return render(request, 'core/profile.html', {'form':form_instance, 'remote_addr': remote_addr, 'updated_at':updated_at, 'created_at': created_at})
    else:
        return redirect('login')