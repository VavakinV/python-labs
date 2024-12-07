import sqlite3

db_name = "transport.db"

def delete_record_by_id(table_name, field_name, record_id):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        query = f"DELETE FROM {table_name} WHERE {field_name} = ?"
        
        cursor.execute(query, (record_id,))

        connection.commit()

        if cursor.rowcount > 0:
            print(f"Запись с ID {record_id} успешно удалена из таблицы {table_name}.")
        else:
            print(f"Запись с ID {record_id} не найдена в таблице {table_name}.")

    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
    finally:
        connection.close()