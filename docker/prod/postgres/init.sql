-- Database initialisation procedure. Passwords are changed over during the manual setup
-- phase and are only here to serve as placeholders for user initialisation.

-- Alter the default postgres user to have an encrypted password
ALTER USER postgres WITH ENCRYPTED PASSWORD 'abcdefghijklm';

-- Create a new superuser with an encrypted password
CREATE USER wayne_lambert WITH SUPERUSER ENCRYPTED PASSWORD 'catgftitw';

-- Make the password valid forever
ALTER USER wayne_lambert VALID UNTIL 'infinity';

-- Create the initial database and assign ownership to new user
CREATE DATABASE portfolio_db OWNER wayne_lambert;

-- Grant all rights and priviliges to the newly created database to the newly created superuser
GRANT ALL PRIVILEGES ON DATABASE portfolio_db TO wayne_lambert;