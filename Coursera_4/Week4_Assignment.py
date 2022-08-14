import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite') #database
cur = conn.cursor() #cursor holds the rows (one or more) returned by SQL statement
#could be referred to in a program to fetch and process teh rows returned by SQL statement, one at a time
#use cursor to interconnect with database

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')
#composite primary key in Member table ()
#so if student 1 is taking 3 classes, composite primary key is (1,1), (1,2), (1,3)

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley"(entry[0]), "si110"(entry[1]), 1(entry[2]) ],
#   [ "Mea", "si110", 0 ]
# ]

str_data = open(fname).read() #will throw exception when there is no file to read; on open function
json_data = json.loads(str_data) #PARSING data INTO JSON object; multiple arrays in one whole array

for entry in json_data: #Entry itself is a row; we are looking at each row (which is an array )
    #we are using for loops because it is an array (not called a list; called array
    #if you are doing for loop, you are getting element (array) in the array

    name = entry[0] 
    title = entry[1]
    role = entry[2]

    print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name) 
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]
    #insert if doesn't exist --> 
    #fetchone() = fetches the nex row of a query result set, returning a single sequence(array), or NONE when no more data is available
    #?: placeholder
    #SELECT --> returns to a "result set"
    #WHERE clause is narrowing down (returning a single sequence)
    #[0]: columm
    #Prepared statement: if you present your prepared statement with a questionmark, you can provide data later
    


    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) 
        VALUES ( ?, ?, ? )''', ( user_id, course_id, role, ) )

    conn.commit()

    #SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    #  || : concatenating (putting strings together side by side)
    # AS: representing first part
    # X : alias object
    # execute(): only execute a single SQL statement
    # executescript(): execute multiple SQL statements with one call