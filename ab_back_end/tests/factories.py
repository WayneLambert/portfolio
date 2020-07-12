import os

import factory
from django.contrib.auth.models import User

from contacts.models import Contact


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.sequence(lambda n: f'test_user{n}@waynelambert.dev')
    first_name = 'Wayne'
    last_name = 'Lambert'
    password = factory.PostGenerationMethodCall(
        'set_password', os.environ['PYTEST_TEST_PASSWORD']
    )


class ContactFactory(factory.DjangoModelFactory):
    class Meta:
        model = Contact

    first_name = 'Wayne'
    last_name = 'Lambert'
    email = factory.sequence(lambda n: f'test_user{n}@waynelambert.dev')
    message = 'Test Message'
