from flask import Flask, render_template
import sqlite3 as sql
app = Flask(__name__)
app.secret_key = 'development key'
@app.route('/')
def login():
   return render_template('homepage.html')

@app.route('/viewer')
def viewer():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from orders")
   rows = cur.fetchall();
   return render_template('viewer.html', rows = rows)

if __name__ == '__main__':
   app.run(debug = True)


