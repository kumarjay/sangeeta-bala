from flask import Flask, render_template, request, flash, redirect
from flask import url_for
from send_email import send_mail

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

abc = 'hello world'

@app.route('/')
def index():
    return render_template('index.html', name=request.args.get('name'))


@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    name = request.form.get('name')
    email = request.form.get('email')
    print('name : ', name, ' ', email)

    status = send_mail(name, email, email)
    # status = True

    if status == True:
        flash('You appointment is successfully booked !!!')
    else:
        flash('Sorry, There was some technical problem. Please try agian !!')
    return redirect(url_for('index', name= name))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)