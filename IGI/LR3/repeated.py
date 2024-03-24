def repeatedTask(func):
    """This is decorator to repeat functions with choice"""
    def wrapper():
        while True:
            func()
            choice = input('Wanna try again? (y/n)')
            if choice == 'n':
                break
    
    return wrapper