import sqlite3

from DAO.DAO import DAO
from modele.utilisateur import Utilisateur

class UtilisateurDAO(DAO):
    @classmethod
    def afficherTous(cls):
        utilisateurs = list()

        sql = "SELECT * FROM Utilisateurs"
        curseur = cls._executer_requete(sql)

        resultat = curseur.fetchall()
        for enregistrement in resultat:
            utilisateurs.append(Utilisateur(enregistrement["id"], enregistrement["pseudo"], enregistrement["pwd"]))
            
        return utilisateurs

    @classmethod
    def chercherParPseudo(cls, pseudo):
        sql = "SELECT * FROM Utilisateurs WHERE pseudo = ?"
        curseur = cls._executer_requete(sql, [pseudo])

        resultat = curseur.fetchone()

        if resultat is None:
            utilisateur = None
        else:
            utilisateur = Utilisateur(resultat["id"], pseudo)

        return utilisateur
    
    @classmethod
    def chercherParPseudoEtMotDePasse(cls, pseudo, pwd):
        print(pseudo, pwd)
        partiesJoueurs = list()
        partiesJoueurs.append([pseudo])
        partiesJoueurs.append([pwd])
        print(len(partiesJoueurs))
        sql = "SELECT * FROM Utilisateurs WHERE pseudo = ? AND pwd = ?"
        curseur = cls._executer_requete(sql, partiesJoueurs)
        resultat = curseur.fetchone()

        if resultat is None:
            utilisateur = None
        else:
            utilisateur = Utilisateur(resultat["id"], pseudo, pwd)

        return utilisateur

    @classmethod
    def creer(cls, utilisateur):
        sql = "INSERT INTO Alarm.Utilisateurs ('pseudo') VALUES (?),('pwd') VALUE (?)"
        curseur = cls._executer_requete(sql, [utilisateur.pseudo], [utilisateur.pwd])
        lignesAffectees = curseur.rowcount
        if lignesAffectees == 1:
            utilisateur.id = curseur.lastrowid
        else:
            raise sqlite3.OperationalError("L'utilisateur n'a pas pu être ajouté à la base de données.")

        return lignesAffectees

    @classmethod
    def effacerTous(cls):
        sql = "DELETE FROM Utilisateurs"
        curseur = cls._executer_requete(sql)

        return curseur.rowcount
