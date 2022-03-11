import random

from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin


class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
	template_name = "agent_list.html"

	def get_queryset(self):
		organisation = self.request.user.userprofile
		return Agent.objects.filter(organisation=organisation)


class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
	template_name = "agent_create.html"
	form_class = AgentModelForm

	def get_success_url(self):
		return reverse("agents:agent-list")

	def form_valid(self, form):
		user = form.save(commit=False)
		user.is_agent = True
		user.is_organisor = False
		user.set_password(f"{random.randint(0,100000)}")
		user.save()
		Agent.objects.create(
			user=user,
			organisation=self.request.user.userprofile
		)
		send_mail(
			subject="You are invite to be an agent",
			message="You were added as an agent on DJANGOCRM. Please come login to start working.",
			from_email="admin@test.com",
			recipient_list=[user.email]
		)
		return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
	template_name = "agent_detail.html"
	context_object_name = "agent"

	def get_queryset(self):
		organisation = self.request.user.userprofile
		return Agent.objects.filter(organisation=organisation)


class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
	template_name = "agent_update.html"
	form_class = AgentModelForm

	def get_success_url(self):
		return reverse("agents:agent-list")

	def get_queryset(self):
		organisation = self.request.user.userprofile
		return Agent.objects.filter(organisation=organisation)


class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
	template_name = "agent_delete.html"
	context_object_name = "agent"

	def get_success_url(self):
		return reverse("agents:agent-list")

	def get_queryset(self):
		organisation = self.request.user.userprofile
		return Agent.objects.filter(organisation=organisation)