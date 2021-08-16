# PASSWORD HASHER

A little script that ask the user for an input and use the hash function from passlib library. The main purpose of this project was use a more secure way of storing users data like passwords.

## Install

after clonning, follow these instructions:

On Windows:

    $ python -m venv name of the virtualenv
    $ env\Scripts\activate
    $ pip install requirements.txt
    $ set DB_HOST=your localhost
    $ set DB_USER=your MySQL/MariaDB user
    $ set DB_PASSWORD=your MySQL/MariaDB password
    $ set DB_NAME= your database name

On Linux:

    $ python -m venv name of the virtualenv
    $ . env\Scripts\activate
    $ pip install requirements.txt
    $ export DB_HOST=your localhost
    $ export DB_USER=your MySQL/MariaDB user
    $ export DB_PASSWORD=your MySQL/MariaDB password
    $ export DB_NAME= your database name

## Running

On Windows:

    $ python main.py

On Linux:

    $ python3 main.py


Example of use:
    
    ```$ python(3) main.py
     
     $ Type your plaintext password (it won't be echoed):

     $ Your hashed password: $pbkdf2-sha256$29000$4pwzppRyTkmpdQ4hhJBSig$Yg/yq9VWkrN5NF6phWiN336r.GnwdoGqSkzsOjS8xmo

     $ Password stored in database`

### Note

- The name *****passwords** is needed for the table used in the database.
