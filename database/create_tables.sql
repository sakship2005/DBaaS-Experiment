-- Students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(50),
    enrollment_date DATE
);

-- Courses table
CREATE TABLE IF NOT EXISTS courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(50),
    instructor VARCHAR(50)
);

-- Enrolments table
CREATE TABLE IF NOT EXISTS enrolments (
    enrolment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
