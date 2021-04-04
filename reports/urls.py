from django.urls import path
from .views import (
    ReportListView,
    ReportUpdateView,
    ReportDetailView,
    ReportDeleteView,
    ReportCreateView
)

urlpatterns = [
    path('<int:pk>/edit', ReportUpdateView.as_view(), name='report_edit'),
    path('<int:pk>', ReportDetailView.as_view(), name='report_detail'),
    path('<int:pk>/delete', ReportDeleteView.as_view(), name='report_delete'),
    path('new/', ReportCreateView.as_view(), name='report_new'),
    path('', ReportListView.as_view(), name='report_list'),
]