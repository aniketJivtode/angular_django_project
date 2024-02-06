# serializers.py
from django.contrib.auth import authenticate
from rest_framework import serializers
from usermanagement.models import User_Management
from datetime import datetime
from pytz import timezone
from django.views.decorators.http import require_http_methods
from django.db import transaction


class UserManagementProfileRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Management
        fields = ['username', 'email', 'password', 'first_name', 'last_name', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User_Management.objects.create_user(**validated_data)
        return user

    def get_fields(self):
        fields = super().get_fields()
        for field_name, field in fields.items():
            if field_name in ['is_admin', 'is_active', 'is_staff', 'is_superuser']:
                field._kwargs['default'] = field.get_default()
        return fields


class UserManagementLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    # user = authenticate(email=email, password=password)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        # Your authentication logic to validate credentials and obtain user
        user = authenticate(email=email, password=password)

        if user:
            data['user'] = user
        else:
            raise serializers.ValidationError("Invalid credentials")

        return data


class UserProfileSerializer(serializers.ModelSerializer):

    # created_on=serializers.DateTimeField(required=False,input_formats=['%d/%m/%Y %H:%M'])
    # modified_on=serializers.DateTimeField(required=False,input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = User_Management
        fields = ['id','username', 'email', 'password', 'first_name', 'last_name', 'department', 'password_expiry_status',
                  'password_change_attempts', 'user_status', 'password_creation_date', 'password_creation_time',
                  'rights', 'visible', 'created_by','created_on','modified_on', 'modified_by', 'remarks',
                  'last_passwords', 'server_rights', 'server_visible', 'server_access', 'fingerprint_data1',
                  'fingerprint_data2', 'fingerprint_data3', 'fingerprint_data4', 'fingerprint_data5']

        # fields = '__all__', 'modified_on','created_on',

    def get_modified_on(self, obj):
        return obj.modified_on.strftime('%d/%m/%Y %H:%M') if obj.modified_on else None or 'null'

    def get_created_on(self, obj):
        return obj.created_on.strftime('%d/%m/%Y %H:%M') if obj.created_on else None or 'null'

    def to_internal_value(self, data):
        # Convert 'created_on' to current datetime in 'Asia/Kolkata' time zone
        created_on_value = data.get('created_on')
        if created_on_value in [None, 'null', '']:
            india_timezone = timezone('Asia/Kolkata')
            current_time = datetime.now(india_timezone).strftime("%Y-%m-%dT%H:%M:%S")
            data['created_on'] = current_time
        elif created_on_value:
            # Parse and format 'created_on' value if it is not 'null' or an empty string
            parsed_datetime = datetime.strptime(created_on_value, "%m/%d/%Y %H:%M")
            india_timezone = timezone('Asia/Kolkata')
            formatted_datetime = india_timezone.localize(parsed_datetime).strftime("%Y-%m-%dT%H:%M:%S")
            data['created_on'] = formatted_datetime

        # Convert 'modified_on' to current datetime in 'Asia/Kolkata' time zone
        modified_on_value = data.get('modified_on')
        if modified_on_value in [None, 'null', '']:
            india_timezone = timezone('Asia/Kolkata')
            current_time = datetime.now(india_timezone).strftime("%Y-%m-%dT%H:%M:%S")
            data['modified_on'] = current_time
        elif modified_on_value:
            # Parse and format 'modified_on' value if it is not 'null' or an empty string
            parsed_datetime = datetime.strptime(modified_on_value, "%m/%d/%Y %H:%M")
            india_timezone = timezone('Asia/Kolkata')
            formatted_datetime = india_timezone.localize(parsed_datetime).strftime("%Y-%m-%dT%H:%M:%S")
            data['modified_on'] = formatted_datetime

        return super().to_internal_value(data)

    # def to_internal_value(self, data):
    #     # Convert 'created_on' and 'modified_on' to None if they are set to 'null'
    #     if data.get('created_on') == 'string' or data.get('modified_on') == '':
    #         data['created_on'] = None
    #     if data.get('modified_on') == 'string' or data.get('modified_on') == '':
    #         data['modified_on'] = None
    #
    #     return super().to_internal_value(data)

    # def to_internal_value(self, data):
    #     # Convert 'created_on' to None if it is an empty string or 'string'
    #     created_on_value = data.get('created_on')
    #     if created_on_value == 'string' or created_on_value == '':
    #         data['created_on'] = None
    #     elif created_on_value:
    #         # Parse and format 'created_on' value if it is not empty or 'string'
    #         parsed_datetime = datetime.strptime(created_on_value, "%m/%d/%Y %H:%M")
    #         formatted_datetime = parsed_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    #         data['created_on'] = formatted_datetime
    #
    #     # Convert 'modified_on' to None if it is an empty string or 'string'
    #     modified_on_value = data.get('modified_on')
    #     if modified_on_value == 'string' or modified_on_value == '':
    #         data['modified_on'] = None
    #     elif modified_on_value:
    #         # Parse and format 'modified_on' value if it is not empty or 'string'
    #         parsed_datetime = datetime.strptime(modified_on_value, "%m/%d/%Y %H:%M")
    #         formatted_datetime = parsed_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    #         data['modified_on'] = formatted_datetime
    #
    #     return super().to_internal_value(data)

    @transaction.atomic
    def update(self, instance, validated_data):
        # print("+++validated_data+++++", validated_data)
        user_id = self.context['request'].parser_context['kwargs']['pk']
        # print("user_id", user_id)
        if 'id' in validated_data:
            id = validated_data.pop('id')
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
            print("instance",instance)
            return instance



    # @require_http_methods(["PUT"])
    # def update(self, instance, validated_data):
    #     # Implement the logic to update the instance with the validated data
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.user_type = validated_data.get('user_type', instance.user_type)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.department = validated_data.get('department', instance.department)
    #     instance.password_expiry_status = validated_data.get('password_expiry_status', instance.password_expiry_status)
    #     instance.password_change_attempts = validated_data.get('password_change_attempts', instance.password_change_attempts)
    #     instance.user_status = validated_data.get('user_status', instance.user_status)
    #     instance.password_creation_date = validated_data.get('password_creation_date', instance.password_creation_date)
    #     instance.password_creation_time = validated_data.get('password_creation_time', instance.password_creation_time)
    #     instance.rights = validated_data.get('rights', instance.rights)
    #     instance.visible = validated_data.get('visible', instance.visible)
    #     instance.created_on = validated_data.get('created_on', instance.created_on)
    #     instance.created_by = validated_data.get('created_by', instance.created_by)
    #     instance.modified_on = validated_data.get('modified_on', instance.modified_on)
    #     instance.modified_by = validated_data.get('modified_by', instance.modified_by)
    #     instance.remarks = validated_data.get('remarks', instance.remarks)
    #     instance.last_passwords = validated_data.get('last_passwords', instance.last_passwords)
    #     instance.server_rights = validated_data.get('server_rights', instance.server_rights)
    #     instance.server_visible = validated_data.get('server_visible', instance.server_visible)
    #     instance.server_access = validated_data.get('server_access', instance.server_access)
    #     instance.fingerprint_data1 = validated_data.get('fingerprint_data1', instance.fingerprint_data1)
    #     instance.fingerprint_data2 = validated_data.get('fingerprint_data2', instance.fingerprint_data2)
    #     instance.fingerprint_data3 = validated_data.get('fingerprint_data3', instance.fingerprint_data3)
    #     instance.fingerprint_data4 = validated_data.get('fingerprint_data4', instance.fingerprint_data4)
    #     instance.fingerprint_data5 = validated_data.get('fingerprint_data5', instance.fingerprint_data5)
    #     instance.is_admin = validated_data.get('is_admin', instance.is_admin)
    #     instance.is_active = validated_data.get('is_active', instance.is_active)
    #     instance.is_staff = validated_data.get('is_staff', instance.is_staff)
    #     instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
    #
    #
    #     # Save the changes
    #     instance.save()
    #
    #     return instance

