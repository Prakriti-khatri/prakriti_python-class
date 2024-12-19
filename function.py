def store_contact(name,number,contacts={}):
 contacts[name]=number
 return contacts
def phone_book():
   contacts={}
   while True:
      name=input("enter a name")
      number=input("enter a number")
      contacts=store_contact(name,number,contacts)

      user_choice=input("""
    do you want to exit
1.yes
2.no""")
      if user_choice=="1":
        return contacts
my_contact_book=phone_book()
def get_phone_number(name,contacts):
 return contacts.get(name.lower())
user_name=input("enter name to find phone nuber")
print(get_phone_number(user_name,my_contact_book))
   
   
   
phone_book()
   
