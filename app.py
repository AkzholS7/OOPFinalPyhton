from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"
DB_HOST = "35.222.165.63"
DB_NAME = "shaurma"
DB_USER = "postgres"
DB_PASS = ""

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


@app.route('/')
def Index():


    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM client"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)

@app.route('/add_student', methods=['POST'])
def add_student():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        client_name = request.form['client_name']
        food_name   = request.form['food_name']
        price       = request.form['price']
        amount      = request.form['amount']
        cur.execute("INSERT INTO client (client_name, food_name, price, amount) VALUES (%s, %s, %s, %s)", (client_name, food_name, price, amount))
        conn.commit()
        flash('Client order submited')
        return redirect(url_for('Index'))
    else:
        flash("Fill all parts")

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('SELECT * FROM client WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', client = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_student(id):
    if request.method == 'POST':
        client_name = request.form['client_name']
        food_name   = request.form['food_name']
        price       = request.form['price']
        amount      = request.form['amount']


        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE client
            SET client_name = %s,
                food_name= %s,
                price = %s,
                amount= %s  
            WHERE id = %s
        """, (client_name, food_name, price, amount, id))
        flash('Order Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_student(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DELETE FROM client WHERE id = {0}'.format(id))
    conn.commit()
    flash('Order Removed')
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
