import cx_Oracle
import csv

connection = cx_Oracle.connect("SulJis", "password")

cursor = connection.cursor()

tables = ["Animes", "Genres", "Studios", "Ratings", "Episodes", "Scores", "GenresAnimes", "StudiosAnimes", "RatingsAnimes"]

for table in tables:
    file = table + ".csv"
    query = "SELECT * FROM {}".format(table)
    cursor.execute(query)
    with open(file, "w", encoding = "utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter = ",")
        row = cursor.fetchone()
        while row != None:
            writer.writerow(list(row))
            row = cursor.fetchone()
cursor.close()
connection.commit()
connection.close()
