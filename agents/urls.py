from django.urls import path
from .views import AgentDetailView, AgentListView, AgentCreateView, AgentUpdateView, AgentDeleteView


app_name = 'agents'

urlpatterns = [
	path('', AgentListView.as_view(), name='agent-list'),
	path('create/', AgentCreateView.as_view(), name='agent-create'),
	path('<pk>/', AgentDetailView.as_view(), name='agent-detail'),
	path('<pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
	path('<pk>/delete/', AgentDeleteView.as_view(), name='agent-delete')
]