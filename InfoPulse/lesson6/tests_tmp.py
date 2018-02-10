
import requests

req = requests.get("http://pulse-rest-testing.herokuapp.com/roles")
dataD = req.json()
for a in dataD:
    print(a, "WAS DELETED")
    requests.delete("http://pulse-rest-testing.herokuapp.com/roles/"+str(a['id'])+"/")