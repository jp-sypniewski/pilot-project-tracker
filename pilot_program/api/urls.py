from django.urls import path

from pilot_program.api.views import (PilotProgramListCreateAPIView,
                                     PilotProgramDetailAPIView)

urlpatterns = [
    path('pilot/', PilotProgramListCreateAPIView.as_view(), name='pilot-list'),
    path('pilot/<int:pk>', PilotProgramDetailAPIView.as_view(), name='pilot-detail')
]