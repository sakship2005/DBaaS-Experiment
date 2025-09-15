from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__, template_folder="../frontend")

# Database connection
def get_db_connection():
    conn = sqlite3.connect("elearning.db")
    conn.row_factory = sqlite3.Row
    return conn

# Home page
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Join tables to show student enrolments
    cursor.execute("""
        SELECT s.student_id, s.name AS student_name, s.email, s.enrollment_date,
               c.course_name, p.amount, p.payment_date
        FROM students s
        LEFT JOIN enrolments e ON s.student_id = e.student_id
        LEFT JOIN courses c ON e.course_id = c.course_id
        LEFT JOIN payments p ON s.student_id = p.student_id
    """)
    data = cursor.fetchall()

    # fetch courses for dropdowns
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    # fetch students for dropdowns
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()
    return render_template("index.html", students=data, all_courses=courses, all_students=students)

# Add a student
@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    return redirect('/')

# Add a course
@app.route('/add_course', methods=['POST'])
def add_course():
    course_name = request.form['course_name']
    instructor = request.form['instructor']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (?, ?)", (course_name, instructor))
    conn.commit()
    conn.close()
    return redirect('/')

# Enroll a student
@app.route('/enroll', methods=['POST'])
def enroll():
    student_id = request.form['student_id']
    course_id = request.form['course_id']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrolments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
    conn.commit()
    conn.close()
    return redirect('/')

# Add a payment
@app.route('/add_payment', methods=['POST'])
def add_payment():
    student_id = request.form['student_id']
    amount = request.form['amount']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO payments (student_id, amount) VALUES (?, ?)", (student_id, amount))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
