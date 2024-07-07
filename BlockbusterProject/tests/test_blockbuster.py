import unittest
from unittest import TestCase
from src.Blockbuster.film import Film
from src.Blockbuster.movie_genre import Azione, Drama, Commedia
from src.Blockbuster.noleggio import Noleggio


class testFilm (TestCase):

    def setUp(self) -> None:

        film1 = Commedia(1, "The Shawshank Redemption")
        film2 = Drama(2, "The Godfather")
        film3 = Azione(3, "The Dark Knight")
        film4 = Azione(4, "Pulp Fiction")
        film5 = Drama(5, "Schindler's List")        
        film6= Azione(6,"L'ultimo dei Moicani")
        film7=Azione(7,"Balla coi lupi")

        lista_Blokbuster = [film1, film2, film3, film4, film5, film6, film7]

        blockbuster:Noleggio= Noleggio(lista_Blokbuster)


