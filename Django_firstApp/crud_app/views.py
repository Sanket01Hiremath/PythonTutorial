from django.shortcuts import render, redirect
from .models import UserForm

user_data = {}

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user_data[username] = form.cleaned_data
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})

def user_list(request):
    return render(request, 'users/user_list.html', {'user_data': user_data})

def update_user(request, username):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_data[username] = form.cleaned_data
            return redirect('user_list')
    else:
        form = UserForm(initial=user_data.get(username, {}))
    return render(request, 'users/user_form.html', {'form': form})

def delete_user(request, username):
    if username in user_data:
        del user_data[username]
    return redirect('user_list')
