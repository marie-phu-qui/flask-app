import requests

r = requests.get("http://localhost:8484/multiply/3/9")

r_post = requests.post("http://localhost:8484/post", json={"number":4})
print(r_post.text, r.text)