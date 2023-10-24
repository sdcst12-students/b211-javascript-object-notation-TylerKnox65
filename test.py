import requests
import json

req = requests.get('https://sdcaf.hungrybeagle.com/menu.php')
print(req)
data = json.loads(req.text)