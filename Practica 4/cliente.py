import json
import requests

res = requests.get("http://localhost:1880/hello",json={"a":[1,2,3],"b":[4,5,6]})
print(res.json())