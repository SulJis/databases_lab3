import cx_Oracle
import chart_studio.plotly as py
import plotly.graph_objs as go
connection = cx_Oracle.connect("SulJis", "password")

cursor = connection.cursor()

query_genres = \
"""
SELECT genre, COUNT(animeId) as total
FROM animes_ratings_episodes_scores
INNER JOIN GenresAnimes
USING(animeId)
GROUP BY genre
ORDER BY total DESC
"""
query_ratings = \
"""
SELECT rating, ROUND(
                    (COUNT(rating)/(
                        SELECT COUNT(AnimeId)
                        FROM Animes
                        ))*100) as percent
FROM
animes_ratings_episodes_scores
GROUP BY rating
HAVING 
RATING IS NOT NULL
"""

query_studios = \
"""
SELECT studio, TRUNC(AVG(score), 2) as AverageScore
FROM animes_ratings_episodes_scores
INNER JOIN StudiosAnimes
USING(animeId)
GROUP BY studio
order by AverageScore DESC
"""

cursor.execute(query_genres)
query_genres_result = cursor.fetchall()
genres = []
genres_count = []

for row in query_genres_result:
    genres.append(row[0])
    genres_count.append(row[1])

genresData = [go.Bar(
    x = genres,
    y = genres_count
)]

genresLayout = go.Layout(
    title='Genres and animes',
    xaxis=dict(
        title='Genres',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Number of animes',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

genresBar = go.Figure(data = genresData, layout=genresLayout)
html = py.plot(genresBar, filename = "genres.html")

cursor.execute(query_ratings)
queryRatingsResult = cursor.fetchall()

ratings = []
percents = []

for row in queryRatingsResult:
    ratings.append(row[0])
    percents.append(row[1])

ratingsData = [go.Pie(
    labels = ratings,
    values = percents)]

ratingsPie = go.Figure(data = ratingsData)
ratingsPercents = py.plot(ratingsPie, filename = "ratingsPie")

cursor.execute(query_studios)
queryStudiosResult = cursor.fetchall()
studios = []
score = []
for row in queryStudiosResult:
    studios.append(row[0])
    score.append(row[1])

studiosData = [go.Bar(
    x = studios,
    y = score
)]

studiosLayout = go.Layout(
    title='Studios and average score',
    xaxis=dict(
        title='Studios',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Average score',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

studiosBar = go.Figure(data = studiosData, layout=studiosLayout)

studiosAvgScores = py.plot(studiosBar, filename='studiosBar')

cursor.close()
connection.close()
