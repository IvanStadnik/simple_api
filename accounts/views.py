from django.shortcuts import render
from django.views.generic import TemplateView

from accounts.tasks import print_task


class DashboardView(TemplateView):
    template_name = 'accounts/dashboard.html'

    def get_context_data(self, **kwargs):
        # print_task.delay(self.request.user.id if self.request.user.is_authenticated else 1000)
        return super(DashboardView, self).get_context_data(**kwargs)
