from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from members.models import Member
from members.forms import MemberForm

class MemberListView(ListView):
    model = Member
    template_name = 'members/list.html'
    context_object_name = 'members'

class MemberCreateView(CreateView): 
    model = Member
    form_class = MemberForm
    template_name = 'members/form.html'
    success_url = reverse_lazy('member_list')

class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'members/form.html'
    success_url = reverse_lazy('member_list')

class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('member_list')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)