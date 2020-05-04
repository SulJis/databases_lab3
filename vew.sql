CREATE OR REPLACE VIEW Animes_ratings_episodes_scores AS
SELECT animeId,
       Animes.title,
       RatingsAnimes.rating,
       Episodes.episodesNumber,
       Scores.score
FROM
Animes
LEFT JOIN RatingsAnimes
USING (animeId)
LEFT JOIN Episodes
USING (animeId)
LEFT JOIN Scores
USING (animeId);
