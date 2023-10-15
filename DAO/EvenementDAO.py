import sqlite3

from DAO.DAO import DAO
from modele.evenement import Evenement

class EvenementDAO(DAO):

    @classmethod
    def creer(cls, evenement):
        sql = "INSERT INTO Evenement ('id', 'utilisateurId', 'typeEvenement', 'temps') VALUES (?, ?, ?, ?)"
        curseur = cls._executer_requete(sql, [evenement.id, evenement.utilisateurId, evenement.typeEvenement, evenement.temps])

        lignesAffectees = curseur.rowcount
        if lignesAffectees == 1:
            evenement.id = curseur.lastrowid
        else:
            raise sqlite3.OperationalError("L'evenement n'a pas pu être ajouté à la base de données.")

        return lignesAffectees

    @classmethod
    def effacerTous(cls): #à compléter pour prendre en compte les clés étranges
        sql = "DELETE FROM Evenenemt"
        curseur = cls._executer_requete(sql)

        resultat = curseur.rowcount
        return resultat
