from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:2502@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(sql, {"id": 16})

    transaction.commit()
    connection.close()


test_delete()
