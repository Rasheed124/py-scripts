
from unittest.mock import patch

from django.db import DatabaseError
from django.test import TestCase
from django.urls import reverse


class HealthCheckTests(TestCase):
    def test_health_check_returns_200_when_database_is_available(self):
        response = self.client.get(reverse("health-check"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "status": "ok",
                "database": "ok",
            },
        )

    def test_health_check_returns_503_when_database_fails(self):
        with patch(
            "config.settings.health.connection.cursor",
            side_effect=DatabaseError,
        ):
            response = self.client.get(reverse("health-check"))

        self.assertEqual(response.status_code, 503)
        self.assertEqual(
            response.json(),
            {
                "status": "error",
                "database": "unavailable",
            },
        )

    def test_health_check_only_accepts_get_requests(self):
        response = self.client.post(reverse("health-check"))

        self.assertEqual(response.status_code, 405)
