import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence

class TestZoo (TestCase):


    def setUp(self) -> None:
       self.zoo_1: Zoo= Zoo(c)

       self.zookeeper_1: ZooKeeper= ZooKeeper(nome= "Mimmo",cognome= "me puzza",id=1)
       self.fence_1 : Fence = Fence(area=100,temperature=25.0, habitat="Savana")
       self.fence_2 : Fence = Fence(area=100,temperature=25.0, habitat="Foresta")
       self.animal_1: Animal = Animal(name="Pluto",species="canide",age=5,height=300.0,width=100.0,preferred_habitat="Savana")
       self.animal_2: Animal = Animal(name="Arcibaldo",species="Equidi",age=5,height=3.0,width=1.0,preferred_habitat="Savana")


    def test_animal_dimension_1 (self):
        """" questo test controlla se la dimensione dell'animale sia troppo grande per l'area della fence in tal caso non vengono aggiunti alla fence """
        self.zookeeper_1.add_animal(self.animal_1,self.fence_1)
        result: int = len(self.fence_1.lista_animali_recinto)
        message: str = f'Error: the functioon add_animal should not add self.animal_1 intoself.fence_1'
        
        self.assertEqual(result,0, message)

    def test_animal_dimension_2 (self):
        """" questo test controlla che la dimensione dell'animale sia adeguata a l'area della gabbia """
        self.zookeeper_1.add_animal(self.animal_2,self.fence_1)
        result: int = len(self.fence_1.lista_animali_recinto)
        message: str = f'Error: the functioon add_animal should not add self.animal_1 intoself.fence_1'
        
        self.assertEqual(result,1, message)


    def test_animal_habitat_1 (self):
        """"questo test controlla che l'habitat dell'animale sia uguale l'habitat della gabbia se diverso non aggiunge l'animale """
        self.zookeeper_1.add_animal(self.animal_1,self.fence_2)
        result: int = len(self.fence_2.lista_animali_recinto)
        message: str = f'Error: the function allow only equal habitat'

        self.assertEqual(result,0,message)

    def test_animal_habitat_2(self):
        """"questo test controlla che l'habitat dell'animale sia uguale a l'habitat della gabbia """
        self.zookeeper_1.add_animal(self.animal_1,self.fence_2)
        result: int = len(self.fence_2.lista_animali_recinto)
        message: str = f'Error: the function allow only equal habitat'

        self.assertEqual(result,1,message)

    
    
        


if __name__ == "__main__":

    unittest.main()