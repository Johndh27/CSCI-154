class Hamburger:
    
    """Class that adds the components of a Hamburger into a list"""

    # Initializes the values of the 'dictionary' or Hamburger ingredients
    def __init__(self, **kwargs):
        # function to update the dictionary with keyword arguments being passed through Hamburger
        self.__dict__.update(kwargs)
        
    # Joins the items in the dictionary together into a list, with a separating comma        
    def __str__(self, sep=''):
        # function to do the above ^ comment
        return(', '.join(list(self.__dict__.values())))

burger1 = Hamburger(meat="chicken", extra1="cheese", extra2="ketchup")
print(burger1)
