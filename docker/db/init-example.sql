-- This file exists for documentation purposes only. My actual file (init.sql)
-- used to construct the project contains my actual secret values.
-- The init.sql file is stored in the same location as this file, however is not
-- visible in my git or docker repositories because it has been added to the
-- .gitignore and .dockerignore files. 

-- Simply use the below code as boilerplate for your project!

-- Alter the default postgres user to have an encrypted password
ALTER USER postgres WITH ENCRYPTED PASSWORD 'choose-a-password';

-- Create a new superuser with an encrypted password
CREATE USER your_chosen_username WITH SUPERUSER ENCRYPTED PASSWORD 'choose-a-password';

-- Make the password valid forever
ALTER USER your_chosen_username VALID UNTIL 'infinity';

-- Create the initial database and assign ownership to new user
CREATE DATABASE your_chosen_database_name OWNER your_chosen_username;

-- Grant all rights and priviliges to the newly created database to the newly created superuser
GRANT ALL PRIVILEGES ON DATABASE your_chosen_database_name TO your_chosen_username;