from pupil import Pupil

def find_pupil_by_name(pupils:list[Pupil], surname:str):
    """
    Finds a pupil by its name.
    """
    for pupil in pupils:
        if pupil.surname.lower() == surname.lower():
            return pupil
    return None

def sort_pupils_by_age(pupils:list[Pupil]):
    """
    Returns sorted pupils list by age
    """
    return sorted(pupils, key= lambda p: p.age)

def sort_by_age_categories(pupils:list[Pupil]):
    """
    Returns sorted pupils list by age categories in order:
    junior, middle, senior
    """
    result = {
    "junior":[],
    "middle":[],
    "senior":[]    
    }
    
    for pupil in sort_pupils_by_age(pupils):
        result[pupil.determine_age_category()].append(pupil)
        
    return result