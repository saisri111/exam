
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def register():
    return render_template('register.html')



@app.route('/success', methods=['POST'])
def success():
    name = request.form['name']
    email = request.form['email']
    rno = request.form['rno']
    return render_template(
        'success.html',
        name=name,
        email=email,
        rno=rno,
    )

if __name__ == '__main__':
    app.run(debug=True)