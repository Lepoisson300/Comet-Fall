import sqlite3

from datetime import datetime
from interface import Interface

class basedonnee :
    """
    ###############################################
    #Classe permettant de gérer la base de données#
    ###############################################
    """
    def __init__(self):
        self.connexion = sqlite3.connect('basedonnee.db')
        self.curseur = self.connexion.cursor()

    def enregistrer(self):

        """
        #######################################################################
        #Fonction qui enregistre le score et le pseudo dans la base de données#
        #######################################################################
        """
        try :

            id_joueur = 1
            req = self.curseur.execute('INSERT INTO Joueur VALUES(?,?)', ((id_joueur, user_input, )) )
            req = self.curseur.execute('INSERT INTO Jeu VALUES(?,?,?)', ((id_joueur, self.score, str(datetime.now()),)))
            id_joueur = id_joueur+1

        except Exception as e:
            print("ERREUR", e)
            self.connexion.rollback()
            print("Commande annulee")

        finally:
            self.connexion.close()

    def score(self):

        """
        #########################################################
        #Fonction permettant de récupérer les scores des joueurs#
        #########################################################
        """

        try :

            req = self.curseur.execute('SELECT pseudo,score FROM Jeu join Joueur on Jeu.id_joueur = Joueur.id_joueur order by ASC')
            print(self.curseur.fetchone())

        except Exception as e:
            print("ERREUR", e)
            self.connexion.rollback()
            print("Commande annulee")

        finally:
            self.connexion.close()