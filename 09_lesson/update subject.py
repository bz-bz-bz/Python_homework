from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:2502@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "UPDATE subject SET "
        "subject_title = :updated_st WHERE subject_id = :id")
    connection.execute(sql, {"updated_st": "updated title", "id": 16})

    transaction.commit()
    connection.close()


test_update()
