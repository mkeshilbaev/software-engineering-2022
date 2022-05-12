from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    coins = serializers.IntegerField(read_only=True)
    birth_date = serializers.DateField(required=False)

    class Meta:
        model = User
        fields = ['id', 'user_id', 'first_name', 'middle_name', 'last_name', 'birth_date', 'email', 'phone', 'gender',
                  'user_type', 'coins']


class CheckAccessSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(write_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_teacher = serializers.BooleanField(read_only=True)
    is_student = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        user_id = validated_data['user_id']
        cur_user = User.objects.get(user_id=user_id)
        is_admin = is_teacher = is_student = False
        if cur_user.is_admin():
            is_admin = True
        if cur_user.is_teacher():
            is_teacher = True
        if cur_user.is_student():
            is_student = True
        return {'is_admin': is_admin, 'is_teacher': is_teacher, 'is_student': is_student}