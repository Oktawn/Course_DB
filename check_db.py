import pymysql

def create_user(user_login, password):
    try:
        connection = pymysql.connect(
            host = 'server14.hosting.reg.ru',
            port = 3306,
            user = 'u2559429_admin',
            password= 'Efim0909.',
            database= 'u2559429_efim',
            cursorclass= pymysql.cursors.DictCursor
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
        print('Connection error')
        print(ex)

def check_user(user_login, password):
    try:
        connection = pymysql.connect(
            host = 'server14.hosting.reg.ru',
            port = 3306,
            user = 'u2559429_admin',
            password= 'Efim0909.',
            database= 'u2559429_efim',
            cursorclass= pymysql.cursors.DictCursor
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
        print('Connection error')
        print(ex)

def get_data_user(user_login):
    try:
        connection = pymysql.connect(
            host = 'server14.hosting.reg.ru',
            port = 3306,
            user = 'u2559429_admin',
            password= 'Efim0909.',
            database= 'u2559429_efim',
            cursorclass= pymysql.cursors.DictCursor
        )

        try:
            # Insert data into table
            with connection.cursor() as cursor:
                insert_query = f"SELECT * FROM student WHERE login = '{user_login}';"
                cursor.execute(insert_query)
                connection.commit()
                result = cursor.fetchall()
                data = str(result)
                for i in ['[',']','{','}']:
                    data = data.replace(i,'')
                    data = data.replace(' ','')
                data = data.replace("'",'')
                data = data.replace(",",' ')
                data = data.replace(":",' ')
                data = data.split(' ')
                return data

        finally:
            connection.close()


    except Exception as ex:
        print('Connection error')
        print(ex)

def change_transcript(user_login, transcript):
    try:
        connection = pymysql.connect(
            host = 'server14.hosting.reg.ru',
            port = 3306,
            user = 'u2559429_admin',
            password= 'Efim0909.',
            database= 'u2559429_efim',
            cursorclass= pymysql.cursors.DictCursor
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
        print('Connection error')
        print(ex)

