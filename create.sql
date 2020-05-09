CREATE TABLE animes (
    animeid  NUMBER(5) NOT NULL,
    title    VARCHAR2(100 CHAR)
);

ALTER TABLE animes ADD CONSTRAINT animes_pk PRIMARY KEY ( animeid );

CREATE TABLE episodes (
    animeId  NUMBER(5) NOT NULL,
    episodesNumber  NUMBER(5)
);

ALTER TABLE episodes ADD CONSTRAINT episodes_pk PRIMARY KEY ( animeid );

CREATE TABLE genres (
    genre VARCHAR2(20 CHAR) NOT NULL
);

ALTER TABLE genres ADD CONSTRAINT genres_pk PRIMARY KEY ( genre );

CREATE TABLE genresanimes (
    animeId  NUMBER(5) NOT NULL,
    genre    VARCHAR2(20 CHAR) NOT NULL
);

ALTER TABLE genresanimes ADD CONSTRAINT genresanimes_pk PRIMARY KEY ( animeId, genre );

CREATE TABLE ratings (
    rating VARCHAR2(5 CHAR) NOT NULL
);

ALTER TABLE ratings ADD CONSTRAINT ratings_pk PRIMARY KEY ( rating );

CREATE TABLE ratingsanimes (
    animeId  NUMBER(5) NOT NULL,
    rating  VARCHAR2(5 CHAR) NOT NULL
);

ALTER TABLE ratingsanimes ADD CONSTRAINT ratingsanimes_pk PRIMARY KEY ( animeId, rating);

CREATE TABLE scores (
    animeId  NUMBER(5) NOT NULL,
    score           NUMBER(4, 2)
);

ALTER TABLE scores ADD CONSTRAINT scores_pk PRIMARY KEY ( animeId );

CREATE TABLE studios (
    studio VARCHAR2(50 CHAR) NOT NULL
);

ALTER TABLE studios ADD CONSTRAINT studios_pk PRIMARY KEY ( studio );

CREATE TABLE studiosanimes (
    animeId  NUMBER(5) NOT NULL,
    studio  VARCHAR2(50 CHAR) NOT NULL
);

ALTER TABLE studiosanimes ADD CONSTRAINT studiosanimes_pk PRIMARY KEY ( animeId, studio);


ALTER TABLE episodes
    ADD CONSTRAINT episodes_animes_fk FOREIGN KEY ( animeId )
        REFERENCES animes ( animeId );

ALTER TABLE genresanimes
    ADD CONSTRAINT genresanimes_animes_fk FOREIGN KEY ( animeId )
        REFERENCES animes ( animeId );

ALTER TABLE genresanimes
    ADD CONSTRAINT genresanimes_genres_fk FOREIGN KEY ( genre )
        REFERENCES genres ( genre );

ALTER TABLE ratingsanimes
    ADD CONSTRAINT ratingsanimes_animes_fk FOREIGN KEY ( animeid )
        REFERENCES animes ( animeid );

ALTER TABLE ratingsanimes
    ADD CONSTRAINT ratingsanimes_ratings_fk FOREIGN KEY ( rating )
        REFERENCES ratings ( rating );

ALTER TABLE scores
    ADD CONSTRAINT scores_animes_fk FOREIGN KEY ( animeid )
        REFERENCES animes ( animeid );

ALTER TABLE studiosanimes
    ADD CONSTRAINT studiosanimes_animes_fk FOREIGN KEY ( animeid )
        REFERENCES animes ( animeid );

ALTER TABLE studiosanimes
    ADD CONSTRAINT studiosanimes_studios_fk FOREIGN KEY ( studio )
        REFERENCES studios ( studio );


CREATE SEQUENCE animeSequence;

CREATE OR REPLACE TRIGGER animes_on_insert
  BEFORE INSERT ON Animes
  FOR EACH ROW
BEGIN
  SELECT animeSequence.nextval
  INTO :new.animeId
  FROM dual;
END;
