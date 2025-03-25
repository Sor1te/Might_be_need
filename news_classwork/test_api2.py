from requests import post, delete, get

print(delete('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/news/1').json())
print(get('http://localhost:5000/api/news/q').json())
print(post('http://localhost:5000/api/news', json={}).json())
print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())