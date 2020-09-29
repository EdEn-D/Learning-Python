from urllib import request

intel_stock = 'http://chart.finance.yahoo.com/table.csv?s=INTC&a=2&b=18&c=2017&d=2&e=24&f=2017&g=d&ignore=.csv'

def download_stock_data(csvUrl):
    response = str(request.urlopen(csvUrl).read())
   # csv = response.read()
   # csv_str = str(response)
    lines = response.split(r"\n")
    fileName = r'intel.csv'
    fx = open(fileName, "w")
    for line in lines[2:]:
        fx.write(line + '\n')

    fx.close()

download_stock_data(intel_stock)