from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Report

class ReportListView(LoginRequiredMixin, ListView):
    model=Report
    template_name='report_list.html'

class ReportDetailView(LoginRequiredMixin, DetailView):
    model=Report
    template_name='report_detail.html'

class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Report
    fields=('title','body')
    template_name='report_edit.html'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Report
    template_name='report_delete.html'
    success_url=reverse_lazy('report_list')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ReportCreateView(LoginRequiredMixin, CreateView):
    model=Report
    fields=('title','body')
    template_name='report_new.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
