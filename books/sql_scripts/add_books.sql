-- SQL to insert some books data into the Postgresql database 'books'

INSERT INTO books_book (title, subtitle, author, isbn)
VALUES (
            'REST APIs with Django',
            'Build powerful web APIs with Python and Django',
            'William S. Vincent',
            '978-1983029981'
        ),
        (
            'Git Pocket Guide',
            'A Working Introduction',
            'Richard E. Silverman',
            '978-1449325862'
        ),
        (
            'Python Tricks',
            'A Buffet of Awesome Python Features',
            'Dan Bader',
            '978-1775093305'
        ),
        (
            'Fluent Python',
            'Clear, Concise, and Effective Programming',
            'Luciano Ramalho',
            '978-1491946008'
        );