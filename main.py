from fastapi import FastAPI, Query, Path,Body,Depends
from schemas import Student
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
app = FastAPI()
origins = [""]


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_CRED = {
    "dbname": "postgres",
    "dbuser": "postgres",
    "dbpassword": "3216777VASHJJ900",
    "dbhost": "localhost"
}

con = psycopg2.connect(dbname=DB_CRED['dbname'], user=DB_CRED['dbuser'],password=DB_CRED['dbpassword'], host=DB_CRED['dbhost'])
cursor = con.cursor()

# @app.options('/get_by_student_id',status_code=200)
# def create_student_options(item: Student):
#     return "родили"


@app.post('/create_student',status_code=200)
def create_student(item: Student):
    cursor.execute(f"""INSERT INTO student( familia, imia, otchestvo, birthdate) 
                    VALUES ('{item.familia}','{item.imia}','{item.otchestvo}','{item.birthdate}')""")
    con.commit()
    return "родили"

@app.get('/get_all_student')
def get_all_students():
    cursor.execute("SELECT * FROM student")
    fet = cursor.fetchall()
    output_List = []
    for student in fet:
        output_List.append({'id':student[0],'familia':student[1],'imia':student[2],'otchestvo':student[3], 'birthdate':student[4]})
    return output_List


@app.get("/get_by_student_{id}")
def get_by_student_id(id):
    cursor.execute(f"SELECT * FROM student WHERE id = {id}")
    fet = cursor.fetchall()
    if len(fet)>0 :
        return {'familia':fet[0][1],'imia':fet[0][2],'otchestvo':fet[0][3],'birthdate':fet[0][4]}
    else:
        return "ничего"
    
@app.get("/is_over_18")
def is_over_18_():
    cursor.execute(f"SELECT * FROM student WHERE birthdate<'2005-07-17'")
    fet = cursor.fetchall()
    output_List = []
    for student in fet:
        output_List.append({'id':student[0],'familia':student[1],'imia':student[2],'otchestvo':student[3], 'birthdate':student[4]})
    return output_List

@app.put("/Change_info_{id}")
def Change_info(item: Student,id):
    cursor.execute(f"UPDATE student SET familia = '{item.familia}'WHERE id = {id}")
    con.commit()
    return "готово"

@app.get("/imia_get_{imia}")
def is_over_18_(imia):
    cursor.execute(f"SELECT * FROM student WHERE imia='{imia}'")
    fet = cursor.fetchall()
    output_List = []
    for student in fet:
        output_List.append({'id':student[0],'familia':student[1],'imia':student[2],'otchestvo':student[3], 'birthdate':student[4]})
    return output_List