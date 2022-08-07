# pip intall requests
import requests
# url로
order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'url'
# 요청을 보내서
response = requests.get(URL)
# 응답 받은 값을 가져온다.
print(response,type(response)) # 
 