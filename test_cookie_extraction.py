import browser_cookie3

cj = browser_cookie3.chrome()

trouves = False

for cookie in cj:
    if "servo.leaudiledefrance.fr" in cookie.domain:
        trouves = True
        print(
            "Nom :", cookie.name,
            "| Domaine :", cookie.domain,
            "| Expiration :", cookie.expires
        )

if not trouves:
    print("Aucun cookie SERVO trouvé")
