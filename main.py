# vazifa1----------------------


import psycopg2
import serial

db_name = 'pythonProject8'
password = '1234'
host = 'localhost'
port = 5432
user = 'postgres'


conn = psycopg2.connect(dbname=db_name,
                        password=password,
                        host=host,
                        port=port,
                        user=user)

cur = conn.cursor()

created_table_query = """ create table if not exists products(
    id bigserial,
    namee varchar(128),
    price varchar(128),
    color varchar(128),
    image varchar(128)
);
"""


# vazifa2----------------------

def save(self):
    db_name = 'pythonProject8'
    password = '1234'
    host = 'localhost'
    port = 5432
    user = 'postgres'

    conn = psycopg2.connect(dbname=db_name,
                            password=password,
                            host=host,
                            port=port,
                            user=user)
    cur = conn.cursor()

    u = (input('id >'))
    e = input('name>')
    x = (u, e)
    insert_user_query = """ insert into users(id,namee)
                            values (%s,%s);"""
    cur.execute(insert_user_query,x)
    conn.commit()
    conn.close()


def insert_product(self):
    db_name = 'pythonProject8'
    password = '1234'
    host = 'localhost'
    port = 5432
    user = 'postgres'

    conn = psycopg2.connect(dbname=db_name,
                            password=password,
                            host=host,
                            port=port,
                            user=user)

    cur = conn.cursor()
    insert_query = """insert into users(username,age,email)
                     values (%s,%s);"""


def select_all_products(self):
    db_name = 'pythonProject8'
    password = '1234'
    host = 'localhost'
    port = 5432
    user = 'postgres'

    conn = psycopg2.connect(dbname=db_name,
                            password=password,
                            host=host,
                            port=port,
                            user=user)

    cur = conn.cursor()

    select_all_product = """select * from users"""
    cur.execute(select_all_product)

# vazifa3----------------------


class Alphabet:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 26:
            h = 'abcdefghijklmnopqrstuvwxyz'
            l = h[self.index]
            self.index += 1
            return l
        else:
            raise StopIteration


alphabet_iterator = Alphabet()
for l in alphabet_iterator:
    print(l)

# vazifa4----------------------


import threading
import time


def number(start, end):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)


def letter():
    letters = 'ABCDE'
    for l in letters:
        print(l)
        time.sleep(1)


def printt():
    t1 = threading.Thread(target=number, args=(1, 5))
    t2 = threading.Thread(target=letter)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


printt()

# vazifa5----------------------
pass

# vazifa6----------------------


import psycopg2


class ConnectDb:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


with ConnectDb('pythonProject8', 'postgres', '1234', 'localhost', '5432') as (conn, cur):
    cur.execute("SELECT * FROM my_table")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# vazifa7----------------------


import psycopg2
import requests

url = "https://dummyjson.com/products/"
respons = requests.get(url)

db_name = 'pythonproject8'
password = '1234'
host = 'localhost'
port = 5432
user = 'postgres'
conn = psycopg2.connect(dbname=db_name,
                        password=password,
                        host=host,
                        port=port,
                        user=user)

cur = conn.cursor()
create_table_query = """CREATE TABLE IF NOT EXISTS url(
                    id serial primary key,
                    title varchar(50),
                    description varchar(128),
                    category varchar (120),
                    price int
                    discountPercentage int
                    rating int,
                    stock int,
                    tags varchar(128),
                    sku varchar(128),
                    weight int,
                    dimensions varchar(128),
                    warrantyInformation varchar(128),
                    shippingInformation varchar(128),
                    availabilityStatus varchar(128),
                    reviews varchar(128),
                    returnPolicy varchar(128),
                    minimumOrderQuantity varchar(128),
                    meta varchar(128),
                    )"""


insert_into_query = """INSERT INTO url(id,title,description,category,price,discountPercentage,rating,stock,tags,sku,weight,dimensions,warrantyInformation,shippingInformation,availabilityStatus,reviews,returnPolicy,minimumOrderQuantity,meta)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
for user in respons.json()['users']:
    cur.execute(insert_into_query)
    conn.commit()
