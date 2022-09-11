from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from classrooms.models import Classroom

@login_required
def dashboard(request):
    created_classrooms = Classroom.objects.filter(creator=request.user)
    participating_classrooms = Classroom.objects.filter(participants=request.user)

    return render(request, 'students/dashboard.html', {
        'user': request.user,
        'created_classrooms': created_classrooms,
        'participating_classrooms': participating_classrooms
    })

@login_required
def profile(request, username):
    if username == request.user.username:
        return redirect(reverse('dashboard'))

    user = get_object_or_404(User, username=username)

    return render(request, 'students/profile.html', {'user': user})