from flask import Flask, render_template, flash, request
from functions import *

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def calc():
    num1 = 0
    num2 = 0
    val = ""
    
    if(request.method == "POST"):
        num1 = request.form["number1"]
        num2 = request.form["number2"]
        choice = request.form.get("operation")

        if choice=="+":
            val = add(float(num1),float(num2))
        elif choice=="-":
            val = sub(float(num1),float(num2))
        elif choice=="*":
            val = prod(float(num1),float(num2))
        elif choice=="/":
            val = div(float(num1),float(num2))
        

    return render_template("calc.html", number1 = num1 , number2 = num2, value = val)

if __name__ == "__main__":
    app.run(debug=True)