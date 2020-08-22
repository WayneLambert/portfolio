""" Helper functions to facilitate the testing of the blog application """

def get_sample_form_data():
    # Data -> title, content, categories, reference_url, status, exp_validity
    return [
        (
            'Test Title', 'Test content', 'https://waynelambert.dev', 0, True
        ),
    ]
