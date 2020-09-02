from django.urls import path

from pilot_program.api.views import (PilotProgramListCreateAPIView,
                                     PilotProgramDetailAPIView,
                                     TaskListCreateAPIView,
                                     TaskDetailAPIView)

urlpatterns = [
    path('pilots/', PilotProgramListCreateAPIView.as_view(), name='pilot-list'),
    path('pilots/<int:pk>', PilotProgramDetailAPIView.as_view(), name='pilot-detail'),
    path('pilots/<int:pilot_pk>/tasks', TaskListCreateAPIView.as_view(), name='pilot-tasks'),
    path('tasks/<int:pk>', TaskDetailAPIView.as_view(), name='task-detail')
]