# Import the driver.
import psycopg2
import json

# Connect to the "bank" database.
conn = psycopg2.connect(
    database='bank',
    user='maxroach',
    sslmode='disable',
    port=26257,
    host='localhost'
)

# Make each statement commit immediately.
conn.set_session(autocommit=True)

# Open a cursor to perform database operations.
cur = conn.cursor()

# Create the "accounts" table.
cur.execute("CREATE TABLE IF NOT EXISTS accounts (id INT PRIMARY KEY, balance INT)")

# Insert two rows into the "accounts" table.
#cur.execute("INSERT INTO accounts (id, balance) VALUES (1, 1000), (2, 250)")

filepath = 'test.json'  
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
   	   #print(fp.readline()[1:-1])
       x=json.loads(line.strip()[1:-1])
       print(x['id'])
       print(x['bal'])
       print(x['time'])
      # cur.execute("INSERT INTO accounts (id, balance) VALUES (" x['id'] ,  x['bal'] ")")
       cur.execute("INSERT INTO accounts (id, balance) VALUES (%s,%s)",(x['id'],x['bal']))
       line = fp.readline()
       cnt += 1

# Print out the balances.
#cur.execute("SELECT id, balance FROM accounts")
#rows = cur.fetchall()
#print('Initial balances:')
#for row in rows:
#    print([str(cell) for cell in row])

# Close the database connection.
cur.close()
conn.close()
