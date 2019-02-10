import datetime
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db_time.db")

# Функция переконфигурирования БД
def RecrateTable():
    # Подключение к БД
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Удаление уже созданных таблиц
    cursor.execute("DROP TABLE IF EXISTS Monday1")
    cursor.execute("DROP TABLE IF EXISTS Monday2")
    cursor.execute("DROP TABLE IF EXISTS Tuesday1")
    cursor.execute("DROP TABLE IF EXISTS Tuesday2")
    cursor.execute("DROP TABLE IF EXISTS Wednesday1")
    cursor.execute("DROP TABLE IF EXISTS Wednesday2")
    cursor.execute("DROP TABLE IF EXISTS Thursday1")
    cursor.execute("DROP TABLE IF EXISTS Thursday2")
    cursor.execute("DROP TABLE IF EXISTS Friday1")
    cursor.execute("DROP TABLE IF EXISTS Friday2")
    # Создание таблицы
    cursor.execute("""create table Monday1(
                      Subject       String,
                      Teacher       String,
                      Room          String,
                      Start_clock   int,
                      Start_minutes int)""")
    cursor.execute("""create table Monday2(
                          Subject       String,
                          Teacher       String,
                          Room          String,
                          Start_clock   int,
                          Start_minutes int)""")
    cursor.execute("""create table Tuesday1(
                          Subject       String,
                          Teacher       String,
                          Room          String,
                          Start_clock   int,
                          Start_minutes int)""")
    cursor.execute("""create table Tuesday2(
                          Subject       String,
                          Teacher       String,
                          Room          String,
                          Start_clock   int,
                          Start_minutes int)""")
    cursor.execute("""create table Wednesday1(
                          Subject       String,
                          Teacher       String,
                          Room          String,
                          Start_clock   int,
                          Start_minutes int)""")
    cursor.execute("""create table Wednesday2(
                          Subject       String,
                          Teacher       String,
                          Room          String,
                          Start_clock   int,
                          Start_minutes int)""")
    cursor.execute("""create table Thursday1(
                          Subject       String,
                          Teacher       String,
                          Room          String,
                          Start_clock   int,
                          Start_minutes int)""")
    cursor.execute("""create table Thursday2(
                          Subject       String,
                          Teacher       String,
                          Room          String,
                          Start_clock   int,
                          Start_minutes int)""")
    cursor.execute("""create table Friday1(
                          Subject       String,
                          Teacher       String,
                          Room          String,
                          Start_clock   int,
                          Start_minutes int)""")
    cursor.execute("""create table Friday2(
                          Subject       String,
                          Teacher       String,
                          Room          String,
                          Start_clock   int,
                          Start_minutes int)""")
    # Создание массивов данных
    Monday1 = [('CУБД, лекция', 'Голдовский', '1329', 13, 50),
               ('Техническая защита информации, лекция', 'Голдовский', '1329', 15, 20),
               ('Основы управленческой деятельностью, лекция', 'Федорова', '1527', 16, 50),
               ('ЭВМ, лб', 'Шамров', '1326', 18, 20)]
    Monday2 = [('CУБД, лекция', 'Голдовский', '1329', 13, 50),
               ('ЭВМ, пр', 'Шамров', '1326', 15, 20),
               ('Основы управленческой деятельностью, пр', 'Федорова', '1527', 16, 50),
               ('ЭВМ, лб', 'Шамров', '1326', 18, 20)]
    Tuesday1 = Tuesday2 = [('Сети, лекция', 'Желенков', '5306', 12, 00),
                           ('Техническая защита информации, лб', 'Голдовский', '1330', 13, 50),
                           ('Сети, лб', 'Адская комба', '1327', 15, 20)]
    Wednesday1 = Wednesday2 = [('CУБД, лб', 'Голдовский', '1330', 15, 20),
                               ('Системное администрирование', 'Ларина', '1329', 16, 50),
                               ('Системное администрирование', 'Ларина', '1329', 18, 20)]
    Thursday1 = Thursday2 = [('ЭВМ, лб', 'Шамров', '1326', 10, 30),
                             ('ЭВМ, лекция', 'Шамров', '1329', 12, 00)]
    Friday1 = [('Крипта, лк', 'Семенов', '1319', 13, 50),
               ('Крипта, пр', 'Семенов', '1319', 15, 20),
               ('Правоведение, лекция', 'Зарубина', '1340', 16, 50)]
    Friday2 = [('Крипта, лк', 'Семенов', '1319', 13, 50),
               ('Крипта, пр', 'Семенов', '1319', 15, 20),
               ('Правоведение, пр', 'Зарубина', '1340', 16, 50)]
    # Вставка данных в БД
    conn.commit()
    cursor.executemany("INSERT INTO Monday1 VALUES (?,?,?,?,?)", Monday1)
    cursor.executemany("INSERT INTO Monday2 VALUES (?,?,?,?,?)", Monday2)
    cursor.executemany("INSERT INTO Tuesday1 VALUES (?,?,?,?,?)", Tuesday1)
    cursor.executemany("INSERT INTO Tuesday2 VALUES (?,?,?,?,?)", Tuesday2)
    cursor.executemany("INSERT INTO Wednesday1 VALUES (?,?,?,?,?)", Wednesday1)
    cursor.executemany("INSERT INTO Wednesday2 VALUES (?,?,?,?,?)", Wednesday2)
    cursor.executemany("INSERT INTO Thursday1 VALUES (?,?,?,?,?)", Thursday1)
    cursor.executemany("INSERT INTO Thursday2 VALUES (?,?,?,?,?)", Thursday2)
    cursor.executemany("INSERT INTO Friday1 VALUES (?,?,?,?,?)", Friday1)
    cursor.executemany("INSERT INTO Friday2 VALUES (?,?,?,?,?)", Friday2)
    conn.commit()
    conn.close()


def getThisDayTable():
    day_mass = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "No", "No"]
    day_str = day_mass[datetime.datetime.today().weekday()]
    if day_str is "No":
        return []
    wk = datetime.datetime.today().strftime("%V")
    even = str(int(wk) % 2 + 1)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM "+day_str + even)
    mysel = cursor.execute("SELECT * FROM "+day_str + even)
    rows = cursor.fetchall()
    mass_day = []
    for row in rows:
        mass_day.append(row)
    conn.close()
    return mass_day


if __name__ == '__main__':
    # RecrateTable()
    print(getThisDayTable())
