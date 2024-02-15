# Requirment
# Ask user if he or she wants to login or register
# If register : Ask username, password, user type (Buyer/Seller) and store it in a file.
# Login : Ask the username and password , if username and password exist userdata file them print Login sucessful. check the usertype. 
# If the user is buyer, give him choice: view product, view his/her bills, purchase product. 
#If the user is seller: Add product ,views his /her products bills.
# View bills - Only bills which has the buyer value same as login user should be printed
# Seller - Give seller view products choice and if he/she enters view product , list the product of the logged in seller



import json
from ecommerce_buyer import view_all_products, view_bills
from ecommerce_seller import add_product, seller_product_bills


def register():
    user_name = input('Enter your username :')
    user_password = input('Create a password :')
    user_type = input('Are yoy a buyer or seller ?').lower()

    user_data = {"user_name":user_name,"user_password":user_password, "user_type": user_type}
    json_user_data = json.dumps(user_data)

    f = open('D:/Python With Django/Mind Riser/file/userdata.txt','a')
    f.write(json_user_data +'-')
    f.close()
    user_log = input("Do you want to login [y/n] :").lower()
    if user_log == "y":
        login()
    else:
        print("Registered Successfully")

        
def login():
    user_name = input('Enter your username:')
    user_password = input('Enter your password:')

    f = open('D:/Python With Django/Mind Riser/file/userdata.txt','r')
    json_user_data = f.read()
    f.close()
    list_user_data = json_user_data.split('-')
    user_login = False
    for i in list_user_data:
        if  i!= '':
            dict_data = json.loads(i)
            if (user_name == dict_data.get("user_name")) and user_password == dict_data.get("user_password"):
                    user_login = True
                    type = dict_data.get("user_type")
                    break

            
    if user_login == True:
        print('Login Successfull')
        if type == "buyer":
            print(f"Hi {dict_data.get('user_name')}! Welcome to your buyer account.")
            print("What would you like to do?")
            user_operation = input ("[view product/ view bills] :").lower()
            if user_operation == "view product" or user_operation == "view products":
                view_all_products(user_name)
            elif user_operation == "view bill" or user_operation == "view bills":
                view_bills()
            elif user_operation == "purchase":
                purchase()
            else:
                print("Invalid Operation!! Please try again.")
        else:
            print(f"Hii {dict_data.get('user_name')}! Welcome to your seller account.")
            print("What would you like to do?")
            user_operation = input("[add product/ view bills]:").lower()
            if user_operation == "add product" or user_operation == "add products":
                add_product()
            elif user_operation == "view bill" or user_operation == "view bills":
                view_bills()
            else:
                print('Invalid Slection')

 
    else:
        print("Invalid Credentials")
            



def purchase(username):
    purchase_product_name = input('Which product do you want to buy?')
    purhcase_quantity = int(input('how much quantity'))

    f = open('D:/Python With Django/Mind Riser/file/productdata.txt', 'a')

    product_json_data = f.read()

    f.close()

    list_product_data = product_json_data.split('-')
    available = False
    product_dict_data = None
    for i in list_product_data:
        if i !='':
            dict_data = json.loads(i)
            if purchase_product_name == dict_data['product_name']:
                available = True
                product_dict_data = dict_data
                price = int(dict_data['product_price'])

        if available == True:
            print('Purchase Completed')
            a = purhcase_quantity * price 
            print(f'Your total amount is {a}')

        
            
            bill_data = {'buyer':username, 'product':product_dict_data.get('produc_name'), 'quantity':purhcase_quantity, 'prroduct_price':product_dict_data.get('product_price'),'total':a}
            bill_json_data = json.dumps(bill_data)
            f = open('D:/Python With Django/Mind Riser/file/bill.txt', 'a')
            f.write(bill_json_data +'-')
            f.close()

        else:
            print('Invalid product name!')
            purchase(username)



def view_products():
    pass


user_input = input("Do you want to login or register?").lower()

if user_input == "register":
    register()

if user_input == "login":
    login()







