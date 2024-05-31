import pymysql
import requests
from config import Config
from bs4 import BeautifulSoup


def init_db():
    try:
        connection = pymysql.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Connected to MySQL database")
        return connection
    except pymysql.Error as e:
        print("Error connecting to MySQL database:", e)


connection = init_db()


def check_student(email, psw, bcrypt):
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT *
                FROM Student
                WHERE email = %s
            """
            cursor.execute(sql, email)
            user = cursor.fetchone()
            if bcrypt.check_password_hash(user["password"], psw):
                return user
            return None
    except pymysql.Error as e:
        print("Error retrieving user:", e)


def update_student(first_name, last_name, email):
    try:
        with connection.cursor() as cursor:
            sql = """
                UPDATE Student
                SET first_name = %s, last_name = %s
                WHERE email = %s
            """
            cursor.execute(sql, (first_name, last_name, email))
            connection.commit()
    except pymysql.Error as e:
        print("Error updating user:", e)


def show_grade(id):
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT d.name, g.grade
                FROM Grade g
                JOIN Disciplines d ON g.disciplines_id = d.id
                WHERE g.student_id = %s;
            """
            cursor.execute(sql, (id))
            results = cursor.fetchall()
            return results
    except pymysql.Error as e:
        print("Error retrieving user:", e)


def show_group(id):
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT speciality FROM SGroup WHERE id=%s;
            """
            cursor.execute(sql, (id))
            results = cursor.fetchone()
            ans = results["speciality"]
            return ans
    except pymysql.Error as e:
        print("Error retrieving user:", e)


def show_schedule(id):
    url = (
        "https://old.tyuiu.ru/shedule_new/bin/groups.py?act=show&print=&sgroup=%s" % id
    )
    html_content = requests.get(url).text
    return html_content


def show_assignment(id):
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT d.name ,a.description, a.grade, a.max_grade, a.is_completed
                FROM Student s
                JOIN Assignments a ON s.id = a.student_id
                JOIN Disciplines d ON a.discipline_id = d.id
                WHERE s.id = %s;
            """
            cursor.execute(sql, (id))
            results = cursor.fetchall()
            return results
    except pymysql.Error as e:
        print("Error retrieving user:", e)


def update_grade(student_id, disciplines_id, grade):
    try:
        with connection.cursor() as cursor:
            sql = """
                UPDATE Grade
                inner join Assignments on Grade.disciplines_id = Assignments.discipline_id and Grade.student_id = Assignments.student_id
                set Grade.grade=(select sum(Assignments.grade) from  Assignments where  Assignments.discipline_id = Grade.disciplines_id and Assignments.student_id = Grade.student_id)
            """
            cursor.execute(sql, (student_id, disciplines_id, grade))
            connection.commit()
    except pymysql.Error as e:
        print("Error updating user:", e)
