
from django.db import DatabaseError, connection
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET


@require_GET
@never_cache
def health_check(request):
    """
    Check whether the Django application and database are available.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")

        return JsonResponse({
            "status": "ok",
            "database": "ok",
        })

    except DatabaseError:
        return JsonResponse(
            {
                "status": "error",
                "database": "unavailable",
            },
            status=503,
        )
