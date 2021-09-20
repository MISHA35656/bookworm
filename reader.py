from requests import *
from requests.exceptions import Timeout, ConnectionError
import sys

print('Введите URL ленты')
url = sys.stdin.readline()
news = requests.get(url)
if news.status_code != 200:
  print('Ошибка: Код ответа сервера должен быть 200, но код ответа сервера ' news.status_code)
else:
  pass
except Timeout:
  print('Server timeout')
except ConnectionError:
  print('Connection error')
except:
  print('Error')
