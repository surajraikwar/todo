from .models import Task,Account
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm, AddTaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


'''
home page -
guest users gets option to login or signing up
and after logging in user gets muliple choice of options for creating is Public portfolio
'''


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect('api:list')
    else:
        return render(request, 'api/index.html')


'''
Signup with name, email and password
'''


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=password)
            login(request, account)

            return redirect('api:list')

        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'api/registration.html', context)


'''
registered user can login with his email and password
'''


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('api:list')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('api:list')

    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, 'api/login.html', context)


'''
logged in user can logout
'''


@login_required
def logout_view(request):
    logout(request)

    return redirect('api:index')


#lists all the tasks of the logged in users
def list(request):
    user=request.user
    if user.is_authenticated:
        tasks = Task.objects.filter(account=user)
        return render(request, 'api/list.html', {'tasks':tasks, 'account':user})
    else:
        return redirect('api:index')


@login_required
def add_tasks_to_account(request, *args, **kwargs):

    form = AddTaskForm()

    if request.POST:
        form = AddTaskForm(request.POST)
        if form.is_valid:
            task = form.save(commit=False)

            task.account = request.user
            task.save()


        return redirect('api:list')

    else:
        form = AddTaskForm()
    return render(request, 'api/add-task.html', {'form': form})

# deleting existing project
@login_required
def delete_task(request, pk):
    task_to_delete = Task.objects.get(pk=pk)
    task_to_delete.delete()
    return HttpResponseRedirect('/list')
