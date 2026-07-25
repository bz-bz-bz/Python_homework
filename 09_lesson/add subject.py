from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:2502@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "INSERT INTO subject "
        "(subject_id,subject_title) VALUES (:new_id, :new_name)")
    connection.execute(sql, {"new_id": 16, "new_name": "Astronomy"})

    transaction.commit()
    connection.close()


test_insert()
