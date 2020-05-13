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
    cursor.execute("INSERT INTO Animes(title) VALUES (:title)", title = title)

    rating = csv_data["Rating"][i].strip()
    if rating != "None" and rating != "-":
        if not rating in ratings:
            ratings.append(csv_data["Rating"][i])
            cursor.execute("INSERT INTO Ratings(rating) VALUES(:rating)", rating = rating)
        cursor.execute("INSERT INTO RatingsAnimes(animeId, rating) VALUES(:id, :rating)", id= i+1, rating = rating)

    episodes = csv_data["Episodes"][i].strip()
    score = csv_data["Score"][i].strip()


    if episodes != "None" and episodes != "-":
        cursor.execute("INSERT INTO Episodes(animeId, episodesNumber) VALUES (:id, :episodes)", id = i + 1, episodes = int(episodes))

    if score != "None" and score != "-":
        cursor.execute("INSERT INTO Scores(animeId, score) VALUES (:id, :score)", id = i + 1, score = float(score))

    currentGenres = csv_data["Genres"][i].split(",")
    for genre in currentGenres:
        genre = genre.strip()
        if genre != "None" and genre != "-":
            if not genre in genres:
                genres.append(genre)
                cursor.execute("INSERT INTO Genres(genre) VALUES(:genre)", genre = genre)
            cursor.execute("INSERT INTO GenresAnimes(animeId, genre) VALUES(:id, :genre)", id = i + 1, genre = genre)

    currentStudios = csv_data["Studios"][i].split(",")
    for studio in currentStudios:
        studio = studio.strip().encode("ascii", "replace").decode("ascii", "ignore")
        if (studio != "None" and studio != "-"):
            if (not studio in studios):
                studios.append(studio)
                cursor.execute("INSERT INTO Studios(studio) VALUES(:studio)", studio = studio)
            cursor.execute("INSERT INTO StudiosAnimes(animeId, studio) VALUES(:id, :studio)", id = i + 1, studio = studio)

cursor.close()
connection.commit()
connection.close()
