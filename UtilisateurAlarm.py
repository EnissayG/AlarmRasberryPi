from modele.utilisateur import Utilisateur

class UtilisateurAlarme(Utilisateur) :

    _bouton = -1

    @property
    def bouton(self):
        return self._bouton

    @bouton.setter
    def bouton(self, new_bouton):
        self._bouton = new_bouton

    def __str__(self):
        utilisateurStr = super().__str__()

        return "Utilisateur : {utilisateur}, bouton : {bouton}".format(utilisateur = utilisateurStr, bouton = self.bouton)
