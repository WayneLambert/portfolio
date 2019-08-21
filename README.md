# [Portfolio Project - at waynelambert.dev](https://waynelambert.dev)

This site is hosted at <https://waynelambert.dev> and illustrates the use of Django apps to showcase Django, Python and other programming and web framework skills and technologies. It is intended to be a desktop site and is not fully optimised for the mobile experience.

The blog is not intended to be a fully blown production product, therefore some typical blog features have been purposefully omitted. For example, comments and tags are additional features that could be developed for the blog.

## [Blog Project](https://waynelambert.dev/blog)

The blog is implemented as a classic CRUD application which uses views for each of the HTTP methods individually rather than using Django's viewsets. This is a design decision to demonstrate the ability to use the views individually. For rapid prototyping and development of a full CRUD application, Django's viewsets are likely to be a better choice.

The blog ties together users and profiles with signals so that profile data can be created when a new user is registered.

### Blog Features

- CREATE a new post assigned to the user which is logged in at the time
- READ existing posts that are either assigned to a given author, or in their entirety or simply on its own.
- UPDATE or DELETE existing post(s). This can only be achieved by the author of the post, therefore authentication checking is implemented
- Authentication and authorisation implemented
- Profiles are created in line with a user being created using Django signals
- Profiles can be viewed and adjusted as the registered author's selection choices
- The use of Django Crispy Forms makes the forms secure from cross-site attacks. The formatting of the forms are also consistent and improve upon Django's standard forms
- There are views by all posts, by author, by category and blog post detail views
- A category selector in the sidebar allows a visitor to see all of the posts listed within the selected category
- Search feature helps visitors navigate their way around the blog
- A [contents page](https://waynelambert.dev/users/contents/) allows people to see the full range of posts on the blog. The relationship between categories and posts is a many-to-many relationship.
- Django templates code is written in many files making it more easily maintainable and following the DRY principle
- Media is stored on Amazon S3
- The sites transactional emails are handled using Amazon's Simple Email Service

## [The Scrape It Project](https://waynelambert.dev/scraping/scraping-options/)

The Scrape It project demonstrates the use of the Requests library to handle the request/response cycle for the GET requests that are required to retrieve data from another website.

Python's third party library, Beautiful Soup, is used to parse the required HTML from the response object. Python text functions are used to target, strip and append any required text so that it's in a suitable format.

Finally, the Django component of the application is the handling of the URLs to target a view which returns the required response to the Django template. In other words, there is no 'M' component used within this app, it just uses the 'V' and the 'T' components of the MVT architectural paradigm that Django uses.

## [The Word Counting App](https://waynelambert.dev/count/check-count/)

The word counting app is a demonstration of using Python to calculate the number of occurrences of each of the words and letters used within the string input/pasted by the user. Again, no models are required for this app, however Django's view handles the request/response cycle and the rendering of the applicable context is handled using a Django template.

You can import some 'lorem ipsum' text instead of typing or copying/pasting. No data is recorded within the application and the text used does not appear in any analytics.

## [API Endpoints](https://waynelambert.dev/api/blog/posts)

The blog app also has some API endpoints programmed in that can be used by a front-end developer with a framework such as React, Vue or Angular.

These can be accessed by going to either of the following urls:

- [Blog Posts List View](https://waynelambert.dev/api/blog/posts)
- [Blog Post Detail View](https://waynelambert.dev/api/blog/posts/1)

The '1' part of the url can be exchanged for any other valid primary key number for the post.

These addresses expose the browsable API endpoints that Django Rest Framework provides.

## [Contact](https://www.waynelambert.dev/contact/)

You can contact me at [contact@waynelambert.dev](mailto:contact@waynelambert.dev) or by using the [contact form](https://www.waynelambert.dev/contact/) on the site.

## License

Copyright (c) Wayne Lambert. All rights reserved.

Licensed under the [MIT](/LICENSE) License.
