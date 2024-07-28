from django.urls import path
from members.views import MemberListView, MemberCreateView, MemberUpdateView, MemberDeleteView

urlpatterns = [
    path('', MemberListView.as_view(), name='member_list'),
    path('add/', MemberCreateView.as_view(), name='member_add'),
    path('edit/<int:pk>/', MemberUpdateView.as_view(), name='member_edit'),
    path('delete/<int:pk>/', MemberDeleteView.as_view(), name='member_delete'),
]