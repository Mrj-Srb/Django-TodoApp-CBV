
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.urls import reverse_lazy

# Create your views here.


class TasksList(ListView,LoginRequiredMixin):
    template_name = 'todo/tasks/tasks_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        tasks = Task.objects.filter(user = self.request.user)

        return tasks 
    
class CreateTask(CreateView,LoginRequiredMixin):
    model = Task
    fields = ['content']
    success_url = reverse_lazy("tasks_list")
    

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CreateTask,self).form_valid(form)
    


class UpdateTask(UpdateView,LoginRequiredMixin):
    model = Task
    fields = ['content']
    success_url = reverse_lazy("tasks_list")
    template_name = 'todo/tasks/tasks_edit.html'

class DeleteTask(DeleteView,LoginRequiredMixin):
    model = Task
    success_url = reverse_lazy("tasks_list")
    template_name = 'todo/tasks/tasks_delete.html'

class DoneTask(View,LoginRequiredMixin):

    def get(self,*args,**kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task,user=self.request.user,id=pk)
        if not task.is_done:
            task.is_done = True
        elif task.is_done:
            task.is_done = False
        task.save()
        return redirect(reverse_lazy("tasks_list"))
        
    
    
