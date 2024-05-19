from pupil import Pupil
from pupil_serializer import PupilSerializer as serializer
from pupil_extensions import sort_by_age_categories, find_pupil_by_name, sort_pupils_by_age

def main():
    data = {
        'Kirov':7,
        'Hzkov':13,
        'Tikhonova':16,
        'Studenichnik':11,
        'Dvachevskaya':6,
        'Makarov':12,
        'Orehovskiy':14,
        'Nemchinskiy':11,
        'Neko':8,
        'Mayakovskiy':17,
        'Brigadir':15,
        'Lenova':9,
        'Savkin':14,
        'Skarynin':10,
    }

    pupils = Pupil.create_pupils_from_dict(data)

    csvfilename = "Task 1/pupils.csv"
    serializer.save_to_csv(pupils, csvfilename)
    
    picklefilename = "Task 1/pupils.pickle"
    serializer.save_to_pickle(pupils, picklefilename)

    while True:
        print("\nMain Menu:")
        print("1. Output age categories")
        print("2. Search by name")
        print("3. Output sorted by age")
        print("4. Print from csv file")
        print("5. Print from pickle file")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            age_categories = sort_by_age_categories(pupils)
            for age_category in age_categories.keys():
                print("\n" + age_category + ": ")
                for sortedPupil in age_categories[age_category]:
                    print(sortedPupil)
        
        
        elif choice == '2':
            search_name = input("Enter the name to search: ")
            found_pupil = find_pupil_by_name(pupils, search_name)
            if found_pupil:
                print(f'Found a pupil: {found_pupil}')
            else:
                print(f"Pupil not found by surname: {search_name}.")

        elif choice == '3':
            sorted_pupils = sort_pupils_by_age(pupils)
            print("Sorted pupils:")
            for pupil in sorted_pupils:
                print(f"{pupil.age}, {pupil.surname}")

        elif choice == '4':
            loaded_pupils_csv = serializer.load_from_csv(csvfilename)
            for pupil in loaded_pupils_csv:
                print(pupil)

        elif choice == '5':
            loaded_pupils_pickle = serializer.load_from_pickle(picklefilename)
            for pupil in loaded_pupils_pickle:
                print(pupil)

        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()