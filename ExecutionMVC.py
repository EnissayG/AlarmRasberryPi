from modele.evenement import Evenement
from modele.utilisateur import Utilisateur

from DAO.DAO import DAO
from DAO.EvenementDAO import EvenementDAO
from DAO.UtilisateurDAO import UtilisateurDAO


from peripheriques import Peripherique


from exceptions.peripheriqueException import PeripheriqueException
from exceptions.bdconfigexception import BdConfigException

import traceback
import time
from datetime import datetime
from random import uniform
global utilisateurActif

class Jeu() :

    def __init__(self, fichierConfig) -> None:
        
        self.__peripherique = None
        self.__utilisateur = None
        self.__evenement = None 
        self.__configuration = fichierConfig

    

    

        
    def __connecteurUtilisateur(self):

        

         
            user= input("Inscrivez votre nom utilisateur:").strip()
            pwd=input("Inscrivez votre mot de passe:").strip()
            
            utilisateur= Utilisateur(user,pwd)
            utilisateurActif = utilisateur;
            validation = self.__connecterUtilisateurBD(utilisateur)
            
            return validation

    def __inscrireUtilisateur(self):
            
            user= input("Inscrivez votre nom utilisateur:").strip()
            pwd=input("Inscrivez votre mot de passe:").strip()
            
            
            utilisateur= Utilisateur(1,user,pwd)
            utilisateurActif = utilisateur;
            validation = self.__inscrireUtilisateurBD(utilisateur)
            
            return validation

    
    def __inscrireEvenement(utilisateurID,evenementNom):
        
            evenement = Evenement(utilisateurID,evenementNom,time.time())
            
            
            utilisateur= Utilisateur(user,pwd)
            validation = self.__creerEvenementBD(evenement.utilisateurId,evenement.typeEvenement, evenement.temps)
            
            return validation

         

    def __inscrireUtilisateurBD(self, utilisateur):
        user = utilisateur._pseudo
        pwd = utilisateur._pwd
        print(user,pwd)

        resultat = UtilisateurDAO.chercherParPseudoEtMotDePasse(user,pwd)
        if resultat is None:
            UtilisateurDAO.creer(utilisateur)
            print(utilisateur.pseudo, " vous êtes un nouveau utilisateur")
            return True
        else:
            utilisateur.id = utilisateur.id
            print(utilisateur.pseudo, " vous êtes un joueur existant")
            return False

    
    
    
    def __connecterUtilisateurBD(self,utilisateur):
         resultat = UtilisateurDAO.chercherParPseudoEtMotDePasse(utilisateur.pseudo,utilisateur.pwd)
         if resultat is None:
             print(utilisateur.pseudo, " Authentification échouée ")
             return False
         else:
             utilisateur.id = utilisateur.id
             print(utilisateur.pseudo, " Authentification réussie")
             return True
            
    def __creerEvenementBD(self,evenement):
         resultat = EvenementDAO.creer(evenement.utilisateurId,evenement.typeEvenement, evenement.temps)
         if resultat is None:
             print(utilisateur.pseudo, " Authentification échouée ")
             return False
         else:
             utilisateur.id = utilisateur.id
             print(utilisateur.pseudo, " Authentification réussie")
             return True


    def main(self):

        try:

            #Configuration des capteurs/effecteurs
            self.__peripherique = Peripherique()
            self.__peripherique.setup(self.__configuration)
            
            #condition qui reste fausse jusqu'a une bonne décision pour inscription ou login
            conditionConnection= False

            #Configuration de la bd
            DAO.setup(self.__configuration)

            decision = input("Voulez vous vous inscrire ou vous connecter ? (i/c)")
            #decision = decision.trim()
            #decision = decision.lower

            
            while conditionConnection == False:
                if(decision == "i"):
                    user = self.__inscrireUtilisateur()
                    conditionConnection = True
                
                elif(decision == "c"):
                    self.__connecteurUtilisateur()                  
                    conditionConnection = True
                    
                else:
                    print("Veuillez rentrer une option valide soi I ou C")
                    break
                
                
            
            #Inscrire les joueurs à la partie
            self.__inscrireJoueur()

            #Inscrire la partie dans la bd et lui associer ses joueurs
            resultat = PartiesDAO.creer(self.__partie)
            print("La ", self.__partie, " est enregistrée en mémoire.")

            #Jouer
            print("La partie commence")
            jouer = True
            while jouer == True :
                time.sleep(0.1)
                if(Peripherique.buttonState==1):
                    Peripherique.Led(0)
                  
                    if (0 == GPIO.input(ObstaclePin)):
                        
                        Peripherique.LCD1602.clear()
                        Peripherique.LCD1602.write(0, 0, 'Intrusion')
                        Peripherique.LCD1602.write(1, 1, 'Detecte!')
                        time.sleep(0.8)
                        Peripherique.LCD1602.clear()
                        Peripherique.beep(0.5)
                        Peripherique.beep(0.5)
                        Peripherique.beep(0.5)
                        Peripherique.light(0.3, 0.02)

                else:
                    
                    Peripherique.Led(1)

        except PeripheriqueException as err:
            print(err)
            traceback.print_exc()

        except BdConfigException as err:
            print(err)
            traceback.print_exc()

        except Exception as err:
            print("une erreur inatendue est survenue ", err)
            traceback.print_exc()
    
if __name__ == "__main__":
    jeu = Jeu("config.ini")
    jeu.main()
