import json
from log_reg_service import current_user
# from users_service import purchase_product

PRODUCT_FILE_PATH = "./db/product.txt"

def get_products():
    with open(PRODUCT_FILE_PATH, 'r') as file:
        list_products = []
        for product_line in file:
            list_products.append(json.loads(product_line.strip()))
    return list_products

def buy_product(b):
    with open(PRODUCT_FILE_PATH, 'r+') as file:
        for product_to_buy in file:
            current_prod = json.loads(product_to_buy.strip())
            if current_prod['id'] == b:
                with open('./db/users.txt', 'r+') as file_users:
                    shopping_user = current_user()
                    result = []
                    for user_line in file_users:
                        user_obj = json.loads(user_line.strip())
                        if user_obj['username'] == shopping_user:
                            user_obj['product'].append(b)
                            result.append(json.dumps(user_obj) + "\n")
                        else:
                            result.append(user_line)

                    file_users.seek(0)
                    file_users.truncate()
                    file_users.writelines(result)
