from rest_framework import serializers
from users.models import IR_M_USERS


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = IR_M_USERS
        fields = ('__all__', 'confirm_password')
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None and password == confirm_password :
            instance.set_password(password)
        else:
            raise serializers.ValidationError("password doesn't match")
        instance.save()
        return instance