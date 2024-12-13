import psycopg2
import sys
import os
import hashlib
import getpass
import re

def main():
    try:
        conn = psycopg2.connect(host='82.67.90.50', dbname='postgres ', user='postgres ', password='|)r6>|}ST87B', port = '5432')
    except Exception as e:
        print(e)
        sys.exit(1)

    cur = conn.cursor()

    print("Bienvenue sur le programme d'authentification")
    print("1. Connexion")
    print("2. Inscription")
    print("3. Quitter")
    choix = input("Que voulez-vous faire ? ")

    if choix == "1":
        username = input("Nom d'utilisateur: ")
        password = getpass.getpass("Mot de passe: ")
        password = hashlib.sha256(password.encode()).hexdigest()

        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        if cur.fetchone():
            print("Vous êtes connecté")
        else:
            print("Mauvais nom d'utilisateur ou mot de passe")
    elif choix == "2":
        username = input("Nom d'utilisateur: ")
        password = getpass.getpass("Mot de passe: ")
        password = hashlib.sha256(password.encode()).hexdigest()
        email = input("Email: ")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Email invalide")
            sys.exit(1)

        cur.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        conn.commit()
        print("Vous êtes inscrit")
    elif choix == "3":
        sys.exit(0)
    else:
        print("Choix invalide")
        sys.exit(1)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()








