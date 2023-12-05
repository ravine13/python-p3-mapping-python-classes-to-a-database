from config import CONN, CURSOR

class Song:
    all = []

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)

    @classmethod
    def create(cls, name, album):
        sql = """
            INSERT INTO songs(name, album)
            VALUES(?, ?)
        """
        CURSOR.execute(sql, (name, album))
        CONN.commit()
        song = cls(name, album)
        song.id = CURSOR.lastrowid
        return song
    
    def save(self):
        sql = """
            INSERT INTO songs(name, album)
            VALUES(?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def new_from_db(cls,row):
        song = cls(row[1],row[2])
        song.id = row[0]

    @classmethod
    def all(cls):
        sql = """
            SELECT *
            FROM songs
        """

        all = CURSOR.execute(sql).fetchall()
        cls.all = [cls.new_from_db(row) for row in all]