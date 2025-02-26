from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas
tasks = []

@app.route('/')
def index():
    # Renderiza la plantilla 'index.html' y pasa la lista de tareas a la plantilla
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    # Obtiene la tarea del formulario
    task = request.form.get('task')
    if task:
        # Agrega un diccionario de tarea a la lista de tareas
        tasks.append({'name': task, 'completed': False})
    # Redirige a la página de inicio
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    # Marca la tarea como completada si el id es válido
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
    # Redirige a la página de inicio
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    # Verifica que el id de la tarea sea válido
    if 0 <= task_id < len(tasks):
        # Elimina la tarea de la lista
        tasks.pop(task_id)
    # Redirige a la página de inicio
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Inicia la aplicación en modo de depuración
    app.run(debug=True)
