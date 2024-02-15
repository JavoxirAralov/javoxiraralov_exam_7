from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView,DeleteView

from apps.form import UserForm
from apps.models import User

#
class UserListVeiw(ListView):
    template_name = 'index.html'
    queryset = User.objects.order_by('-id')
    context_object_name = 'users'
#

class UserUpdateView(UpdateView):
    template_name = 'update_user.html'
    form_class = UserForm
    model = User
    success_url = reverse_lazy('users_update')

#
class UserDeleteView(DeleteView):
    template_name = 'delete_user.html'
    model = User
    success_url = reverse_lazy('users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())

    def update(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if request.method == 'POST':
            user = self.get_object()
            user.title = request.POST['title']
            user.content = request.POST['content']
            user.save()
            return redirect('index')
        context = {
            'user': self.get_object()
        }
        return render(request, 'update_user.html', context)




