from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_fnc):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_fnc(request)
    return wrapper_func
