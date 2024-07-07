from film import Film
from movie_genre import Azione,Commedia,Drama


class Noleggio:
    def __init__(self,film_list:list) -> None:
        self.film_list = film_list
        self.rented_film: dict={}
        self.__clientID= None

    def AddFilm (self,film:Film)-> None: # appende i film alla lista dei film disponibile in  videoteca
        if film in self.film_list:
            print(f'il film è gia presente nella lista {film.getTitle()}')
        else: 
            film  not in self.film_list
            self.film_list.append(film)
    
    def RemoveFilm (self,film:Film) -> None:
        self.film_list.remove(film)
                
    def isAvaible(self,film:Film) -> bool:
        if film in self.film_list:
            print(f'Il film scelto è disponibile: {film.getTitle()}".')
            return True
        else: 
            print(f'Il film scelto non è disponibile: {film.getTitle()}".')
            return False
        
    def SetIdClient(self, id_client: int) -> None:
        id_client = self.__clientID

    def GetIdClient(self) -> int:
        return self.__clientID
    
    def rentAMovie(self, film: Film, clientID)-> None:
        if self.isAvaible(film) == True:
            self.RemoveFilm(film)
            print(True)
            if clientID in self.rented_film:
                self.rented_film[clientID].append(film)
                print (f'"Il cliente {clientID} ha noleggiato {film.getTitle()}!"{self.rented_film}')    
            else :
                self.rented_film[clientID] = [film]
                print (self.rented_film)
                print (f'"Il cliente {clientID} ha noleggiato {film.getTitle()}! nuovo cliente')    
        else:
            print(f'Non è possibile nolegiare il film {film.getTitle()}')

    def giveBack(self, film: Film, clientID : int, days:int)-> None:
        
        self.rented_film[clientID].remove(film)
        self.film_list.append(film)
        total= film.calcolaPenaleRitardo(days)
        print(f'{clientID}! La penale da pagare per il film {film.getTitle()} e di {total} euro!"')

    def printMovies(self):
        movies:Film
        for movies in self.film_list:
            print (f'{movies.getTitle()} - {movies.getGenere()}')

    def printRentMovies(self,clientID):
        movies:Film
        print(f'lista film del cliente n {clientID} :')
        for movies in self.rented_film[clientID]:
            print (f'{movies.getTitle()}')

""""printRentMovies(clientID): questo metodo deve stampare
 la lista dei film noleggiati dal cliente di cui viene specificato l'id."""

    



