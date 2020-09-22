from django.contrib.auth.decorators import user_passes_test
from rest_framework import status
from rest_framework.response import Response


def group_required(group_names):
    """Requires user membership in at least one of the groups passed in."""
    def decorator(view_func):
        def in_groups(request, *args, **kwargs):
            u = request.user
            if u.is_authenticated:
                if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                    return view_func(request, *args, **kwargs)
                return Response(status=status.HTTP_403_FORBIDDEN)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return in_groups
    return decorator

