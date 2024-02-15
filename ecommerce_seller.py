import json

def add_product(username):
    product_name = input('Enter product name:')
    product_discription = input('Enter product discription:')
    product_price = input('Enter product price:')

    product_dict_data = {'product_name':product_name, 'product_desc':product_discription, 'product_price':product_price}
    product_json_data = json.dumps(product_dict_data)
    f = open('D:/Python With Django/Mind Riser/file/productdata.txt', 'a')

    f.write(product_json_data + '-')

    f.close()


def seller_product_bills(username):
    f = open('D:/Python With Django/Mind Riser/file/bill.txt', 'r')

    bill_json_data = f.read()
    f.close()