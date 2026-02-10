from db import get_connection

def add_new_contact():
    print("Add new contact Selected : ")
    person_s_no = int(input("Enter serial number : "))
    person_name = input("Enter person's name : ")
    person_phone_number = input("Enter person's phone number : ")
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    """
    INSERT INTO contacts ('sno','name','phone_number')
    VALUES (?,?,?)
    """,
    (person_s_no , person_name, person_phone_number)
    )
    conn.commit()
    conn.close()

    print("Contact Added Successfully!")


def view_all_contact():
    print("View All Contact Selected : ")
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    """
    SELECT * FROM contacts
    """
    )
    print("These are list of all contacts.")

    contacts = cursor.fetchall()
    if len(contacts) == 0:
        print("No contacts found!")
    else: 
        print("\n S.No | Name | Contact ")
        print("*" * 50 )

    for contact in contacts:
        person_s_no,person_name,person_phone_number = contact
        print(person_s_no, "|" , person_name, "|" , person_phone_number)

        conn.close()



def search_contact_by_name():
    print("Search Contact by Name Selected : ")

    search_name = input("Enter name you want to search : ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    """
    SELECT name , phone_number FROM contacts
    WHERE name = ? 
    """,
    (search_name,)
    )

    contacts = cursor.fetchall()
    if len(contacts) == 0 :
        print("No contacts found!")
    else:
        print("\nName | Phone Number")
        print("-" * 30) 

        for name, phone_number in contacts :
            print(f"{name} | {phone_number}")

    conn.close()

def delete_contact():
    print("Delete Contact Selected : ")
    
    person_name = input("Enter name which contact you want to delete : ")
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    """
    DELETE FROM contacts
    where name = ?
    """,
    (person_name,)
    )
    conn.commit()
    print("Contact Deleted successfully! ")
    conn.close()


def exit_program():
    print("Exiting program......Logging out... ")
    quit()
    
 
