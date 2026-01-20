from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT COUNT(b.id)
                FROM artist a, album b
                WHERE a.id =b.artist_id 
             """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_node(n_alb):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT a.id,
                FROM artist a, album b
                WHERE a.id = b.artist_id
                GROUP BY a.id
                HAVING COUNT(b.id) >= %s
                """
        cursor.execute(query, (n_alb,))
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    def get_all_edges():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT LEAST(a1.id, a2.id) AS a1
                            GREATEST (a1.id, a2.id) AS a2, COUNT(*) AS peso
                            FROM artist a1, artist a2, album b, track , genre g 
                             WHERE a1.id != a2.id AND a1.id = b.artist_id AND a2.id = b.artist_id AND t.album_id = b.id AND g.id = t.genre_id
                            GROUP BY a1.id, a2.id"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['a1'], row['a2'], row['peso'])
        cursor.close()
        conn.close()
        return result
