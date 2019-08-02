# Transactional Emails Testing

The log files included within the directory are emails that were generated as a result of testing the transactional emails configuration when setting up Amazon's Simple Email Service.

The generated email within the log files is the standard template that Django uses. This can be easily overwritten by adding a template called `password_reset_email.html`

For example, the password reset email could say something like:

```html
{% autoescape off %}
  Username: {{ user.get_username }}

  To reset your account password on {{ domain }}, click the link below:

  {{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

  If clicking the link above doesn't work, copy and paste the URL into a new browser window.

  Many thanks,

  Wayne
{% endautoescape %}
```

The `{{ domain }}` is configured within the `django_site` table of your project's database. You can access this through the admin panel.
