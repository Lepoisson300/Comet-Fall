import sqlite3

from datetime import datetime


class Database:
    """
    Classe permettant de gérer la base de données
    """

    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def save(self):
        """
        Fonction qui enregistre le score et le pseudo dans la base de données
        """
        try:
            id_joueur = 1
            self.cursor.execute('INSERT INTO Joueur VALUES(?,?)', (id_joueur, self.username))
            self.cursor.execute(
                'INSERT INTO Jeu VALUES(?,?,?)', (id_joueur, self.score, str(datetime.now()))
            )
            id_joueur += 1
        except Exception as e:
            self.conn.rollback()
        finally:
            self.conn.close()

    def score(self):
        """
        Fonction permettant de récupérer les scores des joueurs
        """
        try:
            self.username = input()
            self.score = input()
            self.cursor.execute(
                'SELECT pseudo,score FROM Jeu join Joueur on Jeu.id_joueur = Joueur.id_joueur'
            )
            print(self.cursor.fetchone())

        except Exception as e:
            print("ERREUR", e)
            self.conn.rollback()
            print("Commande annulee")

        finally:
            self.conn.close()
