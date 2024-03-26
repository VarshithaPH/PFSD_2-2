from flask import *

import psycopg2

app = Flask(__name__)
app.secret_key = "123"
conn = psycopg2.connect(
    database="pfsd1", user='postgres',
    password='postgres',
    host='127.0.0.1', port='5432'
)
cur = conn.cursor()


@app.route('/')
def welcome():
    cur.execute("SELECT * FROM STUDENT")
    students = cur.fetchall()
    return render_template('try1.html', students=students)


@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        regnum = request.form.get('regnum', type=int, default=0)
        name = request.form['name']
        subject1 = request.form['subject1']
        subject2 = request.form['subject2']
        cur.execute("INSERT INTO STUDENT (REGNUM,NAME,SUBJECT1,SUBJECT2) VALUES (%s,%s,%s,%s)",
                    (regnum, name, subject1, subject2))
        conn.commit()
        flash('Student Added successfully')
        return redirect(url_for('welcome'))


if __name__ == "__main__":
    app.run(debug=True)
