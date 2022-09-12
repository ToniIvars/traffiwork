from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .forms import ClassroomCreationForm
from .models import Classroom

@login_required
def add(request):
    if request.method == 'POST':
        form = ClassroomCreationForm(request.POST)

        if form.is_valid():
            classroom = form.save(commit=False)

            classroom.creator = request.user
            classroom.save()
            classroom.participants.add(request.user)

            form.save_m2m()

            messages.success(request, 'La clase se ha creado correctamente')
            return redirect(reverse('dashboard'))

    else:
        form = ClassroomCreationForm()

    return render(request, 'classrooms/add.html', {'form': form})

@login_required
def join(request, id):
    classroom = get_object_or_404(Classroom, pk=id)

    try:
        classroom.participants.get(pk=request.user.pk)
        messages.error(request, f'Ya participas en la clase "{classroom.name}"')
    except ObjectDoesNotExist:
        classroom.participants.add(request.user)
        messages.success(request, f'Te has unido a la clase "{classroom.name}"')

    return redirect(reverse('dashboard'))