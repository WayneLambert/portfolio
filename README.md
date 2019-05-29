# Portfolio Project

The site hosted at waynelambert.dev is intended to illustrate the problem solving skills of a web developer and data scientist using web technologies, programming languages and frameworks.

It is accepted that in some cases, the solutions are overkill in terms of what would suffice in an actual production environment and the site is intended to demonstrate skill and usage of the applicable technologies.

## Blog

The classic blog is implemented as a classic CRUD application which uses views for each of the HTTP methods individually rather than using Django's viewsets. This is a design decision to demonstrate the ability to use the views individually. For rapid prototyping and development of a full CRUD application, Django's viewsets are likely to be a better choice.

The blog uses images and has various different relationships between other tables within the database structure. The relationships of the database tables can be seen in the diagram [ INSERT LINK HERE ]

A custom users model is implemented which ties together blog authors and users that have registered with the site.

## License

Copyright (c) Wayne Lambert. All rights reserved.

Licensed under the [MIT](LICENSE.txt) License.