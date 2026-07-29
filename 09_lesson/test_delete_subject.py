from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:2502@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "INSERT INTO subject (subject_id,subject_title)"
        "VALUES (:new_id, :new_name)"
    )
    connection.execute(sql, {"new_id": 16, "new_name": "Astronomy"})
    delete_sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(delete_sql, {"id": 16})
    select_sql = text(
        "SELECT subject_title FROM subject"
        "WHERE subject_id = :id")
    result = connection.execute(select_sql, {"id": 16}).scalar()
    assert result is None
    transaction.commit()
    connection.close()
