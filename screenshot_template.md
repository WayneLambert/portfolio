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

```python

# In your project's settings.py

# Additional field to adjust the login point for the Admin site
ADMIN_ALIAS = os.environ['ADMIN_ALIAS']

```

```env
ADMIN_ALIAS=custom-slug-to-admin-panel

```

```python

from django.contrib.auth import views as auth_views
from django.urls import path
from my_project.settings import ADMIN_ALIAS


urlpatterns = [
    path(
        f'{ADMIN_ALIAS}/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        f'{ADMIN_ALIAS}/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    path(f'{ADMIN_ALIAS}/', admin.site.urls),

```

```python

from django.contrib.auth.models import User


class Profile(models.Model):

    AUTHOR_VIEW = (
        (0, 'Username'),
        (1, 'Full Name')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ...
    author_view = models.IntegerField(choices=AUTHOR_VIEW, default=0)
    ...

```


```html

<div class="article-metadata">
    <p class="author_name">
      <a href="{% url 'user-posts' post.author.username %}">
        {% if post.author.profile.author_view == 0 %}
          {{ post.author.username }}
        {% else %}
          {{ post.author.first_name }} {{ post.author.last_name }}
        {% endif %}
      </a>
    </p>
    <p class="date_stamp">
      <small class="text-muted">
        Published: {{ post.publish_date|date:"D d-M-y H:i" }}  |  
        Updated: {{ post.updated_date|date:"D d-M-y H:i" }}
      </small>
    </p>
</div>
<div class="author-metadata-block"></div>

```

```html

{% include "blog/author_view.html" %}

```
