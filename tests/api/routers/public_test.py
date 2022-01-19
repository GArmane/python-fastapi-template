import pytest

_prefix = "/public"


@pytest.mark.integration()
class TestPublic:
    endpoint = f"{_prefix}/status"

    def test_health_check(self, test_client, env_settings):
        with test_client:
            response = test_client.get(self.endpoint)
            assert response.status_code == 200
            assert response.json() == {
                "title": env_settings.web_app_settings.title,
                "description": env_settings.web_app_settings.description,
                "version": env_settings.web_app_settings.version,
                "status": "OK",
            }
