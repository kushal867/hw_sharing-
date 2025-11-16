from django.urls import path
from .api_views import (
    SubjectListCreateView, SubjectDetailView,
    HomeworkListCreateView, HomeworkDetailView,
    SubmissionListCreateView, SubmissionDetailView,
    CommentListCreateView, CommentDetailView
)

urlpatterns = [

    # SUBJECTS
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),

    # HOMEWORK
    path('homeworks/', HomeworkListCreateView.as_view(), name='homework-list'),
    path('homeworks/<int:pk>/', HomeworkDetailView.as_view(), name='homework-detail'),

    # SUBMISSIONS
    path('submissions/', SubmissionListCreateView.as_view(), name='submission-list'),
    path('submissions/<int:pk>/', SubmissionDetailView.as_view(), name='submission-detail'),

    # COMMENTS
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
