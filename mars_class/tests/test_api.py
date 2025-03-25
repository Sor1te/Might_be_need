from requests import get, post

print(post('http://localhost:5000/api/jobs', json={}).json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1, 'job': 'dihg', 'work_size': 23, 'collaborators': '1 2 3', 'is_finished': False}).json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1, 'job': 'dihg', 'work_size': 23}).json())

print(post('http://localhost:5000/api/jobs',
           json={'work_size': 23}).json())