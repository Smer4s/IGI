from pupil import Pupil
from csv import writer,reader
from pickle import dump, load

class PupilSerializer:
    @staticmethod
    def save_to_csv(pupils: list[Pupil], filename:str):   
        """
        Saves pupil data to a CSV file.
        """
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = writer(csvfile)
            csvwriter.writerow(['Surname', 'Age'])
            for pupil in pupils:
                csvwriter.writerow([pupil.surname, pupil.age])
                
    @staticmethod
    def load_from_csv(filename:str):
        """
        Loads pupil data from a CSV file.
        """
        pupils = []
        with open(filename, 'r') as csvfile:
            csvreader = reader(csvfile)
            next(csvreader)
            for row in csvreader:
                name, age = row
                pupils.append(Pupil(name, age))
                
        return pupils

    @staticmethod
    def save_to_pickle(pupils:list[Pupil], filename:str):
        """
        Saves pupil data to a pickle file.
        """
        with open(filename, "wb+") as file:
            dump(pupils, file)
            
    @staticmethod
    def load_from_pickle(filename:str):
        """
        Loads pupil data from a pickle file.
        """
        with open(filename, 'rb') as file:
            products = load(file)
        return products
                
    