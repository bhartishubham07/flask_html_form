from flask import Flask, render_template, request

FAI = Flask(__name__)

@FAI.route('/data', methods = ['GET','POST'])
def data():
    if request.method == 'POST':
        username = request.form['na']
        password = request.form['pw']
        return 'Form is Submitted'
        
    return render_template('data.html')


if __name__ == '__main__':
    FAI.run(debug=True)