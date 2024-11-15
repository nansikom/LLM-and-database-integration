import sqlite3
import pandas as pd

# Use the relative path to the database file
database = 'chinook.db'

# Create a connection to the database
conn = sqlite3.connect(database)

# Query to select all rows from the Tracks table
query = "SELECT * FROM genres;"

# Execute the query and load the results into a DataFrame
genres_df = pd.read_sql(query, conn)

# Print the contents of the Tracks table
print(genres_df)

# Close the connection
conn.close()