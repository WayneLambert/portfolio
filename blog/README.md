# Django Blog

![Django Blog](https://wl-portfolio.s3.eu-west-2.amazonaws.com/post_images/django-blog.png)

The blog is implemented as a classic CRUD application which uses views for each of the HTTP methods individually rather than using Django's viewsets. This is a design decision to demonstrate the ability to use the views individually.

For rapid prototyping and development of a full CRUD application, Django's viewsets are likely to be a better choice.

The blog itself contains articles that document some of the processes and design decisions for the portfolio website in addition to more general programming, web development and data science topics.

## Blog Features

- Uses a PostgreSQL database for production.
- Tests are built in using the PyTest framework and a SQLite database.
- CREATE a new post assigned to the user which is logged in at the time.
- READ existing posts that are either assigned to a given author, or in their entirety or simply on its own.
- UPDATE or DELETE existing post(s). This can only be achieved by the author of the post, therefore authentication checking is implemented.
- Authentication and authorisation implemented.
- Profiles are created in line with a user being created using Django signals. This is achieved by associating a sender with a receiver to create an attachment from one element to another.
- Profiles can be viewed and adjusted as the registered author's selection choices.
- The use of Django Crispy Forms makes the forms secure from cross-site attacks. The formatting of the forms are also consistent and improve upon Django's standard forms.
- There are views by all posts, by author, by category and blog post detail views.
- A category selector in the sidebar allows a visitor to see all of the posts listed within the selected category.
- Search feature helps visitors navigate their way around the blog.
- A [contents page](https://waynelambert.dev/blog/contents/) allows visitors to see the full range of posts on the blog. The relationship between categories and posts is a many-to-many relationship, therefore the same post may appear more than once on the contents page.
- Django templates code is written in many files making it more easily maintainable and following the DRY principle.
- Media is stored on Amazon S3.
- The site's transactional emails are handled using Amazon's Simple Email Service.

## Technologies Used

- Languages: Python, HTML / CSS
- Frameworks: Django, Django REST Framework, Bootstrap, FontAwesome
- Libraries: Whitenoise, PyTest, Bandit
- Other: GitHub, Docker
