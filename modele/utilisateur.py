class Utilisateur:
    def __init__(self, *args) -> None:
        nbArgs = len(args)

        #Validation du nombre
        if nbArgs > 3:
            raise TypeError("Le constructeur Joueur prend 1 ou 2 paramètres.")

        if nbArgs == 2:
            self._id = None
            self.pseudo = args[0]
            self.pwd = args[0]
        else:
            self.id = args[0]
            self.pseudo = args[1]
            self.pwd = args[2]
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        #Validation du paramètre
        if not isinstance(new_id, int):
            raise TypeError("L'id du joueur doit être un entier.")
        
        self._id = new_id

    @property
    def pseudo(self):
        return self._pseudo
    

    @pseudo.setter
    def pseudo(self, new_pseudo):
        self._pseudo = new_pseudo
        
    @property
    def pwd(self):
        return self._pwd
    
    @pwd.setter
    def pwd(self, new_pwd):
        self._pwd = new_pwd

    def __str__(self):
        if self.id is None:
            idStr = "non défini"
        else:
            idStr = str(self.id)
        return "{id}, {pseudo}, {pwd}".format(id = idStr, pseudo = self.pseudo, pwd = self.pwd)
