import psycopg2
import config


def connect():
    connection = psycopg2.connect(
        dbname=config.db,
        user=config.user,
        password=config.passwd,
        host=config.host)
    connection.autocommit = True
    return connection


def create_db():
    try:
        connection = connect()
        with connection.cursor() as cursor:
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS category 
                (ID SERIAL, 
                NAME TEXT)
                ''')
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS subcategory 
                (ID SERIAL, 
                PARENT_ID INT,
                NAME TEXT)
                ''')
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS product 
                (ID SERIAL, 
                PARENT_ID INT,
                NAME TEXT, 
                DESCRIPTION TEXT,
                IMAGE TEXT,
                COST FLOAT, 
                COUNT INT, 
                BUY_COST FLOAT, 
                POSITION TEXT,
                BAR_CODE INT)
                ''')
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS users 
                (ID INTEGER PRIMARY KEY, 
                PHONE TEXT,
                FULL_NAME TEXT,
                ADDRESS TEXT,
                STATE TEXT)
                ''')
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS cart 
                (ID INTEGER PRIMARY KEY,
                PRODUCT_ID INT,
                COUNT INT)
                ''')
        print('OK')
    except Exception as _ex:
        print("[INFO] DB ex: ", _ex)
    finally:
        connection.close()


class user():
    def add(tel_id: object, phone: object, full_name: object, address: object) -> object:
        try:
            connection = connect()
            with connection.cursor() as cursor:
                cursor.execute(
                    f"INSERT INTO users (ID, PHONE, FULL_NAME, ADDRESS) VALUES ({tel_id}, '{phone}', '{full_name}', '{address}')")
        except Exception as _ex:
            print("[INFO] DB ex: ", _ex)
        finally:
            connection.close()
        return

    def info(tel_id):
        try:
            connection = connect()
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM users WHERE ID = {tel_id}")
                i = cursor.fetchone()
                _, phone, name, addr, _ = i
                return phone, name, addr
        except TypeError:
            print("Пользователя не существует")
            return None
        except Exception as _ex:
            print("[INFO] DB err in whoim: ", _ex)
        finally:
            connection.close()

    class update():
        def phone(tel_id, phone):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"UPDATE  users SET PHONE = '{phone}' WHERE ID = {tel_id}")
                return
            except Exception as _ex:
                print("[DB][ERR] update user phone: ", _ex)
            finally:
                connection.close()

        def FIO(tel_id, full_name):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"UPDATE  users SET FULL_NAME = '{full_name}' WHERE ID = {tel_id}")
                return
            except Exception as _ex:
                print("[DB][ERR] update user full name: ", _ex)
            finally:
                connection.close()

        def addr(tel_id, address):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"UPDATE  users SET ADDRESS = '{address}' WHERE ID = {tel_id}")
                return
            except Exception as _ex:
                print("[DB][ERR] update user address: ", _ex)
            finally:
                connection.close()

    def check(id):
        try:
            connection = connect()
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT STATE FROM users WHERE ID = {id}")
                i = cursor.fetchone()
                i = str(i[0]).split('|')
                print(i)
                return i
        except Exception as _ex:
            print("[DB][ERR] User check: ", _ex)
        finally:
            connection.close()

    def change_state(id, state):
        try:
            connection = connect()
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE users SET STATE = '{state}' WHERE ID = {id}")
        except Exception as _ex:
            print("[DB][ERR] User change state: ", _ex)
        finally:
            connection.close()
    class cart():
        def __init__(self):
            super().__init__()
            pass
        def delete(self, user_id):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"DELETE FROM cart WHERE ID = {user_id}")
            except Exception as _ex:
                print("[DB][ERR] add all cart: ", _ex)
            finally:
                connection.close()
            return

        def dell_product(self, user_id, prod_id):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"DELETE FROM cart WHERE ID = {user_id} AND PRODUCT_ID = {prod_id}")
            except Exception as _ex:
                print(f"[DB][ERR] del product from cart for user: {user_id}: ", _ex)
            finally:
                connection.close()
            return

        def change_count(self, user_id, prod_id, new_count):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE cart SET COUNT = {new_count} WHERE ID = {user_id} AND PRODUCT_ID = {prod_id}")
            except Exception as _ex:
                print(f"[DB][ERR] change product count in cart for user: {user_id}: ", _ex)
            finally:
                connection.close()
            return
        def add(self, user_id, product_id, count):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO cart (ID, PRODUCT_ID, COUNT) VALUES ({user_id},{product_id},{count}")
            except Exception as _ex:
                print(f"[DB][ERR] add product in cart for user: {user_id}: ", _ex)
            finally:
                connection.close()
        def add_logic(self, user_id, product_id, get_count):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"SELECT COUNT FROM product WHERE ID = {product_id}")
                    has_count = cursor.fetchone()[0][0]
                    count = self.get_count(user_id, product_id)
                    if count != 0:
                        new_count = int(get_count) + int(count)
                        if new_count > has_count:
                            return 0
                        else:
                            self.change_count(user_id, product_id, new_count)
                            return 1
                    else:
                        self.add(user_id, product_id, get_count)
                        return 2
            except Exception as _ex:
                print("[add or edit cart in db]", _ex)
            finally:
                connection.close()

        def get_count(self, user_id, product_id):
            print(self, user_id, product_id)
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"SELECT COUNT FROM cart WHERE ID = {user_id} AND PRODUCT_ID = {product_id}")
                    count = cursor.fetchone()
                    print(count)
                    if count == [] or count is None:
                        return 0
                    else:
                        return count[0][0]
            except Exception as _ex:
                print("[add or edit cart in db]", _ex)
                return 0
            finally:
                connection.close()
        def send(user_id):
            pass

class admin():
    class add():
        def category(name):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO category (NAME) VALUES ('{name}')")
            except Exception as _ex:
                print("[DB][ERR] add category: ", _ex)
            finally:
                connection.close()
            return

        def sub_category(parent_id, name):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO subcategory (PARENT_ID, NAME) VALUES ('{parent_id}', '{name}')")
            except Exception as _ex:
                print("[DB][ERR] add subcategory: ", _ex)
            finally:
                connection.close()
            return

        def product(parent_id, name, description, image, cost, count, buy_cost, position, bar_code):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO product (PARENT_ID, NAME, DESCRIPTION, IMAGE, COST, COUNT, BUY_COST, POSITION, BAR_CODE) VALUES ('{parent_id}', '{name}', '{description}', '{image}', '{cost}', '{count}', '{buy_cost}', '{position}','{bar_code}')")
            except Exception as _ex:
                print("[DB][ERR] add product: ", _ex)
            finally:
                connection.close()
            return
    class delete():
        def category(category_id):
            try:
                connection = connect()
                a = []
                with connection.cursor() as cursor:
                    cursor.execute(f"SELECT ID FROM subcategory WHERE PARENT_ID = {category_id}")
                    a = cursor.fetchall()
                    for i in a:
                        cursor.execute(f"DELETE FROM product WHERE PARENT_ID = {i[0]}")
                        cursor.execute(f"DELETE FROM subcategory WHERE ID = {i[0]}")
                    cursor.execute(f"DELETE FROM category WHERE ID = {category_id}")

            except Exception as _ex:
                print("[DB][ERR] del category: ", _ex)
            finally:
                connection.close()
            return

        def sub_category(sub_id):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"DELETE FROM product WHERE PARENT_ID = {sub_id}")
                    cursor.execute(f"DELETE FROM subcategory WHERE ID = {sub_id}")
            except Exception as _ex:
                print("[DB][ERR] del subcategory: ", _ex)
            finally:
                connection.close()
            return

        def product(prod_id):
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    cursor.execute(f"DELETE FROM product WHERE ID = {prod_id}")
            except Exception as _ex:
                print("[DB][ERR] del product: ", _ex)
            finally:
                connection.close()
            return
    pass


def len_upd():
    try:
        connection = connect()
        cat_ids = []
        sub_cat_id = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT ID FROM category")
            raw = cursor.fetchall()
            for j in raw:
                cat_ids.append(str(j[0]))
            cursor.execute("SELECT ID FROM subcategory")
            row = cursor.fetchall()
            for i in row:
                sub_cat_id.append('sub'+str(i[0]))

        return cat_ids, sub_cat_id
    except Exception as _ex:
        print("[DB][ERR] len upd: ", _ex)
    finally:
        connection.close()


def parse(type_call, call_id):
    print('[pars]', call_id, type(call_id))
    try:
        connection = connect()
        if type_call == 0:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT NAME FROM category WHERE ID = '{call_id}'")
                i = cursor.fetchone()
                return i[0]
        elif type_call == 1:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT NAME FROM subcategory WHERE ID = '{call_id}'")
                i = cursor.fetchone()
                return i[0]
        elif type_call == 2:
            mass = []
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT ID FROM subcategory WHERE PARENT_ID = '{call_id}'")
                raw = cursor.fetchall()
                for i in raw:
                    mass.append(str(i[0]))
                if mass == []:
                    return None
                else:
                    return mass
        elif type_call == 3:
            product_ids = []
            split_list = []
            j = 0
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT ID FROM product WHERE PARENT_ID = '{call_id}'")
                print(call_id)
                raw = cursor.fetchall()
                print(raw)
                for i in raw:
                    product_ids.append(i[0])
                c = len(product_ids) // 5
                if c < len(product_ids) / 5:
                    c = c + 1
                for i in range(c):
                    split = []
                    for j in range(j, j + 5):
                        try:
                            split.append(product_ids[j])
                        except Exception as _ex:
                            print(_ex)
                            pass
                        j = j + 1
                    split_list.append(split)
            return split_list
        elif type_call == 4:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT NAME FROM product WHERE ID = '{call_id}'")
                i = cursor.fetchone()
                return i[0]
        elif type_call == 5:
            #pars parrent id from product id
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT PARENT_ID FROM subcategory WHERE ID = '{call_id}'")
                i = cursor.fetchall()
                print(i[0])
                return int(i[0][0])

    except Exception as _ex:
        print("[DB][ERR] pars: ", _ex)
    finally:
        connection.close()


#work with productor

def cats():
    try:
        connection = connect()
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM category")
            i = cursor.fetchall()
            return i
    except Exception as _ex:
        print("[DB][ERR] pars: ", _ex)
    finally:
        connection.close()


def sub_cats(parent_id):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT ID, NAME FROM subcategory WHERE PARENT_ID = {parent_id}")
            i = cursor.fetchall()
            return i
    except Exception as _ex:
        print("[DB][ERR] pars: ", _ex)
    finally:
        connection.close()


def prods(parent_id):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT ID, NAME FROM product WHERE PARENT_ID = {parent_id}")
            i = cursor.fetchall()
            return i
    except Exception as _ex:
        print("[DB][ERR] pars: ", _ex)
    finally:
        connection.close()


def get_product_card(id):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM product WHERE ID = {id}")
            i = cursor.fetchone()
            return i
    except Exception as _ex:
        print("[DB][ERR] pars: ", _ex)
    finally:
        connection.close()