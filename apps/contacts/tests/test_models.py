from django.db import models

import pytest

from mixer.backend.django import mixer

from apps.contacts.models import Contact


pytestmark = pytest.mark.django_db(reset_sequences=True)

class TestContact:
    def test_single_contact_save(self, random_contact):
        assert random_contact.pk == 1, 'Should create a `Contact` instance'

    def test_multi_contact_saves(self):
        contacts = mixer.cycle(10).blend(Contact)
        assert contacts[9].pk == 10, '10th instance should have a PK of 10'
        assert Contact.objects.count() == 10, 'Should have 10 objects in the database'

    def test_can_delete_contact(self):
        contacts = mixer.cycle(10).blend(Contact)
        contacts[4].delete()
        assert Contact.objects.count() == 9, \
            'Should have 9 objects remaining in the database'

    def test_first_name_is_charfield(self, random_contact):
        field = random_contact._meta.get_field("first_name")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_last_name_is_charfield(self, random_contact):
        field = random_contact._meta.get_field("last_name")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_email_is_emailfield(self, random_contact):
        field = random_contact._meta.get_field("email")
        assert isinstance(field, models.EmailField), 'Should be an email field'

    def test_message_is_textfield(self, random_contact):
        field = random_contact._meta.get_field("message")
        assert isinstance(field, models.TextField), 'Should be a text field'

    def test_submit_date_is_datetimefield(self, random_contact):
        field = random_contact._meta.get_field("submit_date")
        assert isinstance(field, models.DateTimeField), 'Should be a datetime field'

    def test_full_name(self):
        contact = mixer.blend(Contact)
        contact.first_name = 'wayne'
        contact.last_name = 'lambert'
        assert contact.full_name == 'Wayne Lambert', \
            'Should return concatenation of first and last name with capitalised first letters'

    def test_contact_str(self):
        contact = mixer.blend(Contact, first_name='Wayne', last_name='Lambert')
        assert contact.__str__() == contact.full_name, 'Str should be set to full_name property'
