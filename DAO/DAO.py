import sqlite3
import configparser

from exceptions.bdconfigexception import BdConfigException

class DAO:

    __connexionBD = None
    __nomBD = None

    @staticmethod
    def setup(fichierConfig):
        #sqlite3 database.db -init dump.sql
        try:
            #Lecture du fichier de configuration
            config_obj = configparser.ConfigParser()
            config_obj.read(fichierConfig)
            bdParam = config_obj['BD']
            DAO.__nomBD = bdParam['fichierBD']
        except Exception as err:
            raise BdConfigException("Échec de la configuration de la base de données")

    @staticmethod
    def __get_connexion():

        if(DAO.__connexionBD is None):
            try:
                if DAO.__nomBD is None:
                    bd = ':memory:'
                    #print('Connexion à la bd en mémoire')
                else:
                    bd = '{}.db'.format(DAO.__nomBD)
                    #print("Connexion à la bd ", bd)

                DAO.__connexionBD = sqlite3.connect(bd)
                #Permet d'accéder les colonnes par leur nom lors d'une SELECT par exemple
                DAO.__connexionBD.row_factory = sqlite3.Row
            except:
                raise

        return DAO.__connexionBD

    @classmethod
    def _executer_requete(cls, sql, params = None):

        try:
            #Requête sans paramètre
                 #Requête sans paramètre
            if params is None:
                curseur = DAO.__get_connexion().execute(sql)
            #Requête contenant une liste de plusieurs listes de paramètres
            elif any(isinstance(el, list) for el in params):
                curseur = DAO.__get_connexion().executemany(sql, params)
            #Requête contenant une liste de paramètres
            else:
                curseur = DAO.__get_connexion().execute(sql, params)

            #Effectuer le commit des opérations modifiant la bd
            if sql.find('SELECT') == -1:
                DAO.__get_connexion().commit()
        except:
            raise

        return curseur

    @classmethod
    def fermer_connexion(cls):
        if(DAO.__connexionBD is not None):
            DAO.__connexionBD.close()
            DAO.__connexionBD = None

