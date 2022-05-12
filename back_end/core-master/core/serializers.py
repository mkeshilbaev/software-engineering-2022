import datetime

from rest_framework import serializers

from core.models import Tag, Course, Module, Card, Question, AnswerOption


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'reward_amount', 'status', 'image_url',
                  'image_thumbnail_url', 'certificate_expiration_day', 'certificate_image_url',
                  'certificate_image_thumbnail_url', 'tags', 'updated_at']

    def create(self, validated_data):
        try:
            gained_tags = validated_data.pop('tags')
        except Exception as e:
            print(e)
            gained_tags = []
        course_model = Course.objects.create(**validated_data)
        for t in gained_tags:
            course_model.tags.add(t)
        course_model.save()
        return course_model


class ModuleSerializer(serializers.ModelSerializer):
    # course = serializers.PrimaryKeyRelatedField(many=False, queryset=Course.objects.all())

    class Meta:
        model = Module
        fields = ['id', 'name', 'description', 'course', 'order_index', 'image_url', 'image_thumbnail_url']
        extra_kwargs = {
            'course': {
                'read_only': True
            }
        }

    def to_representation(self, instance):
        self.fields['course'] = serializers.PrimaryKeyRelatedField(many=False, queryset=Course.objects.all())
        return super(ModuleSerializer, self).to_representation(instance)

    def create(self, validated_data):
        module_model = Module.objects.create(**validated_data)
        module_model.save()
        return module_model


class CardSerializer(serializers.ModelSerializer):
    # module = serializers.PrimaryKeyRelatedField(many=False, queryset=Module.objects.all())

    class Meta:
        model = Card
        fields = ['id', 'name', 'description', 'image_url', 'image_thumbnail_url', 'module',
                  'category', 'time_to_finish']

    def to_representation(self, instance):
        self.fields['module'] = serializers.PrimaryKeyRelatedField(many=False, queryset=Module.objects.all())
        return super(CardSerializer, self).to_representation(instance)

    def create(self, validated_data):
        card_model = Card.objects.create(**validated_data)
        card_model.save()
        return card_model


class AnswerOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerOption
        fields = ['id', 'is_correct', 'image_url', 'image_thumbnail_url', 'text']

    def create(self, validated_data):
        answer_option_model = AnswerOption.objects.create(**validated_data)
        answer_option_model.save()
        return answer_option_model


class QuestionSerializer(serializers.ModelSerializer):
    # card = serializers.PrimaryKeyRelatedField(many=False, queryset=Question.objects.all())
    answer_option = AnswerOptionSerializer(required=False, allow_null=True)

    class Meta:
        model = Question
        fields = ['id', 'card', 'question_text', 'description', 'type', 'is_shuffled',
                  'time_limit', 'answer_option', 'answer_text', 'answer_order', 'mark_point']

    def to_representation(self, instance):
        self.fields['card'] = serializers.PrimaryKeyRelatedField(many=False, queryset=Card.objects.all())
        return super(QuestionSerializer, self).to_representation(instance)

    def create(self, validated_data):
        question_model = Question.objects.create(**validated_data)
        question_model.save()
        return question_model



