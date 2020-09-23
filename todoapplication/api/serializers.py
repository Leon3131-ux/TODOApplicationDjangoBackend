from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from todoapplication.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'done', 'date', 'deleted')
        extra_kwargs = {
            "description": {
                "error_messages": {
                    "null": "errors.task.description.required",
                    "blank": "errors.task.description.required",
                    "required": "errors.task.description.required"
                }
            },
            "date": {
                "error_messages": {
                    "invalid": "errors.task.date.invalid",
                    "required": "errors.task.date.invalid",
                    "null": "errors.task.date.invalid"
                }
            },
            "done": {
                "error_messages": {
                    "null": "errors.task.done.required",
                }
            },
            "deleted": {
                "error_messages": {
                    "null": "errors.task.deleted.required"
                }
            }
        }

    # fields with unique=True require special attention for custom error messages
    title = fields.CharField(
        validators=[UniqueValidator(queryset=Task.objects.all(), message='errors.task.title.alreadyUsed')],
        error_messages={"null": "errors.task.title.required", "blank": "errors.task.title.required", "exists": "errors.task.title.alreadyUsed"}
    )


def get_validation_errors(serializer_errors):
    validation_errors = []
    for errors in serializer_errors.values():
        for errorDetail in errors:
            validation_errors.append(errorDetail)
    return validation_errors

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['groups'] = self.user.groups.values_list('name', flat=True)
        return data
