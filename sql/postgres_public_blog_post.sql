INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (1, 'Using CSS for Image Borders', 'using-css-for-image-borders', '', '2019-06-26 17:58:00.751457', '2019-07-10 18:08:53.147970', 'ab_back_end/static/post_images/html5-css3-logo_kvb5xbh.png', 1, 2, '<p>A handy reference for setting some properties to make images with borders. For example, user profile or blog post images.</p>

<p>This was implemented within the blog to give the post&#39;s image a distinct border and can be seen on any of the blog view pages.</p>

<p><a href="https://css-tricks.com/using-css-for-image-borders/" target="_blank">https://css-tricks.com/using-css-for-image-borders/</a></p>');
INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (7, 'Customise Author Name Appearance', 'customise-author-name-appearance', '', '2019-06-26 19:56:18.161662', '2019-07-10 18:30:01.485553', 'ab_back_end/static/post_images/django-logo_sIin4jR.png', 1, 2, '<p>Within the profile settings page for a registered user on this site, there is a drop-down selection which enables them to choose how their posts will be seen by visitors. a</p>

<p>The author of a post can display their user bio with either their full name or their username. This gives them the ability to either post with anonymity should they wish to choose an obscure username, an alias should they wish to represent a company/product, or their own name if they wish for complete transparency and the more personal touch.</p>

<p>So, how is this implemented?</p>

<p>There are only two files that need to be edited for this change to take effect.</p>

<p>The <strong>models.py</strong> within the <strong>Profile</strong> model of the <strong>users</strong> app and the template rendering the author bio data. The template used is actually an HTML file (called <strong>author_view.html</strong>) which is then included within a higher level template during rendering.</p>

<p>First up, the <strong>models.py</strong></p>

<pre>
<code class="language-python">from django.contrib.auth.models import User


class Profile(models.Model):

    AUTHOR_VIEW = (
        (0, ''Username''),
        (1, ''Full Name'')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ...
    author_view = models.IntegerField(choices=AUTHOR_VIEW, default=0)
    ...
</code></pre>

<p>Next, the template which I have called <strong>author_view.html</strong></p>

<pre>
<code class="language-html">&lt;div class="article-metadata"&gt;
    &lt;p class="author_name"&gt;
      &lt;a href="{% url ''user-posts'' post.author.username %}"&gt;
        {% if post.author.profile.author_view == 0 %}
          {{ post.author.username }}
        {% else %}
          {{ post.author.first_name }} {{ post.author.last_name }}
        {% endif %}
      &lt;/a&gt;
    &lt;/p&gt;
    &lt;p class="date_stamp"&gt;
      &lt;small class="text-muted"&gt;
        Published: {{ post.publish_date|date:"D d-M-y H:i" }}  |  
        Updated: {{ post.updated_date|date:"D d-M-y H:i" }}
      &lt;/small&gt;
    &lt;/p&gt;
&lt;/div&gt;
&lt;div class="author-metadata-block"&gt;&lt;/div&gt;</code></pre>

<p>... and finally, just include that HTML snippet in whichever other template you would like it nested in.</p>

<pre>
<code class="language-html">{% include "blog/author_view.html" %}</code></pre>

<p><a href="/blog/post/advanced-form-rendering-with-django-crispy-forms/">This post</a> is an example of where the full name has been used. A guest post from an imaginary guest author going by the name of Bill Gates has chosen to display their posts using their username instead.</p>

<p>In the admin panel, this looks like...</p>

<p><img alt="" src="/media/images/admin_panel_author_view_options.png" style="height:100%; width:100%" /></p>');
INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (9, 'Using WhiteNoise for Static Files', 'using-whitenoise-for-static-files', '', '2019-06-27 16:37:29.224954', '2019-07-04 19:51:13.689634', 'ab_back_end/static/post_images/django-logo_x1yao7z.png', 1, 2, '<p>WhiteNoise is perhaps Django&#39;s de facto standard in helping manage the deployment of static assets on your production server. It works through a few small configuration settings being set in your settings.py file.</p>

<p>Check out the great PyCon US talk called &#39;<a href="https://www.youtube.com/watch?v=E613X3RBegI">Assets in Django without losing your hair</a>&#39; for more information on how to configure this in your project.</p>');
INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (3, 'The Profile Page', 'the-profile-page', '', '2019-06-26 18:17:43.607254', '2019-07-10 18:29:34.878952', 'ab_back_end/static/post_images/django-logo_GsYUSDr.png', 1, 2, '<p>The profile page consists of the fields that can be updated from both the User and the custom Profile models. The form uses Django Crispy Forms and the rendering is achieved by targeting the individual fields and using some HTML, CSS and Bootstrap styling to get the columns appearing the way they do.</p>

<p>I implemented the profile page (illustrated below) using Django Crispy Forms. When a user registers for an account, they will have access to their profile page by clicking the <strong>(Logged in as [user-name]</strong><strong>)</strong> link in the top right corner of the blog application.</p>

<p>This is the page where the author can choose how they would like their name to appear within the author bio information for their posts. You can read more about that <a href="/blog/post/customise-author-name-appearance/">here</a>.</p>

<p>The profile page for a user looks like below...</p>

<p><img alt="" src="/media/images/profile_info.png" style="height:100%; width:100%" /></p>

<p>If you want to follow along, it would be a good idea to <a href="https://github.com/WayneLambert/portfolio/blob/master/users/templates/users/profile.html" target="_blank">open the full template&#39;s code on GitHub</a>.</p>

<p>Let&#39;s go over a few of the key concepts implemented here.</p>

<p>The opening line inherits the main structure of the page from the base.html file.</p>

<pre>
<code class="language-html">{% extends "blog/base.html" %}</code></pre>

<p>The next line makes the website&#39;s static elements such as the CSS stylesheets, JavaScript files and other static assets such as images available to the template.</p>

<pre>
<code class="language-html">{% load static %}</code></pre>

<p>&nbsp;The next line means that the Crispy Form tags are available to the template for rendering.</p>

<pre>
<code class="language-html">{% load crispy_forms_tags %}</code></pre>

<p>Everything within the block content template tags is unique to the page.</p>

<pre>
<code class="language-html">{% block content %}
...
{% endblock content %}</code></pre>

<p>Let&#39;s take a look at the content of the block and pull out some of the pertinent points.</p>

<pre>
<code class="language-html">{% block content %}
  &lt;div class="content-section"&gt;
    &lt;legend class="border-bottom mb-4"&gt;Profile Info&lt;/legend&gt;
    &lt;div class="media"&gt;
      &lt;img class="rounded-circle account-img" src="{{ user.profile.profile_picture.url }}"&gt;
      &lt;div class="media-body"&gt;
        &lt;table style="width:100%"&gt;
          &lt;tr&gt;
            &lt;td&gt;
              &lt;h2 class="account-heading-name" id="account-heading-name"&gt;
                {{ user.first_name }} {{ user.last_name }}
              &lt;/h2&gt;
            &lt;/td&gt;
            &lt;td&gt;
              &lt;em&gt;
                &lt;h4 class="account-heading-username" id="account-heading-username"
                  style="text-align: right"&gt;
                  (Username: {{ user.username }} )
                &lt;/h4&gt;
              &lt;/em&gt;
            &lt;/td&gt;
          &lt;/tr&gt;
        &lt;/table&gt;
        &lt;br&gt;
        &lt;table style="width:100%"&gt;
          &lt;tr&gt;
            &lt;th&gt;Email&lt;/th&gt;
            &lt;th style="text-align: center"&gt;Join Date&lt;/th&gt;
            &lt;th style="text-align: right"&gt;Last Login Date&lt;/th&gt;
          &lt;/tr&gt;
          &lt;tr&gt;
            &lt;td&gt;
              &lt;p class="text-secondary"&gt;
                &lt;a href="mailto:{{ user.email }}"&gt;{{ user.email }}&lt;/a&gt;
              &lt;/p&gt;
            &lt;/td&gt;
            &lt;td&gt;
              &lt;p class="text-secondary" style="text-align: center"&gt;
                &lt;em&gt;{{ user.date_joined }}&lt;/em&gt;
              &lt;/p&gt;
            &lt;/td&gt;
            &lt;td&gt;
              &lt;p class="text-secondary" style="text-align: right"&gt;
                &lt;em&gt;{{ user.last_login }}&lt;/em&gt;
              &lt;/p&gt;
            &lt;/td&gt;
          &lt;/tr&gt;
        &lt;/table&gt;
      &lt;/div&gt;
    &lt;/div&gt;
    &lt;form method="POST" enctype="multipart/form-data"&gt;
      {% csrf_token %}
      &lt;fieldset class="form-group"&gt;
        &lt;div class="form-row"&gt;
          &lt;div class="form-group col-md-6 mb-0"&gt;
            {{ user_form.username|as_crispy_field }}
          &lt;/div&gt;
          &lt;div class="form-group col-md-6 mb-0"&gt;
            {{ user_form.email|as_crispy_field }}
          &lt;/div&gt;
        &lt;/div&gt;
        &lt;div class="form-row"&gt;
          &lt;div class="form-group col-md-4 mb-0"&gt;
            {{ user_form.first_name|as_crispy_field }}
          &lt;/div&gt;
          &lt;div class="form-group col-md-4 mb-0"&gt;
            {{ user_form.last_name|as_crispy_field }}
          &lt;/div&gt;
          &lt;div class="form-group col-md-4 mb-0"&gt;
            {{ profile_form.author_view|as_crispy_field }}
          &lt;/div&gt;
        &lt;/div&gt;
        {{ profile_form.profile_picture|as_crispy_field }}
      &lt;/fieldset&gt;
      &lt;div class="form-group"&gt;
        &lt;button type="submit" class="btn btn-success mr-2"&gt;
          &lt;i class="fa fa-upload"&gt;&lt;/i&gt;
           Update
        &lt;/button&gt;
        &lt;a class="btn btn-secondary mr-2"
          href="{{ request.META.HTTP_REFERER }}"&gt;
          &lt;i class="fa fa-close"&gt;&lt;/i&gt;
          Cancel
        &lt;/a&gt;
      &lt;/div&gt;
    &lt;/form&gt;
  &lt;/div&gt;
{% endblock content %}</code></pre>

<p>The page is rendering different elements from either the <strong>user_form</strong> or the <strong>profile_form</strong> which is rendered through the context within the /users/views.py file.</p>

<pre>
<code class="language-python">@login_required
def profile(request):
    if request.method == ''POST'':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile
                                         )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f''Your account has been updated!'')
            return redirect(''profile'')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        ''user_form'': user_form,
        ''profile_form'': profile_form,
    }

    return render(request, ''users/profile.html'', context)</code></pre>

<p>The view contains the @login_required decorator function which means that it can only be exposed when the user is logged in.</p>

<p>The form has a couple of other interesting pieces of functionality in addition to an essential security tag that must be included.</p>

<pre>
<code class="language-html">&lt;form method="POST" enctype="multipart/form-data"&gt;
      {% csrf_token %}
...</code></pre>

<p>The CRSF token prevents cross-site forgery requests when the form is submitted and generates a post request. The token must be in place for a Django form to be able to post, put or patch a request.</p>

<p>As you can see from the below snippet, some of the fields are from the user form (user model) and some are from the profile form (profile model).</p>

<pre>
<code class="language-html">...
&lt;fieldset class="form-group"&gt;
  &lt;div class="form-row"&gt;
    &lt;div class="form-group col-md-6 mb-0"&gt;
      {{ user_form.username|as_crispy_field }}
    &lt;/div&gt;
    &lt;div class="form-group col-md-6 mb-0"&gt;
      {{ user_form.email|as_crispy_field }}
    &lt;/div&gt;
  &lt;/div&gt;
  &lt;div class="form-row"&gt;
    &lt;div class="form-group col-md-4 mb-0"&gt;
      {{ user_form.first_name|as_crispy_field }}
    &lt;/div&gt;
    &lt;div class="form-group col-md-4 mb-0"&gt;
      {{ user_form.last_name|as_crispy_field }}
    &lt;/div&gt;
    &lt;div class="form-group col-md-4 mb-0"&gt;
      {{ profile_form.author_view|as_crispy_field }}
    &lt;/div&gt;
  &lt;/div&gt;
  {{ profile_form.profile_picture|as_crispy_field }}
&lt;/fieldset&gt;
...</code></pre>

<p>The final piece of the form&#39;s functionality is the buttons themselves. The first button is simply a success button that invokes the post request. Bootstap styling styles the buttons and font awesome is used to for the icons embedded within the buttons.</p>

<p>Finally, the cancel button is more interesting than it appears on the surface. The href takes in HTTP referrer object which is a piece of meta data belonging to the request. Essentially, this is the page that the user was on prior to them landing on the profile page. This is import here because if the user decides against updating their profile, then they just need to be redirected back to the page they were on before.</p>

<pre>
<code class="language-html">...
&lt;div class="form-group"&gt;
  &lt;button type="submit" class="btn btn-success mr-2"&gt;
    &lt;i class="fa fa-upload"&gt;&lt;/i&gt;
      Update
  &lt;/button&gt;
  &lt;a class="btn btn-secondary mr-2"
    href="{{ request.META.HTTP_REFERER }}"&gt;
    &lt;i class="fa fa-close"&gt;&lt;/i&gt;
    Cancel
  &lt;/a&gt;
&lt;/div&gt;
...</code></pre>

<p>&nbsp;I hope that this means that you will now have an idea how to implement custom profile page functionality within your website.</p>');
INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (13, 'Developing Django Project with Docker: The Dockerfile', 'developing-django-project-docker-dockerfile', 'https://github.com/WayneLambert/portfolio/blob/master/Dockerfile', '2019-07-05 14:51:50.855936', '2019-07-10 13:11:52.711414', 'ab_back_end/static/post_images/docker-logo.png', 1, 2, '<p>Docker is a headache to learn but once you get the hang of it and understand all of its concepts and moving pieces, then it works extremely well. I say &#39;all&#39; loosely here of course, since you can get 95% of what you will ever need by learning maybe 10% of its featureset.</p>

<p>I can see that using Docker would give even more benefits when developing a project with multiple languages and frameworks such as having a React fron-end with your Django application. This would mean that the packaging requirements usually managed with the <em>package.json </em>file could also be managed with Docker.</p>

<p>During my time learning about Docker and the development setup and especially making it play nicely with pipenv, I learned that the configuration is very picky. I spent countless hours researching, configuring, building, testing and above all, learning!</p>

<p>Anyway, let me guide you through the <strong>Dockerfile</strong><em> </em>that I am using as at the time of writing this guide.</p>

<p><strong>Dockerfile: In Full</strong></p>

<pre>
<code># Official Python runtime as the base image
FROM python:3.7.3-alpine

RUN apk --update add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq \
    gettext \
    nginx \
    # Pillow dependencies
    jpeg-dev \
    zlib-dev

# Set working directory
WORKDIR /code

# Add metadata to the image
LABEL author="Wayne Lambert &lt;contact@waynelambert.dev&gt;" \
    version="2019.07" \
    description="Docker image for portfolio site. Hosted at https://waynelambert.dev"

# Install pipenv from PyPI
RUN pip install pipenv

# Copy local files to container
COPY Pipfile Pipfile.lock /code/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy --dev

# Copy the contents of code folder locally to the code directory in container
COPY . .

# Run script file.
CMD ./run-dev.sh</code></pre>

<p>Let&#39;s walk through what is declared within the Dockerfile above step-by-step...</p>

<pre>
<code># Official Python runtime as the base image
FROM python:3.7.3-alpine</code></pre>

<p>This line pulls down a streamlined version of Python specifically suitable for the Alpine Linux distribution. This acts as the basis for the remainder of the docker build process.</p>

<pre>
<code>RUN apk --update add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq \
    gettext \
    nginx \
    # Pillow dependencies
    jpeg-dev \
    zlib-dev</code></pre>

<p>This step adds or updates some dependency packages that are required for my project. <strong>apk</strong> is Alpine&#39;s package manager command in a similar way to Ubuntu&#39;s <strong>apt</strong> command.</p>

<ul>
	<li>Postgresql is for the project&#39;s database</li>
	<li><strong>nginx</strong> is for the web server that would be used in development. It is not really required for the development build.</li>
	<li>The <strong>Pillow</strong> dependencies are for image management within the project.</li>
</ul>

<p>&nbsp;</p>

<pre>
<code># Set working directory
WORKDIR /code</code></pre>

<p>This sets the work directory to a folder location within the container being created called <strong>/code</strong>. I have found that it is useful to have this a slightly different than you local development environment. In my local development environment, I tend to call the source folder of the project <strong>src</strong>. It should also be noted that if the directory does not exist within the container then setting the <strong>WORKDIR</strong> in the build makes the directory.</p>

<pre>
<code class="language-bash">RUN mkdir code</code></pre>

<p>There is no need to place a line like this before it.</p>

<pre>
<code># Add metadata to the image
LABEL author="Wayne Lambert &lt;contact@waynelambert.dev&gt;" \
    version="2019.07" \
    description="Docker image for portfolio site. Hosted at https://waynelambert.dev"</code></pre>

<p>This just adds some metadata to the image that you&#39;re creating which might be useful when you put the image onto Docker Hub later.</p>

<pre>
<code># Install pipenv from PyPI
RUN pip install pipenv</code></pre>

<p>Prior to this line being executed with the build script, pipenv does not exist within the container&#39;s installation of Python which was pulled as the base image from Docker Hub at the start of the build.</p>

<pre>
<code># Copy local files to container
COPY Pipfile Pipfile.lock /code/</code></pre>

<p>The Pipfile and Pipfile.lock only exist locally within your project&#39;s root directory. These files need to exist within the container&#39;s working directory, so that they can be used by the container&#39;s recently downloaded pipenv package to install the remainder of your project&#39;s dependencies.</p>

<pre>
<code># Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy --dev</code></pre>

<p>This command uses pipenv to run a system installation using Python&#39;s default pip package manager to install of the project&#39;s dependencies including those that are labelled as <em>&#39;dev-packages&#39;</em> within the <strong>Pipfile</strong>. If you omit the <strong>--dev</strong> flag, then the command will only install those required for production.</p>

<p>The <strong>--ignore-pipfile</strong> flag means that the packages are installed as per the strict version numbers specified in the <em>&#39;Pipfile.lock&#39;</em></p>

<p>The <strong>--deploy</strong> flag ensures that your <strong>Pipfile.lock</strong> file is up to date.</p>

<pre>
<code># Copy the contents of code folder locally to the code directory in container
COPY . .</code></pre>

<p>This copies all the folders and files within your local development environments source folder (in this example, <strong>src</strong><em> </em>folder) into your working directory folder within your Docker container (in this example, the folder we called <strong>/code</strong>.</p>

<pre>
<code># Run script file.
CMD ./run-dev.sh</code></pre>

<p>... and finally, this file runs a shell script that is now accessible from within the container&#39;s working directory. The contents of the shell script is below.</p>

<pre>
<code>#!/bin/bash

python manage.py migrate

python manage.py runserver 0.0.0.0:8001</code></pre>

<p>This script is being run from within the container and therefore does not need to be preceeded with docker exec...</p>

<p>The first command migrates the history of your migration files from within your project. You will need to make sure that these migrations are all sound.</p>

<p>The second command spins up a webserver that is accessible from your browser by going to either 127.0.0.1/8001 or localhost:8001</p>

<p>Since the <strong>docker-compose.yml</strong> file invokes the build process listed within the <strong>Dockerfile</strong>,<em> </em>there is a mapping that maps the ports on the Django project&#39;s service (often called <em>&#39;web&#39;</em>) from port 8000 to 8001. Django&#39;s development port is port 8000 and I have chosen to map it to port 8001 within the container. I have found this another useful indicator that you are browsing your project through a Docker container rather than Django&#39;s standard development server.</p>

<p>The Dockerfile on GitHub for this particular post is <a href="https://github.com/WayneLambert/portfolio/blob/6594d30dde032f259235aa99d71258d675ca2f0e/Dockerfile">here</a>. The link below is where the project&#39;s most-up-date version is in case I find further enhancements to the build process.</p>');
INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (8, 'The Database Schema', 'the-database-schema', '', '2019-06-26 20:42:25.710699', '2019-07-10 18:20:23.952317', 'ab_back_end/static/post_images/postgresql-logo.png', 1, 6, '<p>This post gives a visual representation of the database schema used for this portfolio site.</p>

<p>The database schema is illustrated by the visualisation tool built into JetBrains&#39; database software called DataGrip. As an aside, I have tried many different database clients to handle PostgreSQL databases and DataGrip is certainly my favourite of them all.</p>

<p><em>Because the image requires space to view the entire schema, right click on the image and click &#39;View Image&#39; to see it more clearly.</em></p>

<p><img alt="" src="/media/images/database_schema.png" style="height:383px; width:780px" /></p>

<p>In addition to all of the default tables that come as part of Django&#39;s installation, I have added a blog app which is the main app with most of the main functionality throughout the project.</p>

<p>The blog app has a Category model and a Post model. They are linked with a many-to-many relationship so that each post can belong to many categories and each category can have many posts.</p>

<p>There is also a custom user model which links Django&#39;s users to profiles. This is achieved by using Django signals.</p>

<p>The contacts app contains a database table which captures the contact details for when people contact me through the contact form in hte top left hand corner of the home page of the site.</p>');
INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (6, 'JavaScript About Pages', 'javascript-about-pages', '', '2019-06-26 19:51:22.729121', '2019-07-10 18:10:12.590320', 'ab_back_end/static/post_images/javascript-logo_DFQwqVi.png', 1, 2, '<p>The about pages on the home page of the website is implemented with JavaScript. Some JavaScript functions were set up to present the website viewer with information that relates to the features of the application in addition to the technologies used.</p>

<p>The JavaScript uses a functional programming style with each of the functions handling only what is necessary to accomplish the task. The DRY principle of a function doing one thing and one thing well is used.</p>

<p><a href="https://waynelambert.dev">https://waynelambert.dev</a></p>');
INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (2, 'Advanced Form Rendering with Django Crispy Forms', 'advanced-form-rendering-with-django-crispy-forms', 'https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html', '2019-06-26 18:02:14.983456', '2019-07-10 18:20:44.092789', 'ab_back_end/static/post_images/django-logo_XFSSmOr.png', 1, 6, '<p>A useful blog post that explains how to render Django Crispy Forms across multiple columns by individually placing the fields within a template.</p>');
INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (11, 'Embedding CK Editor into Blog App', 'embedding-ckeditor-into-blog-app', '', '2019-07-03 20:15:01.642403', '2019-07-10 16:16:44.027130', 'ab_back_end/static/post_images/django-logo_oGybUeq.png', 1, 2, '<p>The content fields for the blog posts on this site have been created using a rich text WYSIWYG editor called CK Editor.</p>

<p>This is a JavaScript based editor that can be added to a Django project to give it the ability to add rich text and media to the website.</p>

<p>To implement this, firstly you will need to install the CK Editor. My configuration uses pipenv as the package manager and the installation is being completed within the project&#39;s root directory (called <strong>src</strong> in my case).</p>

<p>Navigate to your project&#39;s root directory and spin up a virtual environment using pipenv.</p>

<pre>
<code class="language-bash">$ pipenv shell</code></pre>

<p>&nbsp;Install Django CK Editor...</p>

<pre>
<code class="language-bash">(src) $ pipenv install django-ckeditor</code></pre>

<p>&nbsp;Then, you will need to register it within your settings area so that Django knows that it is available to your project.</p>

<pre>
<code class="language-python"># In settings.py

INSTALLED_APPS = [
    ''django.contrib.admin'',
    ''django.contrib.auth'',
    ''django.contrib.contenttypes'',
    ''django.contrib.sessions'',
    ''django.contrib.messages'',
    ''django.contrib.staticfiles'',

    # Third Party
    ...
    ''ckeditor'',  # Add
    ''ckeditor_uploader'',  # Add
    ...

    # Project Apps
    ''myapp.apps.MyappConfig'',
    ...
]</code></pre>

<p>Towards the bottom of your project settings, you will need to insert the following code:</p>

<pre>
<code class="language-python"># In settings.py
...

CKEDITOR_UPLOAD_PATH = ''uploads/''

CKEDITOR_CONFIGS = {
    ''default'': {
        ''toolbar'': ''Custom'',
        ''toolbar_Custom'': [
        [''Styles'', ''Format'', ''Bold'', ''Italic'', ''Underline'', ''Strike'',
            ''SpellChecker'', ''Undo'', ''Redo''],
        [''Link'', ''Unlink'', ''Anchor''],
        [''Image'', ''Table'', ''HorizontalRule''],
        [''NumberedList'', ''BulletedList'', ''-'', ''Outdent'', ''Indent'', ''-'',
            ''JustifyLeft'', ''JustifyCenter'', ''JustifyRight'', ''JustifyBlock''],
        [''TextColor'', ''BGColor''],
        [''Smiley'', ''SpecialChar''],
        [''RemoveFormat'', ''CodeSnippet''],
        ],
        ''extraPlugins'': ''codesnippet'',
    }
}

...</code></pre>

<p>You will need an HTML field within a suitable field within your model. In my case, and perhaps the most canonical example, is a post content field for a blog.</p>

<p>One of the fields within your model will need to be declared as a rich text uploading field so that you can do things like upload images to the field.</p>

<pre>
<code class="language-python"># In myapp.models.py

from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    ...
    content = RichTextUploadingField()
    ...</code></pre>

<p>You will need to place a reference to the CK Editors in-built urls.py file within your project&#39;s urls.py file.</p>

<pre>
<code class="language-python"># In your project''s urls.py

urlpatterns = [
    ... ,
    path(''ckeditor/'', include(''ckeditor_uploader.urls'')),
    ... ,
]</code></pre>

<p>You will then be able to benefit from having rich text at your disposal when you&#39;re creating content fields in your application.</p>

<p>If you would like to see the detail for where I learned how to implement this, please check out the video tutorial using the link below.</p>

<p><a href="https://www.youtube.com/watch?v=L6y6cn1XUfw">How to Implement CK Editor into your Django Site</a></p>');
INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (4, 'Protected Admin Page with Password Reset Feature', 'protected-admin-page-with-password-reset-feature', 'https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#overriding-the-default-admin-site', '2019-06-26 19:28:10.390416', '2019-07-10 13:17:27.255990', 'ab_back_end/static/post_images/django-logo_s6NxIfd.png', 1, 2, '<p>In this quick tutorial, we are going to learn how to protect your application against malicious automated scripts that look for admin panels. Since in Django and WordPress applications, these are located at the standard /admin path of a website, it is advisable to change your admin location. This is actually really easy to do. This is just another security measure that should be taken prior to deployment.</p>

<p>Firstly, in your <strong>.env</strong> file which should be located within your project&#39;s source directory (the same level as your <strong>manage.py</strong> file), set up an environment variable called <strong>ADMIN_ALIAS</strong> or something similar.</p>

<pre>
<code>ADMIN_ALIAS=custom-slug-to-admin-panel</code></pre>

<p>You can, of course, change the example string <strong>custom-slug-to-admin-panel</strong> to be whatever your preferred location of the admin panel will be.</p>

<p>Next up, when your project runs, it needs to get the environment variable into the settings. For a simple, key/value pair storage within your <strong>.env</strong> file, this is achieved like this.</p>

<pre>
<code class="language-python"># In your project''s settings.py

# Additional field to adjust the login point for the Admin site
ADMIN_ALIAS = os.environ[''ADMIN_ALIAS'']</code></pre>

<p>Finally, all of the URLs within your project that pertain to the admin panel need some adjustments so that when the administrator of the website navigates to them, they will still access them as they would do if the admin was delivered out of the box by Django.</p>

<pre>
<code class="language-python">from django.contrib.auth import views as auth_views
from django.urls import path
from my_project.settings import ADMIN_ALIAS


urlpatterns = [
    path(
        f''{ADMIN_ALIAS}/password_reset/'',
        auth_views.PasswordResetView.as_view(),
        name=''admin_password_reset'',
    ),
    path(
        f''{ADMIN_ALIAS}/password_reset/done/'',
        auth_views.PasswordResetDoneView.as_view(),
        name=''password_reset_done'',
    ),
    path(
        ''reset/&lt;uidb64&gt;/&lt;token&gt;/'',
        auth_views.PasswordResetConfirmView.as_view(),
        name=''password_reset_confirm'',
    ),
    path(
        ''reset/done/'',
        auth_views.PasswordResetCompleteView.as_view(),
        name=''password_reset_complete'',
    ),
    path(f''{ADMIN_ALIAS}/'', admin.site.urls),
    ...
]</code></pre>

<p>Now, your site has an additional level of protection applied.</p>');
INSERT INTO public.blog_post (id, title, slug, reference_url, publish_date, updated_date, image, status, author_id, content) VALUES (12, 'Custom 404 Page', 'custom-404-page', '', '2019-07-03 21:40:15.582893', '2019-07-10 15:32:19.069126', 'ab_back_end/static/post_images/django-logo_uBu3UWS.png', 1, 2, '<p>A custom 404 error provides an opportunity to turn a lost visitor into an engaged one by providing navigation options to direct them to a useful place within the website.</p>

<p>A 404 page could be a contents page, most visited posts page, a search box to help them find what they&#39;re looking for, etc. In Django, a 404 page is implemented by adding a 404.html to the project&#39;s templates folder.</p>

<p>For my 404 page, I have elected to give the user a search bar, the categories box omn the right hand side and the listing of each of the blog posts by category as a contents list. This helps the confused user find the resource that they&#39;re looking for. My 404.html page looks like:</p>

<pre>
<code class="language-html">{% extends "blog/base.html" %}
{% block content %}
  &lt;h3&gt;Contents Page&lt;/h3&gt;&lt;br&gt;
  {% for category in categories %}
    &lt;h6&gt;&lt;a class="category-name"
        href="{% url "blog-home" %}category/{{ category.slug }}"&gt;{{ category.name }}&lt;/a&gt;
    &lt;/h6&gt;&lt;br&gt;
    {% for item in category.posts.all %}
      &lt;a class="article-title"
          href="{% url ''post-detail'' item.slug %}"&gt;- {{ item.title }}
      &lt;/a&gt;&lt;br&gt;
    {% endfor %}
    &lt;hr&gt;
  {% endfor %}
{% endblock content %}</code></pre>

<p>As an aside, the above HTML template code achieves presenting the user with a list of categories and posts in a many-to-many relationship. The Post and Category models within this site are structured as a many-to-many relationship. You may notice that a post can appear twice within the contents listing since the post can belong to many categories.</p>');