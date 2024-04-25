contact={}
def display_contact():
    print("Name \t\tContact_number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
      print("Press 1 for Create Contact \n Press 2 for Search Contact \n Press 3 for Edit Contact \n Press 4 for Display Contact \n Press 5 for Delete Contact \n Press 6 for Exit")

      choice=int(input("Enter your choice from 1 to 6:"))

      if choice==1:
                 name=input("Enter the Name:")
                 phone=input("Enter the contact number:")
                 contact[name]=phone
      elif choice==2:
          search_name=input("Enter the name:")
          if search_name in contact:
              print(search_name,"'s number is found in your contact book",contact[name])
          else:
              print("Sorry,not found")
      elif choice==3:
          edit_contact=input("Enter the contact to be edited:")
          if edit_contact in contact:
              phone=input("Enter the contact number:")
              contact[edit_contact]=phone
              print("Contact updated")
          else:
              print("Contact is not found in your contact book")
      elif choice==4:
         if not contact:
             print("Empty Contact")
         else:
             display_contact()
      elif choice==5:
         del_contact=input("Enter the contact to be deleted:")
         if del_contact in contact:
             confirm=input("Do you want to delete this contact yes/not:")
             if confirm=='yes' or confirm=='Yes':
                 contact.pop(del_contact)
             else:
                 print("Contact is not found in your contact book")
      else:
               break
         
