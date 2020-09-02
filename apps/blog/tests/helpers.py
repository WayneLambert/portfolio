""" Helper functions to facilitate the testing of the blog application """


def get_sample_form_data():
    return {
        'title': 'Test title which has a title of between 40 and 60 chars',
        'content': 'Test content',
        'categories': [1, 2],
        'reference_url': 'https://waynelambert.dev',
        'status': 0,
        'validity': True,
    }
