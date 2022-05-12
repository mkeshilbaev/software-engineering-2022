from django.http import Http404
from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.serializers import TagSerializer, CourseSerializer, ModuleSerializer, CardSerializer, QuestionSerializer, \
    AnswerOptionSerializer
from core.models import Tag, Course, Module, Card, Question, AnswerOption


class TagView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        cur_course_id = instance.id
        self.perform_destroy(instance)
        res_data = 'Tag with id: ' + str(cur_course_id) + ' deleted!'
        return Response(data={'status': res_data}, status=status.HTTP_202_ACCEPTED)


class CourseView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    parser_classes = (MultiPartParser, JSONParser)


class CourserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    parser_classes = (MultiPartParser, JSONParser)
    lookup_url_kwarg = 'course_id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        cur_course_id = instance.id
        self.perform_destroy(instance)
        res_data = 'Course with id: ' + str(cur_course_id) + ' deleted!'
        return Response(data={'status': res_data}, status=status.HTTP_202_ACCEPTED)


class ModuleView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ModuleSerializer
    parser_classes = (MultiPartParser, JSONParser)

    def get_queryset(self):
        try:
            course = Course.objects.get(id=self.kwargs.get('course_id'))
        except Course.DoesNotExist:
            raise Http404
        queryset = course.module_course.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(course=Course.objects.get(id=self.kwargs.get('course_id')))


class ModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    parser_classes = (MultiPartParser, JSONParser)

    def get_object(self):
        return get_object_or_404(Module, id=self.kwargs.get('module_id'))

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        cur_course_id = instance.id
        self.perform_destroy(instance)
        res_data = 'Module with id: ' + str(cur_course_id) + ' deleted!'
        return Response(data={'status': res_data}, status=status.HTTP_202_ACCEPTED)


class CardView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CardSerializer
    parser_classes = (MultiPartParser, JSONParser)

    def get_queryset(self):
        return Card.objects.filter(module_id=self.kwargs.get('module_id'),
                                   module__course_id=self.kwargs.get('course_id'))

    def perform_create(self, serializer):
        serializer.save(module=Module.objects.get(id=self.kwargs.get('module_id')))


class CardDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CardSerializer
    parser_classes = (MultiPartParser, JSONParser)

    def get_object(self):
        return get_object_or_404(Card, id=self.kwargs.get('card_id'))

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        cur_course_id = instance.id
        self.perform_destroy(instance)
        res_data = 'Card with id: ' + str(cur_course_id) + ' deleted!'
        return Response(data={'status': res_data}, status=status.HTTP_202_ACCEPTED)


class QuestionView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(card_id=self.kwargs.get('card_id'),
                                       card__module_id=self.kwargs.get('module_id'),
                                       card__module__course_id=self.kwargs.get('course_id'))

    def perform_create(self, serializer):
        serializer.save(card=Card.objects.get(id=self.kwargs.get('card_id')))


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = QuestionSerializer

    def get_object(self):
        return get_object_or_404(Question, id=self.kwargs.get('question_id'))

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        cur_course_id = instance.id
        self.perform_destroy(instance)
        res_data = 'Question with id: ' + str(cur_course_id) + ' deleted!'
        return Response(data={'status': res_data}, status=status.HTTP_202_ACCEPTED)


class AnswerOptionView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AnswerOptionSerializer
    queryset = AnswerOption.objects.all()
    parser_classes = (MultiPartParser, JSONParser)


class AnswerOptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AnswerOptionSerializer
    queryset = AnswerOption.objects.all()
    parser_classes = (MultiPartParser, JSONParser)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        cur_course_id = instance.id
        self.perform_destroy(instance)
        res_data = 'Answer option with id: ' + str(cur_course_id) + ' deleted!'
        return Response(data={'status': res_data}, status=status.HTTP_202_ACCEPTED)



