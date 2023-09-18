from re import findall

import requests

response = requests.get('http://www.columbia.edu/~fdc/sample.html').text
result_beta = findall(r'<h3.*?>(.*)</h3>', response)
print(result_beta)

# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
    result_beta = findall(r'<h3>(.*)</h3>', text)
    print(result_beta)

# зачтено
