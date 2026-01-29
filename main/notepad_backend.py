import sqlite3
from datetime import datetime
db_name="Notepad.db"
def database():
    return sqlite3.connect(db_name)
def create_db():
    conn=database()
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            note TEXT NOT NULL,
            modified TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS app_state (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    conn.commit()
    conn.close()
def new_note(title):
    conn = database()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (title, note, modified) VALUES (?, ?, datetime('now', 'localtime'))",
        (title, "",)
    )
    note_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return note_id
def set_app_state(key, value):
    conn = database()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO app_state (key, value) VALUES (?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        (key, str(value))
    )
    conn.commit()
    conn.close()


def get_app_state(key):
    conn = database()
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM app_state WHERE key = ?", (key,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
