import requests
import json

# Відправка GET-запиту
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Перевірка успішності запиту
if response.status_code == 200:
    # Отримання відповіді у форматі JSON
    data = response.json()
    
    # Красивий вивід JSON
    print(json.dumps(data, indent=4, ensure_ascii=False))
else:
    print(f'Помилка запиту: {response.status_code}')