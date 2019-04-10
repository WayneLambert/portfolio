-- SQL to insert some tasks data into the Postgresql database 'todos_todo'

INSERT INTO todos_todo (title, description, open_date, due_date, completed_date, draft, priority)
VALUES ( 'Study models in Django',
         'Gain a deep understanding of the abstract models layer in Django and how that relates to a Postgresql database',
         current_timestamp,
         '2019-04-26',
         '2019-04-10',
         TRUE,
         '(1) High' );
