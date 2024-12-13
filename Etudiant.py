import re
import secrets
import string
import hashlib

class Etudiant(object):

    def __init__ (self, nom, prenom, num_etudiant, aScolaire, filière, classe, absence):
        self._Nom = nom
        self._Prenom = prenom
        self._Num_etudiant = num_etudiant
        self._AScolaire = aScolaire
        self._Filière = filière
        self._Classe = classe
        self._Absence = absence

### GESTION NOM ###
    def get_nom(self):
        return self._Nom
    
    def set_nom(self, nouveau_nom):
        if nouveau_nom == "":
            raise ValueError("Le nom ne peut pas être vide")
        else:
            self._Nom = nouveau_nom
            print("Le nom a été modifié")

### GESTION PRENOM ###   
    def get_prenom(self):
        return self._Prenom
    
    def set_prenom(self, nouveau_prenom):
        if nouveau_prenom == "":
            raise ValueError("Le prénom ne peut pas être vide")
        else:
            self._Prenom = nouveau_prenom
            print("Le prénom a été modifié")
    
### GESTION NUMERO ETUDIANT ###
    def get_num_etudiant(self):
        return self._Num_etudiant
    
    def set_num_etudiant(self, nouveau_num_etudiant):
        if nouveau_num_etudiant == "":
            raise ValueError("Le numéro étudiant ne peut pas être vide")
        else:
            self._Num_etudiant = nouveau_num_etudiant
            print("Le numéro étudiant a été modifié")
    
### GESTION FORMATION ###
    def get_aScolaire(self):
        return self._AScolaire
    
    def get_filière(self):
        return self._Filière
    
    def get_classe(self):
        return self._Classe
    
    def set_filière(self, nouvelle_filière):
        liste_f=["IABD","SRC","SI","MCSI","MOC","IW","RVJV"]
        if nouvelle_filière == "":
            raise ValueError("La filière ne peut pas être vide")
        else:
            for i in liste_f :
                if nouvelle_filière.upper() != i:
                    resultat = False
                else:
                    resultat = True
                    break
            if resultat == False:
                raise ValueError("La filière n'est pas valide")
            else:
                self._Filière = nouvelle_filière
                print("La filière a été modifiée")

    def set_aScolaire(self, nouvelle_aScolaire):
        liste_aS=["1","2","3","4","5"]
        if nouvelle_aScolaire == "":
            raise ValueError("L'année scolaire ne peut pas être vide")
        else:
            for i in liste_aS :
                if nouvelle_aScolaire != i:
                    raise ValueError("L'année scolaire n'est pas valide")
                else:
                    self._AScolaire = nouvelle_aScolaire
            print("L'année scolaire a été modifiée")

    def set_classe(self, nouvelle_classe):
        if nouvelle_classe == "":
            raise ValueError("La classe ne peut pas être vide")
        else:
            self._Classe = nouvelle_classe
            print("La classe a été modifiée")

    def set_filière(self, nouvelle_filière):
        liste_f=["IABD","SRC","SI","MCSI","MOC","IW","RVJV"]
        if nouvelle_filière == "":
            raise ValueError("La filière ne peut pas être vide")
        else:
            for i in liste_f :
                if nouvelle_filière.upper() != i:
                    resultat = False
                else:
                    resultat = True
                    break
            if resultat == False:
                raise ValueError("La filière n'est pas valide")
            else:
                self._Filière = nouvelle_filière
                print("La filière a été modifiée")

### GESTION ABSENCE ###
    def get_absence(self):
        return self._Absence

    def verify_absence(self, nouvelle_absence):
        if nouvelle_absence > 0:
            print("Vous avez éte",nouvelle_absence,"fois absent")
        else:
            print("Vous n'avez pas été absent")

    def set_absence(self, nouvelle_absence):
        self._Absence = nouvelle_absence

### AFFICHAGE ETUDIANT ###
    def afficher(self):
        print("-----------------------------")
        print("Informations de l'étudiant :")
        print("Nom :" ,self.get_nom()) 
        print("Prenom :", self.get_prenom())
        print("Numéro étudiant :", self.get_num_etudiant())
        print("Formation : ",self.get_aScolaire(), self.get_filière(), self.get_classe())
        self.verify_absence(self.get_absence())

### CREATION DE LA CLASSE USER ###
class User (Etudiant):

    def __init__(self, nom, prenom, num_etudiant, aScolaire, filière, classe, absence, email, login, password):
            Etudiant.__init__(self, nom, prenom, num_etudiant, aScolaire, filière, classe,absence)
            self.__email = email
            self.__login = login
            self.__password = password
### GESTION EMAIL ###
    def get_email(self):
        return self.__email
    
    def gen_email(self):
        self.__email = self._Prenom[0].lower()+self._Nom.replace(" ", "").lower()+"@myges.fr"

    def set_email(self, nouveau_email):
            regex = "^[a-z0-9._-]+@[a-z0-9._-]+\.[a-z]{2,6}$"
            if nouveau_email == "":
                ("L'email ne peut pas être vide")
            else:
                if not re.match(regex, nouveau_email):
                    raise ValueError("L'email n'est pas valide")
                else:
                    self._email = nouveau_email
                    print("L'email a été modifié")

### GESTION LOGIN ###
    def get_login(self):
            return self.__login

    def gen_login(self):
        self.__login = self._Prenom[0].lower()+self._Nom.replace(" ", "").lower()

    def set_login(self, nouveau_login):
            if nouveau_login == "":
                raise ValueError("Le login ne peut pas être vide")
            else:
                self._login = nouveau_login
                print("Le login a été modifié")
### GESTION PASSWORD ###
    def get_password(self):
            return self.__password

    def gen_password(self):
        alphabet = string.ascii_letters + string.digits
        password_length = 14
        for i in range(password_length):
            self.__password =self.__password+ ''.join(secrets.choice(alphabet))

    def hash_password(self, passwordHash):
        passwordHash = hashlib.sha256().hexdigest()
        return passwordHash

    def set_password(self, nouveau_password):
            regex = "^(?=.[A-Za-z])(?=.\d)[A-Za-z\d]{10,}$"
            if nouveau_password == "":
                raise ValueError("Le mot de passe ne peut pas être vide")
            elif re.search(regex, nouveau_password):
                self.__password = nouveau_password
            else : 
                raise ValueError("Le mot de passe n'est pas valide")

### AFFICHAGE USER ###
    def Afficher_User(self):
        self.afficher()
        print("Email :", self.get_email())
        print("Login :", self.get_login())
        print("Password :", self.get_password())
        print("-----------------------------")

## Test de la classe Etudiant ##
# etudiant1 = Etudiant("LE BERRE", "Benjamin", "44678935","3","SRC","2")
# etudiant1.afficher()


# etudiant1._Etudiant__set_nom("LB")
# etudiant1._Etudiant__set_prenom("Benjamin")
# etudiant1._Etudiant__set_filière("IABD")
# etudiant1.afficher()


## Test de la classe User ##
user1 = User("LE BERRE", "Benjamin", "44678935","3","SRC","2", 2,"","","")
user1.gen_email()
user1.gen_login()
user1.gen_password()
print(user1.hash_password(user1.get_password()))
user1.Afficher_User()

user2 = User("GOUBY OLLIVER", "Quentin", "65873907","3","SRC","2",0,"","","")
user2.gen_email()
user2.gen_login()
user2.gen_password()
print(user2.hash_password(user2.get_password()))
user2.Afficher_User()

user3 = User("BONNARD", "Esteban", "47362890","3","SRC","2",4,"","","")
user3.gen_email()
user3.gen_login()
user3.gen_password()
print(user3.hash_password(user3.get_password()))
user3.Afficher_User()