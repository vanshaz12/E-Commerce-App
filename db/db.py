
import psycopg2
import psycopg2.extras

DB_URL = "postgres://e_commerce_app_user:GzfNU7ZyGnwN8BLxywNBe8qC77Jc4jNc@dpg-ched1re7avja5m9ktlo0-a.oregon-postgres.render.com/e_commerce_app"

def sql(query, parameters=[]):
  connection = psycopg2.connect(DB_URL) # open connection
  cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # we use cursor to run SQL commands
  cursor.execute(query, parameters) # begin transaction
  results = cursor.fetchall()
  connection.commit() # end transaction
  connection.close() # close connection
  return results
