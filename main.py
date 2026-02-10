from operations import (
    add_new_contact,
    view_all_contact,
    search_contact_by_name,
    delete_contact,
    exit_program
)

print("Welcome to Contact Book!")

while True:
    print('''
1. Add new contact : 
2. View All contact : 
3. Search contact by name : 
4. Delete Contact : 
5. Exit...
''')
   

    choice = input("Enter your choice : ")
    


    menu_actions = {
        "1" : add_new_contact,
        "2" : view_all_contact,
        "3" : search_contact_by_name,
        "4" : delete_contact,
        "5" : exit_program
    }

    action = menu_actions.get(choice)

    if action:
        action()
    else:
        print("invalid choice")

