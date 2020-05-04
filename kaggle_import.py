import cx_Oracle
import csv

connection = cx_Oracle.connect("SulJis", "password")

cursor = connection.cursor()

csv_data = dict()

with open('dataanime.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for header in headers:
        csv_data[header]=None
    reader = list(reader)
    for i in range (0, len(reader)):
        for j in range(0, len(reader[i])):
            if csv_data[headers[j]] == None:
                csv_data[headers[j]] = {i : None}
            csv_data[headers[j]][i] = reader[i][j]

ratings = []
genres = []
studios = []

for i in range (0, len(csv_data["Title"])):
    title = csv_data["Title"][i].strip().encode("ascii", "replace").decode("utf-8", "ignore")
    cursor.execute("INSERT INTO Animes(title) VALUES (q'[{}]')".format(title))

    rating = csv_data["Rating"][i].strip()
    if rating != "None" and rating != "-":
        if not rating in ratings:
            ratings.append(csv_data["Rating"][i])
            cursor.execute("INSERT INTO Ratings(rating) VALUES('{}')".format(rating))
        cursor.execute("INSERT INTO RatingsAnimes(animeId, rating) VALUES({}, q'[{}]')".format(i+1, rating))

    episodes = csv_data["Episodes"][i]
    score = csv_data["Score"][i]


    if episodes != "None" and episodes != "-":
        cursor.execute("INSERT INTO Episodes(animeId, episodesNumber) VALUES ('{}', '{}')".format(i + 1, episodes))

    if score != "None" and score != "-":
        cursor.execute("INSERT INTO Scores(animeId, score) VALUES ('{}', '{}')".format(i + 1, score))

    currentGenres = csv_data["Genres"][i].split(",")
    for genre in currentGenres:
        genre = genre.strip()
        if genre != "None" and genre != "-":
            if not genre in genres:
                genres.append(genre)
                cursor.execute("INSERT INTO Genres(genre) VALUES(q'[{}]')".format(genre))
            cursor.execute("INSERT INTO GenresAnimes(animeId, genre) VALUES({}, q'[{}]')".format(i + 1, genre))

    currentStudios = csv_data["Studios"][i].split(",")
    for studio in currentStudios:
        studio = studio.strip().encode("ascii", "replace").decode("ascii", "ignore")
        if (studio != "None" and studio != "-"):
            if (not studio in studios):
                studios.append(studio)
                cursor.execute("INSERT INTO Studios(studio) VALUES(q'[{}]')".format(studio))
            cursor.execute("INSERT INTO StudiosAnimes(animeId, studio) VALUES({}, q'[{}]')".format(i + 1, studio))

cursor.close()
connection.commit()
connection.close()
