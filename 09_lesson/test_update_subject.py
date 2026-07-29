from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:2502@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    insert_sql = text(
        "INSERT INTO subject (subject_id,subject_title)"
        "VALUES (:new_id, :new_name)"
    )
    connection.execute(insert_sql, {"new_id": 16, "new_name": "Astronomy"})
    sql = text(
        "UPDATE subject SET subject_title = :updated_st"
        "WHERE subject_id = :id")
    connection.execute(sql, {"updated_st": "updated title", "id": 16})
    select_sql = text(
        "SELECT subject_title FROM subject"
        "WHERE subject_id = :id")
    result = connection.execute(select_sql, {"id": 16}).scalar()
    assert result == "updated title"
    transaction.commit()
    connection.close()
