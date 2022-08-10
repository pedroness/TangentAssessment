import sqlite3


class LeaveApplications:
    def __init__(self):
        self.con = sqlite3.connect("leaveapp.db",check_same_thread=False)
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        # self.cur.execute("""DROP TABLE leave""")#
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS leave(
        employee_pk TEXT,
        start_date DATE,
        end_date DATE,
        days_of_leave INTEGER,
        status TEXT NOT NULL DEFAULT 'New'
        )"""
        )

    def insert(self, leave):
        self.cur.execute(
            """INSERT OR IGNORE INTO leave """ """VALUES(?,?,?,?,?)""", leave
        )
        self.con.commit()

    def read(self):
        self.cur.execute("""SELECT * FROM leave""")
        rows = self.cur.fetchall()
        return rows


class Employees:
    def __init__(self):
        self.con = sqlite3.connect("db/leaveapp.db",check_same_thread=False)
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        # self.cur.execute("""DROP TABLE employees""")#
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS employees(
        emp_number TEXT PRIMARY KEY,
        phone_number TEXT,
        first_name TEXT,
        last_name TEXT
        )"""
        )

    def insert(self, employee):
        self.cur.execute(
            """INSERT OR IGNORE INTO employees VALUES(?,?,?,?)""", employee
        )
        self.con.commit()

    def read(self):
        self.cur.execute("""SELECT * FROM employees""")
        rows = self.cur.fetchall()
        return rows
