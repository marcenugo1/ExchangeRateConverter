from forex_python.converter import CurrencyRates
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
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


@app.route("/LatestCurrency")
def LatestCurrency():
    try:
         c = CurrencyRates()
         currencyLatest = c.get_rates('USD')

         new_dict = {}

         for k in currencyLatest.keys():
            if 'MXN' in k:
               new_dict[k] = currencyLatest[k]
            if 'INR' in k:
               new_dict[k] = currencyLatest[k]
            if 'EUR' in k:
               new_dict[k] = currencyLatest[k]
            if 'SGD' in k:
               new_dict[k] = currencyLatest[k]
            if 'RUB' in k:
               new_dict[k] = currencyLatest[k]
            if 'AUD' in k:
               new_dict[k] = currencyLatest[k]
            if 'CZK' in k:
               new_dict[k] = currencyLatest[k]
            if 'BRL' in k:
               new_dict[k] = currencyLatest[k]
            if 'CAD' in k:
               new_dict[k] = currencyLatest[k]
            if 'CNY' in k:
               new_dict[k] = currencyLatest[k]

         img = BytesIO()

         keys = new_dict.keys()
         values = new_dict.values()

         plt.bar(keys, values)
         plt.xlabel('Currency')
         plt.ylabel('Amount')

         plt.savefig(img, format='png')
         plt.close()
         img.seek(0)
         plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    except:
       return render_template('index.html')

    return render_template('plot.html', plot_url=plot_url)
