# Django Rest Framework API Endpoints

![Django REST API Endpoints](https://wl-portfolio.s3.eu-west-2.amazonaws.com/post_images/django-rest-framework.png)

The Django blog also has some REST API endpoints that can be used by a front-end developer with a framework such as React, Vue, Angular or Ember.

These can be accessed by going to either of the following urls:

- [Blog Posts List View](https://waynelambert.dev/api/blog/posts)
- [Blog Post Detail View](https://waynelambert.dev/api/blog/posts/1)

## Implementation & Design Details

- Naturally, the implementation of these endpoints is a highly contrived example for portfolio demonstration purposes.
- The '1' part of the url for the detail view can be exchanged for any other valid primary key number for the post.
- These addresses expose the browsable API endpoints that Django Rest Framework provides.
- Pagination is applied to the posts view so that only 5 posts per page are displayed.
- The time is left in its raw format so that a front-end library such as `moment` can format the time according to each user's locale.

## Technology Stack

- Languages: Python, HTML / CSS
- Frameworks: Django / Django REST Framework
- Databases: PostgreSQL, SQLite3
- Other: GitHub / Docker
