import pytest

from apps.blog.forms import PostForm


pytestmark = pytest.mark.django_db(reset_sequences=True)

class TestPostForm:

    def test_form_tests_for_all_fields(self, sample_post_data):
        """ Checks all fields requiring testing are in the form """
        form = PostForm()
        for field in sample_post_data.keys():
            if field != 'validity':
                assert field in form.fields

    def test_date_fields_not_in_form(self):
        form = PostForm()
        assert 'publish_date' not in form.fields
        assert 'updated_date' not in form.fields

    def test_empty_form_is_invalid(self):
        form = PostForm(data={})
        assert not form.is_valid(), 'Should be invalid'

    def test_form_title_requires_min_num_chars(self, sample_post_data):
        form = PostForm(data=sample_post_data)
        form.data['title'] = 'a sample title'
        error_returned = form.errors['title'][0]
        assert error_returned.startswith('Ensure this value has at least 40 characters (it has ')

    def test_form_title_is_cleaned(self, sample_post_data):
        form = PostForm(data=sample_post_data)
        form.data['title'] = 'why and how IMO salt & vinegar crisps with cheese are best.  '
        form.save(commit=False)
        title = form.cleaned_data['title']
        assert title == 'Why and How IMO Salt and Vinegar Crisps with Cheese are Best'

    def test_title_field_contains_help_text(self, sample_post_data):
        form = PostForm(data=sample_post_data)
        help_text = form.fields['title'].help_text
        assert help_text == 'The length of the post must be between 40 and 60 characters'

    def test_content_field_is_required(self, sample_post_data):
        form = PostForm(data=sample_post_data)
        form.data['content'] = ''
        error_returned = form.errors['content'][0]
        assert error_returned == 'This field is required.'

    def test_categories_field_is_required(self, sample_post_data):
        form = PostForm(data=sample_post_data)
        form.data['categories'] = ''
        error_returned = form.errors['categories'][0]
        assert error_returned == 'This field is required.'

    def test_categories_field_contains_help_text(self, sample_post_data):
        form = PostForm(data=sample_post_data)
        help_text = form.fields['categories'].help_text
        assert help_text == 'Select more than one category by holding down Ctrl or Cmd key'

    def test_form_still_submits_without_image(self, sample_post_data):
        form = PostForm(data=sample_post_data)
        form.data['image'] = None
        assert form.is_valid(), 'Should still be valid'

    def test_image_field_contains_help_text(self, sample_post_data):
        form = PostForm(data=sample_post_data)
        help_text = form.fields['image'].help_text
        assert help_text == 'For bests results, use an image that is 1,200px wide x 600px high'

    def test_status_field_is_required(self, sample_post_data):
        form = PostForm(data=sample_post_data)
        form.data['status'] = ''
        error_returned = form.errors['status'][0]
        assert error_returned == 'This field is required.'
