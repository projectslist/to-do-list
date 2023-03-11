from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy  # for redirecting user

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.core.paginator import Paginator

from .models import Task



# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Pagination Starts

        tasks = context['tasks'].filter(user=self.request.user)


        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            print(search_input)

        page_number = self.request.GET.get('page') or ''
        paginator = Paginator(tasks, 2)
        page = paginator.get_page(page_number)
        context = {
            'tasks': context['tasks'].filter(user=self.request.user,title__icontains=search_input),
            'count': context['tasks'].filter(user=self.request.user, complete=False).count(),
            'search_input': search_input,
            'countPages': paginator.count,
            'page': page

        }

        # Pagination Ends

        if search_input:
            context['page'] = tasks.filter(title__startswith=search_input)


        context['search_input'] = search_input


        return context


    def get_context_dataORG(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['color'] = 'red'
        # context['tasks'] = context['tasks'].filter(user=self.request.user)
        # context['count'] = context['tasks'].filter(complete=False).count()



#Pagination Starts
        #tasks = Task.objects.all()
        tasks = context['tasks'].filter(user=self.request.user)
        paginator = Paginator(tasks, 2)
        # if(self.request.GET['page']):
        # print(self.request.GET.lists())
        if self.request.GET:
            # if self.request.GET['search-area']:
            #     print('inside for search')

            if self.request.GET['page']:
                print('inside')
                page_number = self.request.GET['page']
                page = paginator.get_page(page_number)
            else:
                print('outside')

        else:
            print('bebenki 222')
            page_number = 1
            page = paginator.get_page(page_number)

        # if(self.request.GET['page']):
        #     page_number = self.request.GET['page']
        #     print('eben')
        # else:
        #     page_number = 1
        #     print('nasil')




        context = {
            'tasks' : context['tasks'].filter(user=self.request.user),
            'count': context['tasks'].filter(user=self.request.user,complete=False).count(),
            'countPages' : paginator.count,
            'page' : page

        }

        # Pagination Ends
        print('ebeninki 0000')

        # for searching
        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            # context['tasks'] = context['tasks'].filter(title__icontains=search_input)
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
            print('ebeninki')

        context['search_input'] = search_input

        return context


class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView ):


            def delete_post(request, id):

                # check if task belongs to user
                task = Task.objects.get(id=id)

                if task.user == request.user:
                    if request.method == 'POST':

                        task.delete()
                        return redirect('tasks')

                    return render(request,
                               'base/task_confirm_delete.html',
                                      {'task': task})
                else:
                    return redirect('tasks')




