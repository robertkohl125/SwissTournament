-- Table definitions for the tournament project.
--
--
--Checks for preexisting tournament database and clears it if found.

DROP DATABASE IF EXISTS tournament;

--Creates fresh database.

CREATE DATABASE tournament;

\c tournament;

--Creates table 'players' to contain id's and names of players.

CREATE TABLE players (
	id_num 	SERIAL PRIMARY KEY,
	name 	TEXT);

--Creates table standings to contain id's, wins and matches for players.

CREATE TABLE standings (
    id_num  SERIAL REFERENCES players(id_num) PRIMARY KEY,
    wins    INT DEFAULT 0,
    matches INT DEFAULT 0);

--Created a view of players rankings.

CREATE VIEW swissPairings (id_num, name, wins, matches) AS 
    SELECT  players.id_num, 
            players.name, 
            standings.wins,     
            standings.matches
    FROM players RIGHT JOIN standings ON 
            players.id_num = standings.id_num 
        WHERE standings.wins IS NOT NULL 
    ORDER BY wins DESC;