import requests

r = requests.get("http://localhost:5151/multiply/3/9")

r_post = requests.post("http://localhost:5151/post", json={"number":4})
print(r_post.text, r.text)