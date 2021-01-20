from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/bmi')
def show_form():
    return render_template('base.template.html')

@app.route('/bmi', methods=["POST"])
def process_bmi():
    print(request.form)
    weight = float(request.form.get('weight'))
    height = float(request.form.get('height'))
    bmi = round(weight / (height/100)**2, 2)
    return render_template('bmi_results.template.html', bmi=bmi)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)