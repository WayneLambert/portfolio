# Portfolio Project - waynelambert.dev

The site will soon be hosted at waynelambert.dev and is intended to illustrate the use of Django apps to showcase Django, Python and other programming and web framework skills and technologies.

It is accepted that in some cases, the solutions are overkill in terms of what would suffice in an actual production environment and the site is intended to demonstrate the application of programming skill and usage of applicable technologies.

The blog is not intended to be a full production product, therefore some typical blog features have been purposefully omitted. For example, comments could be added to the blog, however this one has been designed for dictators. :)

## Blog

The blog is implemented as a classic CRUD application which uses views for each of the HTTP methods individually rather than using Django's viewsets. This is a design decision to demonstrate the ability to use the views individually. For rapid prototyping and development of a full CRUD application, Django's viewsets are likely to be a better choice.

The blog ties together users and profiles with signals so that profile data can be created when a new user is registered. The blog uses the Pillow library to compress and adjust images when a user registers to the site.

Various relationships exist within the blog to demonstrate the use of differnet database relationships and how the ORM can be queried using querysets. The relationships of the database tables can be seen in the diagram captured from JetBrains' DataGrip software [ INSERT LINK HERE ]

### Blog Features

- CREATE a new post assigned to the user which is logged in at the time.
- READ existing posts that are either assigned to a given author, or in their entirety or simply on its own.
- UPDATE or DELETE existing post(s). This can only be achieved by the author of the post, therefore authentication checking is implemented.
- A users and profiles components of the overall app that is tied together using signals. A save_profile function is augmented with the ability to save a new profile instance based upon the event of a post being saved by a given user. This is done by the use of a @receiver decorator.
- Each profile can have a profile picture attached to it.
- The use of Django Crispy Forms makes the forms secure from cross-site attacks. The formatting of the forms are also consistent and improve upon Django's standard forms.

## The Scrape It! Project

The Scrape It! demonstrates the use of the Requests library to handle the request/response cycle for the GET requests that are required to retrieve data from another website.

Python's third party library, Beautiful Soup, is used to parse the required HTML from the response object. Python text functions are used to target, strip and append any required text so that it's in a suitable format.

Finally, the Django component of the application is the handling of the URLs to target a view which returns the required response to the Django template. In other words, there is no 'M' component used within this app, it just uses the 'V' and the 'T' components of the MVT architectural paradigm that Django uses.

## The Word Counting App

The word counting app is another demonstration of using Python to calculate the number of occurences of each of the words and letters used within the string input/pasted by the user. Again, no models are required for this app, however Django's view handles the request/response cycle and the rendering of the applicable context is handled using a Django template.

## License

Copyright (c) Wayne Lambert. All rights reserved.

Licensed under the [MIT](/LICENSE) License.
