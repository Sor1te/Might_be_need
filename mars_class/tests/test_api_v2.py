from requests import get, post, delete

# print(delete('http://localhost:5000/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/news/1').json())
#
# print(post('http://localhost:5000/api/jobs', json={}).json())
#
# print(post('http://localhost:5000/api/jobs',
#            json={'team_leader': 1, 'job': 'dihg', 'work_size': 23, 'collaborators': '1 2 3',
#                  'is_finished': False}).json())
print(get('http://localhost:5050/api/v2/users').json())
