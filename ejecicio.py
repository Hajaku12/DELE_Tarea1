import sqlite3

conn = sqlite3.connect('Universidad.db')
cursor = conn.cursor()

# Creación de Tabla de estudiante
cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudiante (
        estudiante_id INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT,
        fecha_nacimiento DATE,
        carrera_id INTEGER,
        FOREIGN KEY (carrera_id) REFERENCES materias(materia_id)
    );
''')

# Creación de tabla de profesor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS profesor (
        profesor_id INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT,
        departamento_id INTEGER,
        FOREIGN KEY (departamento_id) REFERENCES materias(materia_id)
    );
''')

# Creación de tabla de adminitrador
cursor.execute('''
    CREATE TABLE IF NOT EXISTS administrador (
        admin_id INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT
    );
''')

# Creación de tabla de cursos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cursos (
        curso_id INTEGER PRIMARY KEY,
        curso_nombre TEXT,
        departamento_id INTEGER,
        profesor_id INTEGER,
        FOREIGN KEY (departamento_id) REFERENCES cursos(curso_id),
        FOREIGN KEY (profesor_id) REFERENCES profesor(profesor_id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS inscripcion (
        inscripcion_id INTEGER PRIMARY KEY,
        estudiante_id INTEGER,
        curso_id INTEGER,
        FOREIGN KEY (estudiante_id) REFERENCES estudiante(estudiante_id),
        FOREIGN KEY (curso_id) REFERENCES curso(curso_id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS trabajo (
        trabajo_id INTEGER PRIMARY KEY,
        profesor_id INTEGER,
        materia_id INTEGER,
        FOREIGN KEY (profesor_id) REFERENCES profesor(profesor_id),
        FOREIGN KEY (curso_id) REFERENCES curso(curso_id)
    );
''')

# Poblar tablas
cursor.execute("INSERT INTO estudiante VALUES (1, 'Juan', 'Perez', '1990-01-01', 1);")
cursor.execute("INSERT IN profesor VALUES (1, 'Juana', 'Perez', 2);")
cursor.execute("INSERT INTO administrador VALUES (1, 'Juanito', 'Perez');")
cursor.execute("INSERT INTO curso VALUES (1, 'Matematica', 2, 1);")
cursor.execute("INSERT INTO inscripcion VALUES (1, 1, 1);")
cursor.execute("INSERT INTO trabajo VALUES (1, 1, 1);")

conn.commit()
conn.close()

#Create at least two selescts with "where" clauses

conn = sqlite3.connect('University.db')
cursor = conn.cursor()

# Estudiantes de una carrera
cursor.execute("SELECT * FROM estudiante WHERE carrera_id = 1;")
print("Estudiante en la carrera:")
print(cursor.fetchall())

# Proferores de un departamento
cursor.execute("SELECT * FR profesor WHERE departamento_id = 1;")
print( "Profesores de un departamento:")
print(cursor.fetchall())

#Create at least all types of joins
# INNER JOIN
cursor.execute('''
    SELECT estudiante.nombre, estudiante.apellido, curso.curso_nombre
    FROM estudiante
    INNER JOIN inscripcion ON estudiante.estudiante_id = inscripcion.estudiante_id
    INNER JOIN curso ON inscripcion.curso_id = curso.curso_id;
''')
print("\nINNER JOIN:")
print(cursor.fetchall())

# LEFT JOIN
cursor.execute('''
    SELECT profesor.first_nam profesor.apellido, curso.curso_nombre
    FROM profesor
    LEFT JOIN trabajo  profesor.profesor_id = trabajo.profesor_id
    LEFT JOIN curso ON trabajo.curso_id = curso.curso_id;
''')
print("\nLEFT JOIN:")
print(cursor.fetchall())

# RIGHT JOIN 
cursor.execute('''
    SELECT estudiante.nombre, estudiante.apellido, inscripcion.curso_id
    FROM estudiante
    LEFT JOIN inscripcion ON estudiante.estudiante_id = inscripcion.estudiante_id;
''')
print("\nRIGHT JOIN:")
print(cursor.fetchall())

#  FULL OUTER JOIN 
cursor.execute('''
    SELECT estudiante.nombre, estudiante.apellido, curso.curso_nombre
    FROM estudiante
    LEFT JOIN inscripcion ON estudiante.estudiante_id = inscripcion.estudiante_id
    LEFT JOIN curso ON inscripcion.curso_id = curso.curso_id
    UNION
    SELECT estudiante.nombre, estudiante.apellido, NULL AS curso_nombre
    FROM estudiante
    WHERE estudiante.estudiante_id NOT IN (SELECT estudiante_id FROM inscripcion);
''')
print("\nFULL OUTER JOIN:")
print(cursor.fetchall())

conn.commit()
conn.close()