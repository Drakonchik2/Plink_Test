from rest_framework import serializers
from .models import ValidParametres


class ValParSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidParametres
        fields = ('email', 'password', 'first_name', 'last_name')

    def validate_email(self, value):
        if 'gmail' in value:
            raise serializers.ValidationError('Wrong email domain name')
        elif 'icloud' in value:
            raise serializers.ValidationError('Wrong email domain name')
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('Wrong password length')
        if value[0].islower():
            raise serializers.ValidationError('Should begin from uppercase')
        if value[0].isalpha() == False:
            raise serializers.ValidationError('Should begin from uppercase letter')
        return value
