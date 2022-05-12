from django.urls import path, include

from core import views


answer_url_patterns = [
    path('',views.AnswerOptionView.as_view()),
    path('<int:pk>/', views.AnswerOptionDetailView.as_view())
]

question_url_patterns = [
    path('', views.QuestionView.as_view()),
    path('<int:pk>/', views.QuestionDetailView.as_view())
]

tag_url_patterns = [
    path('', views.TagView.as_view()),
    path('<int:pk>/', views.TagDetailView.as_view())
]

urlpatterns = [
    path('tags/', include(tag_url_patterns)),

    path('course/', views.CourseView.as_view()),
    path('course/<int:course_id>/', views.CourserDetailView.as_view()),

    path('course/<int:course_id>/module/', views.ModuleView.as_view()),
    path('course/<int:course_id>/module/<int:module_id>/', views.ModuleDetailView.as_view()),

    path('course/<int:course_id>/module/<int:module_id>/card/', views.CardView.as_view()),
    path('course/<int:course_id>/module/<int:module_id>/card/<int:card_id>/', views.CardDetailView.as_view()),

    path('course/<int:course_id>/module/<int:module_id>/card/<int:card_id>/question/', views.QuestionView.as_view()),
    path('course/<int:course_id>/module/<int:module_id>/card/<int:card_id>/question/<int:question_id>/',
         views.QuestionDetailView.as_view()),

    path('answer_option/', include(answer_url_patterns)),
]