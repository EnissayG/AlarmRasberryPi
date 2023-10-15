from modele.utilisateur import Utilisateur
from datetime import datetime

class Evenement:

    def __init__(self, *args) -> None:
        nbArgs = len(args)

        if nbArgs < 2 or nbArgs > 5:
            raise TypeError("Le constructeur Tour prend 2 a 4 paramètres.")

        if nbArgs == 3:
            self._id = None
            self.utilisateurId = args[0]
            self.typeEvenement = args[1]
            self.temps = args[2]
            
        if nbArgs == 2:
            self._id = None
            self.utilisateurId = args[0]
            self.typeEvenement = args[1]
            self.temps = time.time()
        else:
            self.id = args[0]
            self.utilisateur = args[1]
            self.typeEvenement = args[2]
            self.temps = args[3]

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        #Validation du paramètre
        if not isinstance(new_id, int):
            raise TypeError("L'id du tour doit être un entier.")
        
        self._id = new_id

    @property
    def utilisateurId(self):
        return self.utilisateurId

    @utilisateurId.setter
    def utilisateur(self, new_utilisateurId):
        #Validation du paramètre
        if not isinstance(new_utilisateurId, int):
            raise TypeError("l'utilisateur doit etre défini en int")
        self._utilisateurId = new_utilisateurId


    @property
    def temps(self):
        return self._temps

    @temps.setter
    def temps(self, new_temps):
        #Validation du paramètre
        if not isinstance(new_temps, float):
            raise TypeError("La temps de réaction du tour doit être un float.")
        self._temps = new_temps

    @property
    def typeEvenement(self):
        return self.typeEvenement

    @typeEvenement.setter
    def typeEvenement(self, new_typeEvenement):
        #Validation du paramètre
        if not isinstance(new_typeEvenement, str):
            raise TypeError("Le type d'evenement doit être un string.")
        self.typeEvenement = new_typeEvenement

    def __str__(self):

        if self.id is None:
            idStr = "non défini"
        else:
            idStr = str(self.id)

        strTour = "Id : {id}, Id de l'utilisateur : {utilisateurId}, type d'evenement : {typeEvenement}, temps : {temps}".format(id = idStr, utilisateurId = self.utilisateurId, typeEvenement = self.typeEvenement, temps = datetime.fromtimestamp(self._temps).strftime("%d-%m-%Y, %H:%M:%S"))

        return strTour
