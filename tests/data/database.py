import sqlite3

from app.conf.database import get_test_db_url


def cursor():
    conn = sqlite3.connect(
        get_test_db_url().split('///')[1]
    )
    yield conn.cursor()
    conn.commit()
    conn.close()


def truncate():
    with cursor() as session:
        session.execute('DELETE FROM persons')
