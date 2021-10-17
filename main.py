import requests
import json

url='https://www.cbr-xml-daily.ru/daily_json.js'
response=requests.request('GET',url)
data=json.loads(response.text)
print(str(data['Valute']['USD']['Name'])+str(':'),str(round(data['Valute']['USD']['Value'],2)))




