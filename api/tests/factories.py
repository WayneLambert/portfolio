import factory
from django.contrib.auth import get_user_model

from ab_back_end import settings


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.sequence(lambda n: f"test_email{n}@example.com")
    first_name = 'Wayne'
    last_name = 'Lambert'
    password = factory.PostGenerationMethodCall(
        'set_password', settings.PYTEST_TEST_PASSWORD
    )
