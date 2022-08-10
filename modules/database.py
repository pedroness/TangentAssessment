import sqlite3


class LeaveApplications:
    def __init__(self):
        self.con = sqlite3.connect("db/leaveapp.db",check_same_thread=False)
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
        results=[]
        for val in rows:
            results.append({
                "employee_pk":str(val[0]),
                "start_date":str(val[1]),
                "end_date":str(val[2]),
                "days_of_leave":str(val[3]),
                "status":str(val[4])
            })
           
        return results


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

    def get_employee(self,employee_pk):
        self.cur.execute("""SELECT * FROM employees WHERE emp_number=?""",(employee_pk,))
        rows = self.cur.fetchall()
        return rows

    def read(self):
        self.cur.execute("""SELECT * FROM employees""")
        rows = self.cur.fetchall()
        results=[]
        for val in rows:
            results.append({
                "emp_number":str(val[0]),
                "phone_number":str(val[1]),
                "first_name":str(val[2]),
                "last_name":str(val[3])
            })
           
        return results
