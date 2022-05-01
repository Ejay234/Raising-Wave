import os
from flask import Flask, render_template, request, redirect
from predict import helpMe

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/results', methods=['POST', 'GET'])
def model():
    if request.method == 'POST':
        if not request.form.get("gmsl"):
            return redirect('/')
        else:
            gmsl = request.form.get('gmsl')
        if not request.form.get("sd_gmsl"):
            return redirect('/')
        else:
            sd_gmsl = request.form.get('sd_gmsl')
        if not request.form.get("gia"):
            return redirect('/')
        else:
            gia = request.form.get('gia')
        if not request.form.get("sd_gia"):
            return redirect('/')
        else:
            sd_gia = request.form.get('sd_gia')

        predict = helpMe(gmsl, sd_gmsl, gia, sd_gia)
        print(predict)

        return render_template(
            "results.html/",
            predict=predict,
            gmsl=gmsl,
            sd_gmsl=sd_gmsl,
            gia=gia,
            sd_gia=sd_gia
        )

    else:
        return redirect('/')
