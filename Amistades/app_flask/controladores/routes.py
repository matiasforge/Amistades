from flask import render_template, request, redirect, url_for
from app_flask import app, db
from app_flask.modelos.modelos import User, Friendship, UserFriend

@app.route('/friendships')
def view_friendships():
    cursor = db.cursor()
    cursor.execute('SELECT u1.nombre AS user, u2.nombre AS friend FROM user_friends f JOIN users u1 ON f.user_id = u1.id JOIN users u2 ON f.friend_id = u2.id')
    friendships = cursor.fetchall()
    return render_template('friendships.html', friendships=friendships)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        cursor = db.cursor()
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cursor.execute('INSERT INTO users (nombre, apellido) VALUES (%s, %s)', (nombre, apellido))
        db.commit()
        user_id = cursor.lastrowid
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user = cursor.fetchone()

        return redirect(url_for('view_friendships', user=user))
    return render_template('add_user.html')

@app.route('/add_friendship', methods=['GET', 'POST'])
def add_friendship():
    cursor = db.cursor()
    
    if request.method == 'POST':
        user_id = request.form['user_id']
        friend_id = request.form['friend_id']
        cursor.execute('INSERT INTO user_friends (user_id, friend_id) VALUES (%s, %s)', (user_id, friend_id))
        db.commit()
        return redirect(url_for('view_friendships'))

    cursor.execute('SELECT id, nombre FROM users')
    users = cursor.fetchall()
    
    return render_template('add_friendship.html', users=users)

@app.route('/show_user/<int:user_id>')
def show_user(user_id):
    cursor = db.cursor()
    cursor.execute('SELECT id, nombre, apellido FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()
    return render_template('show_user.html', user=user)

