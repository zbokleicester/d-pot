# JEU 

# définir la grille

import http.client
import json

HOST = "localhost"
PORT = 9999

# PARTIE NON COMPLETE /*
def connexion(, ):
    """Envoie une requête pour connecter le joueur."""
    try:
        conn = http.client.HTTPConnection(HOST, PORT)
        headers = {"Content-Type": "application/json"}
        taille_map = {'pseudo': , 'type': }
        body = json.dumps(taille_map)
        conn.request("POST", "/player_data", body=body, headers=headers)
        response = conn.getresponse()
        if response.status == 200:
            return json.loads(response.read().decode())
        else:
            return {"error": f"Erreur : {response.status} {response.reason}"}
    except Exception as e:
        return {"error": f"Erreur lors de la connexion : {e}"}
# PARTIE NON COMPLETE */
    

class Parametre_Jeu():

    def __init__(self, taille_map, nbr_toursmax, timeout_tours, demarrer_partie):

        self.taille_map = taille_map
        self.nbr_toursmax = nbr_toursmax
        self.timeout_tours = timeout_tours
        self.demarrer_partie = demarrer_partie

    def a_json(self):

         return {

             'taille_map': self.taille_map,
             'nbr_toursmax': self.nbr_toursmax,
             'timeout_tours': self.timeout_tours,
             'demarrer_partie': self.demarrer_partie

         }
    
    @classmethod

    def de_json(cls, parametre_json):

        return cls(parametre_json['taille_map'],parametre_json['nbr_toursmax'],parametre_json['timeout_tours'], parametre_json['demarrer_partie'])
    
class Jeu():

    def __init__(self, parametres):

        self.parametres = parametres


    def sauvegarde_parametres(self, nom_fichier):

        with open(nom_fichier, 'w' ) as f:
            json.dump(self.parametres.a_json(), f, indent= 4)

    @classmethod

    def chargement_parametre(cls, nom_fichier):

        with open(nom_fichier, 'r') as f:
            parametre_json = json.load(f)

        parametres = Parametre_Jeu.de_json(parametre_json)
        return cls(parametres)
    

def demande_para_jeu():

    print("Saisie des paramètres de jeu:")

    try:
        largeur = int(input("Largeur de la carte: "))
        hauteur = int(input("Hauteur de la carte: "))
        taille_map = (largeur, hauteur)
        nbr_toursmax = int(input("Nombre de tours maximum: "))
        timeout_tours = int(input("Durée max en seconde: "))
        demarrer_partie = bool(input("Demarrer la partie, oui/non: ")).strip().lower() == "oui"

        return Parametre_Jeu(taille_map,nbr_toursmax,timeout_tours,demarrer_partie )
    except ValueError:
    
        print("erreur")
        return (demande_para_jeu)



if __name__ == "__main__":


    parametres = demande_para_jeu

    jeu = Jeu(parametres)

    jeu.sauvegarde_parametres('Parametre_jeu.json')

    chargement_jeu = Jeu.chargement_parametre('Parametre_jeu.json')

print(f"taille map: {chargement_jeu.parametres.taille_map}")
print(f"nombre de tours: {chargement_jeu.parametres.nbr_toursmax}")
print(f"timeout tours: {chargement_jeu.parametres.timeout_tours}")
print(f"Demarrer partie: {chargement_jeu.parametres.demarrer_partie}")


# ---------------------Changement des parametres------------------------------------------------------------------

# parametres.taille_map(20,20)
# parametres.nbr_toursmax(20)
# parametres.timeout_tours(30)
# parametres.demarrer_partie(True)

# jeu.sauvegarde_parametres('Parametre_Jeu.json')
    
