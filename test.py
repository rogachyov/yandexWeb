import json
import pprint
import json
from requests import get, delete, post

pprint.pprint(get("http://127.0.0.1:5000/api/v2/users").json())
pprint.pprint(get("http://127.0.0.1:5000/api/v2/users/1").json())

pprint.pprint(post("http://127.0.0.1:5000/api/v2/users").json())
pprint.pprint(delete("http://127.0.0.1:5000/api/v2/users/1").json())

print()

pprint.pprint(get("http://127.0.0.1:5000/api/v2/cities").json())
pprint.pprint(get("http://127.0.0.1:5000/api/v2/cities/1").json())

pprint.pprint(delete("http://127.0.0.1:5000/api/v2/cities/1").json())



# pprint.pprint(get('http://localhost:5000/api/v2/jobs').json())
#
# pprint.pprint(post('http://localhost:5000/api/v2/jobs', {'team_leader': 1, 'job': 'am', 'work_size': 15,
#                                                           'collaborators': '2, 3'}).json())
# pprint.pprint(post('http://localhost:5000/api/v2/jobs', {'team_leader': 1000, 'job': 'am', 'work_size': 15,
#                                                           'collaborators': '2, 3'}).json())
#
# pprint.pprint(get('http://localhost:5000/api/v2/jobs/1').json())
# pprint.pprint(get('http://localhost:5000/api/v2/jobs/1000').json())
#
# pprint.pprint(delete('http://localhost:5000/api/v2/jobs/1').json())
# pprint.pprint(delete('http://localhost:5000/api/v2/jobs/1000').json())
