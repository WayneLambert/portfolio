# Screenshot Template

```python

# In settings.py
...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party
    ...
    'ckeditor',
    'ckeditor_uploader',
    ...

    # Project Apps
    'myapp.apps.MyappConfig',
    ...
]

...

```

```python

# In settings.py
...

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
        ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike',
            'SpellChecker', 'Undo', 'Redo'],
        ['Link', 'Unlink', 'Anchor'],
        ['Image', 'Table', 'HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
            'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        ['TextColor', 'BGColor'],
        ['Smiley', 'SpecialChar'],
        ['RemoveFormat', 'CodeSnippet'],
        ],
        'extraPlugins': 'codesnippet',
    }
}

...

```

```python

# In your project's urls.py

urlpatterns = [
    ... ,
    path('ckeditor/', include('ckeditor_uploader.urls')),
    ... ,
]

```
