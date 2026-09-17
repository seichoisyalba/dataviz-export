import truststore
truststore.inject_into_ssl()  # utilise le magasin de certificats Windows (gère les certificats d'entreprise)

import requests

url = "https://servo.leaudiledefrance.fr/apps/dataviz/"

session = requests.Session()
resp = session.get(url, timeout=30, allow_redirects=True)

print("Status:", resp.status_code)
print("URL finale:", resp.url)
print("Cookies obtenus:", session.cookies.get_dict())
