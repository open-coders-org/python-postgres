import psycopg2


def db():
    connection = psycopg2.connect(
        user="postgres",
        password="root",
        host="localhost",
        port="5432",
        database="hospital",
    )
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM doctor')
    rows = cursor.fetchall()
    print(rows)
    """
    return connection
