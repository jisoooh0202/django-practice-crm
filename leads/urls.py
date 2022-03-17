from django.urls import path
from .views import (
	lead_list, lead_detail, lead_create, lead_update, lead_delete,
	LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView, AssignAgentView, CategoryListView
)


app_name = "leads"

urlpatterns = [
	path('', LeadListView.as_view(), name='lead-list'),
	path('create/', LeadCreateView.as_view(), name='lead-create'),
	path('categories/', CategoryListView.as_view(), name='category-list'),
	path('<pk>/', LeadDetailView.as_view(), name='lead-detail'),
	path('<pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
	path('<pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
	path('<pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent')
]