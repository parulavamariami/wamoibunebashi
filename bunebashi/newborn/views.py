from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, User, Genre, Username, Comment
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserRegisterForm, ServiceForm, UserForm
from .seeder import seeder_func
from django.contrib import messages

def home(request):
    return render(request, 'newborn/home.html')

def about(request):
    heading = 'What About Us?'
    context = {'heading': heading}
    return render(request, 'newborn/about.html', context)

def contact(request):
    heading = 'Contact Info'
    context = {'heading': heading}
    return render(request, 'newborn/contact.html', context)
def sservices(request):
    lookfor = request.GET.get("lookfor") if request.GET.get("lookfor") is not None else ''
    services = Service.objects.filter(Q(title__icontains=lookfor) | Q(genre__name__icontains=lookfor))
    services = list(dict.fromkeys(services))
    heading = 'Services'
    seeder_func()
    genre = Genre.objects.all()
    context = {'services': services, 'heading': heading, 'genre': genre}
    return render(request, 'newborn/services.html', context)
@login_required(login_url='login')
def profile(request, userid):
    user = User.objects.get(id=userid)
    services = user.services.all()
    username = request.user
    heading = f'Welcome back @{username}!'
    context = {'services': services, 'heading': heading}
    return render(request, 'newborn/profile.html', context)
@login_required(login_url='login')
def saving(request, userid):
    user = request.user
    serviceid = Service.objects.get(id=userid)
    user.services.add(serviceid)
    return redirect('profile', user.id)
@login_required(login_url='login')
def remove(request, serviceid):

    obj = Service.objects.get(id=serviceid)
    heading = f'Are you sure you want to remove {obj}?'
    context = {'heading': heading, 'obj': obj}

    if request.method == "POST":
        request.user.services.remove(obj)
        return redirect('profile', request.user.id)

    return render(request, 'newborn/delete.html', context)

def login_user(request):

    if request.user.is_authenticated:
        return redirect('newborn/profile.html', request.user.id)

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist! Try again!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            messages.error(request, 'Username or Password is not correct!')

    heading = 'Let me in'
    context = {'heading': heading}
    return render(request, 'newborn/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):

    form = MyUserRegisterForm()
    heading = 'Sign Up'

    if request.method == 'POST':
        form = MyUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile', user.id)
        else:
            messages.error(request, 'Follow The Instructions and create proper user and password...')

    context = {'heading': heading, 'form': form}

    return render(request, 'newborn/register.html', context)
@login_required(login_url='login')
def add_service(request):
    heading = 'Add New Service '

    genres = Genre.objects.all()
    usernames = Username.objects.all()
    form = ServiceForm()


    if request.method == 'POST':

        service_genres = request.POST.get('genre')
        service_users = request.POST.get('username')

        genre, created = Genre.objects.get_or_create(name=service_genres)
        username, created = Username.objects.get_or_create(fullname=service_users)

        form = ServiceForm(request.POST)

        new_service = Service(creator=request.user, picture=request.FILES['picture'], title=form.data['title'],
                              price=form.data['price'],username=username, description=form.data['description'])

        new_service.save()
        new_service.genre.add(genre)
        return redirect('services')

    context = {'heading': heading, 'form': form, 'genres': genres, 'usernames': usernames}
    return render(request, 'newborn/add-service.html', context)

def see_closer(request, id):
    service = Service.objects.get(id=id)
    heading = f'See {service}'
    service_comments = service.comment_set.all()  # .order_by('-created')
    if request.method == "POST":
        Comment.objects.create(
            user=request.user,
            service=service,
            body=request.POST.get('body')
        )
    context = {'heading': heading, 'service': service, 'comments': service_comments}
    return render(request, 'newborn/see_closer.html', context)

def delete_service(request, serviceid):

    obj = Service.objects.get(id=serviceid)
    heading = f'Delete {obj}?'
    context = {'heading': heading, 'obj': obj}

    if request.method == "POST":
        obj.picture.delete()
        obj.delete()
        return redirect('profile', request.user.id)
    return render(request, 'newborn/delete.html', context)

@login_required(login_url='login')
def update_user(request):
    heading = 'Update Your Profile'
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)

    context = {'heading': heading, 'form': form}
    return render(request, 'newborn/update_user.html', context)

def delete_comment(request, id):
    heading = 'Damn, delete comment, really?'
    comment = Comment.objects.get(id=id)
    service = comment.service
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=id)
        comment.delete()
        return redirect('see-closer', service.id)


    context = {'heading': heading, 'obj': comment}
    return render(request, 'newborn/delete.html', context)

"""def myservices(request, userid):
    registred_users = Service.user.all()
    print(registred_users)

    return render(request, 'newborn/my_services.html', context)"""