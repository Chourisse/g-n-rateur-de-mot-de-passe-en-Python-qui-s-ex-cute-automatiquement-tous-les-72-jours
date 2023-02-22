import random
import string
import requests
import schedule
import time

# Paramètres du programme
SITE_URL = "https://www.example.com"
USERNAME = "your_username"
PASSWORD_LENGTH = 16
PASSWORD_CHARS = string.ascii_letters + string.digits + string.punctuation

# Fonction de génération de mot de passe
def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

# Fonction pour se connecter au site web et changer le mot de passe
def change_password():
    new_password = generate_password(PASSWORD_LENGTH, PASSWORD_CHARS)
    response = requests.post(
        SITE_URL + "/change-password",
        data={"username": USERNAME, "password": new_password}
    )
    if response.status_code == 200:
        print(f"Le mot de passe a été changé avec succès à {time.ctime()}.")
    else:
        print("Une erreur s'est produite lors de la modification du mot de passe.")

# Planifier la tâche pour qu'elle s'exécute toutes les 72 heures
schedule.every(72).hours.do(change_password)

# Boucle d'exécution principale
while True:
    schedule.run_pending()
    time.sleep(1)