import json

def view_all_products(username):
    f = open('D:/Python With Django/Mind Riser/file/productdata.txt', 'r')

    product_json_data = f.read

    f.close()

    list_product_data = product_json_data.split('-')

    for i in list_product_data:
        print(i)
    
def view_bills(username):
    f = open('D:/Python With Django/Mind Riser/file/bill.txt')
    bill_json_data = f.read()
    f.close()
   
    bill_list_data = bill_json_data.split('-')

    # bill_list_data = [bill for bill in bill_json_data["bills"] if bill["buyer"] == username]
    for i in bill_list_data:
         if i !="":
            dict_data = json.loads(i)
            if username == dict_data.get('buyer'):
                print(dict_data)
            
