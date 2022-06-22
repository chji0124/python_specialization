import sqlite3 #import SQL3 to get the library
 
conn = sqlite3.connect('emaildb.sqlite') #make a connection to database
cur = conn.cursor() #cursor is like a handle
#open it and send SQL commands to the cursor and get responses through the cursor

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    #? is a placeholder that will be replaced by 'org'
    #SQLite prepared statment; 1st sequal statement / 2nd value of that placeholder
    #(org,) is a tuple
    #not reading data, it is just to check if the syntax is correct
    row = cur.fetchone()
    #fetching (?. (org,))??
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()


# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
conn.close()