from forex_python.converter import CurrencyRates
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    try:
       c = CurrencyRates()
       convert = c.convert('USD', 'MXN', 0)
    except:
       return render_template('index.html')

    return render_template('index.html', var1=0, var2=convert)


@app.route("/convert", methods=['GET','POST'])
def convert():
    try:
      if request.method == 'POST':
         amount = request.form['var1']
         fromCurrency = request.form['From']
         toCurrency = request.form['To']
         c = CurrencyRates()
         convert = c.convert(fromCurrency, toCurrency, float(amount))
      else:
         return render_template('index.html')
    except:
       return render_template('index.html')

    return render_template('index.html', var1=amount, var2=convert)
