#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute( 'UPDATE standings SET wins = 0, matches = 0')
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute( 'DELETE FROM standings *')
    cursor.execute( 'DELETE FROM players *')
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    cursor.execute( 'SELECT count(*) FROM players')
    count = cursor.fetchone()[0]
    db.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute( 'INSERT INTO players (name) '
                    'VALUES(%s)', (name,))
    cursor.execute( 'INSERT INTO standings (id_num) '
                    'SELECT players.id_num '
                    'FROM players '
                    'WHERE players.name = (%s)', (name,))
    db.commit()
    db.close()
    
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute( 'SELECT * FROM swissPairings')
    standings = cursor.fetchall()
    db.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute( 'UPDATE standings '
                    'SET wins = wins + 1, '
                    'matches = matches + 1 '
                    'WHERE id_num = (%s)', (winner,))
    cursor.execute( 'UPDATE standings '
                    'SET matches = matches + 1 '
                    'WHERE id_num = (%s)', (loser,))
    db.commit()
    db.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute( 'SELECT a.id_num, a.name, b.id_num, b.name '
                    'FROM swissPairings AS a, swissPairings AS b '
                    'WHERE a.wins = b.wins '
                    'AND a.id_num > b.id_num')
    swissPairings = cursor.fetchall()
    db.close()
    return swissPairings
