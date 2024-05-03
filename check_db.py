import pymysql


def create_user(user_login, password):
    try:
        connection = pymysql.connect(
            host="server14.hosting.reg.ru",
            port=3306,
            user="u2559429_admin",
            password="Efim0909.",
            database="u2559429_efim",
            cursorclass=pymysql.cursors.DictCursor,
        )

        try:
            # Insert data into table
            with connection.cursor() as cursor:
                insert_query = f"INSERT INTO `user_data`(login, password) VALUES ('{user_login}', '{password}');"
                cursor.execute(insert_query)
                connection.commit()
        finally:
            connection.close()

    except Exception as ex:
        print("Connection error")
        print(ex)


def check_user(user_login, password):
    try:
        connection = pymysql.connect(
            host="server14.hosting.reg.ru",
            port=3306,
            user="u2559429_admin",
            password="Efim0909.",
            database="u2559429_efim",
            cursorclass=pymysql.cursors.DictCursor,
        )

        try:
            # Insert data into table
            with connection.cursor() as cursor:
                insert_query = f"SELECT * FROM `user_data` WHERE login = '{user_login}' AND password = '{password}';"
                cursor.execute(insert_query)
                connection.commit()
                result = cursor.fetchall()
                result = str(result)
                if result != "()":
                    return True
                else:
                    return False

        finally:
            connection.close()

    except Exception as ex:
        print("Connection error")
        print(ex)


def get_data_user(user_login):
    try:
        connection = pymysql.connect(
            host="server14.hosting.reg.ru",
            port=3306,
            user="u2559429_admin",
            password="Efim0909.",
            database="u2559429_efim",
            cursorclass=pymysql.cursors.DictCursor,
        )

        try:
            # Insert data into table
            with connection.cursor() as cursor:
                insert_query = f"SELECT * FROM student WHERE login = '{user_login}';"
                cursor.execute(insert_query)
                connection.commit()
                result = cursor.fetchall()
                data = str(result)
                for i in ["[", "]", "{", "}"]:
                    data = data.replace(i, "")
                    data = data.replace(" ", "")
                data = data.replace("'", "")
                data = data.replace(",", " ")
                data = data.replace(":", " ")
                data = data.split(" ")
                return data

        finally:
            connection.close()

    except Exception as ex:
        print("Connection error")
        print(ex)


def change_transcript(user_login, transcript):
    try:
        connection = pymysql.connect(
            host="server14.hosting.reg.ru",
            port=3306,
            user="u2559429_admin",
            password="Efim0909.",
            database="u2559429_efim",
            cursorclass=pymysql.cursors.DictCursor,
        )

        try:
            # Insert data into table
            with connection.cursor() as cursor:
                update_query = f"UPDATE `student` SET transcript = '{transcript}' WHERE login = '{user_login}'"
                cursor.execute(update_query)
                connection.commit()
        finally:
            connection.close()

    except Exception as ex:
        print("Connection error")
        print(ex)


def create_table():
    try:
        connection = pymysql.connect(
            host="server14.hosting.reg.ru",
            port=3306,
            user="u2559429_admin",
            password="Efim0909.",
            database="u2559429_efim",
            cursorclass=pymysql.cursors.DictCursor,
        )
        cursor = connection.cursor()
        try:
            insert_query_table_group = """
                CREATE TABLE IF NOT EXISTS GROUPS(
                    group_id INT AUTO_INCREMENT PRIMARY KEY,
                    name_group varchar(32),
                    year int,
                    course int
                )         
            """
            insert_query_table_disc = """
            CREATE TABLE IF NOT EXISTS Disciplines(
                disc_id int AUTO_INCREMENT PRIMARY KEY,
                name_disc varchar(32),
                name_group varchar(32),
                group_year int,
                FOREIGN KEY(name_group)  REFERENCES GROUPS(name_group),
                FOREIGN KEY(group_year)  REFERENCES GROUPS(year)
            )                    
            """

            insert_query_table_ac = """
            CREATE TABLE IF NOT EXISTS AC_Performance(
                    transcript INT PRIMARY KEY,
                     name_disc varchar(32) NOT NULL,
                      result int,
                       FOREIGN KEY (transcript) REFERENCES student(transcript),
                       FOREIGN KEY (name_disc) REFERENCES DISCIPLINES(name_disc)
                                      )
                                      """
            cursor.execute(insert_query_table_group)
            cursor.execute(insert_query_table_disc)
            cursor.execute(insert_query_table_ac)
            connection.commit()
            cursor.close()
        finally:
            connection.close()

    except Exception as ex:
        print("Connection error")
        print(ex)
