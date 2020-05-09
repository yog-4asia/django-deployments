from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views import generic

from groups.models import Group, GroupMember

# Create your views here.
class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs)
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get (self, request,*args,**kwargs):
        group = get_object_or_404(Group,self=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,('Warning already a member!'))
        else:
            messages.success(self.request,('Hey, You are now a member'))

        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self, *args,**args):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get (Self,request,*args,**kwargs):

        try:
            membership = models.GroupMember.objects.filter(
            user=self.request.user,
            group__slug=self.kwargs.get('slug')
            ).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this group!')
        else:
            membership.delete()
            messages.success (self.request, 'You have left the group')
    return super().get(request,*args,**kwargs)

    



















    def get(self, *args,**kwargs):
