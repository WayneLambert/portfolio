import os

import factory

from django.contrib.auth import get_user_model

from contacts.models import Contact


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = 'test_email@example.com'
    first_name = 'Wayne'
    last_name = 'Lambert'
    username = 'wayne-lambert'
    password = factory.PostGenerationMethodCall(
        'set_password', os.environ['PYTEST_TEST_PASSWORD']
    )


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    first_name = 'Wayne'
    last_name = 'Lambert'
    email = 'test_email@example.com'
    message = 'Test Message'
