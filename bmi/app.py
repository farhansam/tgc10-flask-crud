from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/bmi')
def show_form():
    return render_template('base.template.html')

@app.route('/bmi', methods=["POST"])
def sum_num():
    print(request.form)
    weight = int(request.form.get('weight'))
    height = int(request.form.get('height'))
    bmi = weight / (height/100)**2
    return str(bmi)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)