import pytest

from blog.forms import PostForm

from .helpers import get_sample_form_data

pytestmark = pytest.mark.django_db


class TestPostForm:

    fields = ('title', 'content', 'reference_url', 'status', 'exp_validity')
    sample_form_data = get_sample_form_data()

    @pytest.mark.skip(reason="TODO: Test needs further development")
    @pytest.mark.parametrize(argnames=fields, argvalues=sample_form_data)
    def test_post_form(
            self, title, content, reference_url, status, exp_validity, test_image):
        """ Tests that variations of a post form entry behaves as expected. """
        data = {
            'title': title,
            'content': content,
            'reference_url': reference_url,
            'status': status,
        }
        form = PostForm(data=data, files=test_image)

        assert form.is_valid() is exp_validity, \
            'Assets valid form submission for input variation'
