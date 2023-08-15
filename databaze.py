import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS transports (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, capacity FLOAT, length FLOAT,\
             width FLOAT, height FLOAT, available INTEGER)")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS limitations (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, capacitymin FLOAT, capacitymax \
            FLOAT, lengthmin FLOAT, lengthmax FLOAT, widthmin FLOAT, widthmax FLOAT, heightmin FLOAT, heightmax FLOAT)")
        self.connection.commit()

    def add_transport(self, name, capacity, length, width, height, available):
        self.cursor.execute(
            'INSERT INTO transports (name, capacity, length, width, height, available) VALUES (?, ?, ?, ?, ?, ?)',
            (name, capacity, length, width, height, available))
        self.connection.commit()

    def add_limitation(self, name, capacitymin, capacitymax, lengthmin, lengthmax, widthmin, widthmax, heightmin,
                       heightmax):
        self.cursor.execute(
            'INSERT INTO limitations (name, capacitymin, capacitymax, lengthmin, lengthmax, widthmin, widthmax, heightmin, heightmax) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)',
            (name, capacitymin, capacitymax, lengthmin, lengthmax, widthmin, widthmax, heightmin, heightmax))
        self.connection.commit()

    def get_limitations_by_name(self, name):
        self.cursor.execute('SELECT * FROM limitations WHERE name = ?', (name,))
        return self.cursor.fetchone()[2:]

    def get_transports(self):
        self.cursor.execute("SELECT * FROM transports")
        return self.cursor.fetchall()

    def delete_transport(self, dev_id):
        self.cursor.execute("DELETE FROM transports WHERE id=?", (dev_id,))
        self.connection.commit()

    def mark_transport_unavailable(self, dev_id):
        self.cursor.execute("UPDATE transports SET available = 0 WHERE id=?", (dev_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()
