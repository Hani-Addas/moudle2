"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        'name': 'Hani Addas',
        'Student ID': '2458948',
        'pizza toppings': [
            'Tomato',
            'chicken',
            'mashrooms'
        
        ],
        'movie': [
            {
                'title': 'Moneyball',
                'genre': ''
            },
            {
                'title': 'The Matrix',
                'genre': 'sci-fi'
            }
        ]
    }
       
    # Step 3: Print student name and ID
    print(f"My name is {about_me['name']}, but you can call me sir {about_me['name'].split()[0]}")
    
    print (f"My student ID is {about_me ['Student ID']}")
 
   
    # Step 4: Print a bullet list of pizza toppings
    for pizza_toppings in about_me['pizza toppings']:
        print (f'my favorite pizza topping are:*{pizza_toppings}')
    
    # Step 5: Add pizza toppings to the data structure
    
    add_pizza_toppings(about_me, ['papers', 'olives'])
    print_pizza_toppings(about_me)
    
    
    
    
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['olives', 'beef'])
    print_pizza_toppings(about_me)

   
   
   
   
   
    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'the lord of the rings', 'fantasy')

   
   
   
   
   
    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

   
   
   
   
    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])


def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    # Print sentence containing student ID
    print()

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    print(f"My favourite pizza tippings are:*{pizza_toppings}")
    # Print bullet list of favourite pizza toppings
    print()

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5

    # Append new pizza toppings to end of list 

    # Convert all pizza toppings to lowercase
    my_info['pizza toppings'][i] = toppings.lower()
    # Sort toppings list alphabetically
    my_info['pizza toppings'].sort()
    

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    my_info['movies'].append({title, genre})
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    print()

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    print()

if __name__ == '__main__':
    main()