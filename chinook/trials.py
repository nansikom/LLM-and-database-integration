import sqlite3
import pandas as pd
## creating a connection
database = 'chinook.db'
#database = 'chinook.db'
conn = sqlite3.connect(database)
## importing tables
tables = pd.read_sql("""SELECT name, type
 FROM sqlite_master
 WHERE type IN ("table", "view");""", conn)

print(tables)
import matplotlib.pyplot as plt
# Define the SQL query
sql = """
SELECT g.Name AS Genre, COUNT(t.TrackId ) AS Tracks
FROM genres g
JOIN tracks t ON g.GenreId = t.GenreId
GROUP BY Genre
ORDER BY Tracks DESC;
"""
# Read the data into a dataframe
data = pd.read_sql(sql, conn)
plt.bar(data.Genre, data.Tracks)
plt.title("Number of Tracks by Genre")
plt.xlabel("Genre")
plt.ylabel("Tracks")
plt.xticks(rotation=90)
plt.show()