from rest_framework import serializers

from OAuth.service.models import MyUser
from OAuth.service.utils import create_user_service


class UserShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    middle_name = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    user_type = serializers.IntegerField(write_only=True)
    gender = serializers.IntegerField(write_only=True)
    birth_date = serializers.DateField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password',
                  'middle_name', 'phone', 'user_type', 'gender', 'birth_date')

    def create(self, validated_data):
        middle_name = validated_data.pop('middle_name')
        phone = validated_data.pop('phone')
        user_type = validated_data.pop('user_type')
        gender = validated_data.pop('gender')
        birth_date = validated_data.pop('birth_date')
        user_data = {
            'middle_name': middle_name,
            'phone': phone,
            'user_type': user_type,
            'gender': gender,
            'birth_date': str(birth_date)
        }
        user_data.update(**validated_data)
        user_data.pop('password')
        user = MyUser.objects.create_user(**validated_data)
        print('**********')
        print(validated_data)
        user.set_password(validated_data['password'])
        user_data['user_id'] = user.id
        if create_user_service(data=user_data):
            user.save()
            return user
        raise serializers.ErrorDetail


class UserListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', )