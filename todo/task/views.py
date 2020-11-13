from django.shortcuts import render, redirect

from django.views.generic import View
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.


class TaskView(View):
    def get(self, request):
        tasks = list(Task.objects.values())
        if request.is_ajax():
            return JsonResponse({'tasks': tasks}, status=200)

        return render(request, 'task/tasks.html')

    def post(self, request):
        bound_form = TaskForm(request.POST)

        if bound_form.is_valid():
            new_task = bound_form.save()
            return JsonResponse({'task': model_to_dict(new_task)}, status=200)

        return redirect('home')
