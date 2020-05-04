DECLARE
    rows NUMBER(2) := 3;
    TYPE Titles IS VARRAY(3) OF VARCHAR2(100 CHAR);
    TYPE Studios IS VARRAY(3) OF VARCHAR2(50 CHAR);
    titles_arr Titles := Titles('Fullmetal Alchemist', 'Bakuman', 'Steel Ball Run');
    studios_arr Studios := Studios('Gainax', 'Toei Animation', 'David Production');
BEGIN

    FOR i in 1..rows LOOP
        INSERT INTO Animes(title)
        VALUES (titles_arr(i));

        INSERT INTO Studios(studio)
        VALUES(studios_arr(i));

        INSERT INTO StudiosAnimes(animeId, studio)
        VALUES (i, studios_arr(i));
    END LOOP;
END;
