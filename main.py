import cbpro

import mysql.connector
public_client = cbpro.PublicClient()


btc_data = None
eth_data = None
mydb = mysql.connector.connect(
    host="mysql",
    port="3306",
    user="root",
    password="vitten",
    database="trading"
)
mycursor = mydb.cursor()

while True:
    btc_result = public_client.get_product_ticker("BTC-EUR")
    if btc_data!=btc_result:
        btc_data=btc_result
        print("[BTC] new data".format(btc_result))
        mycursor = mydb.cursor()
        sql = "INSERT INTO btc_tricker (ask, bid, volume, price, size) VALUES (%s,%s,%s,%s,%s);"
        val = (float(btc_result["ask"]), float(btc_result["bid"]), float(btc_result["volume"]), float(btc_result["price"]), float(btc_result["size"]),)
        mycursor.execute(sql, val)
        mydb.commit()
    eth_result = public_client.get_product_ticker("ETH-EUR")
    if eth_data != eth_result:
        eth_data = eth_result
        print("[ETH] new data".format(eth_data))
        mycursor = mydb.cursor()
        sql = "INSERT INTO eth_tricker (ask, bid, volume, price, size) VALUES (%s,%s,%s,%s,%s);"
        val = (
        float(eth_result["ask"]), float(eth_result["bid"]), float(eth_result["volume"]), float(eth_result["price"]),
        float(eth_result["size"]),)
        mycursor.execute(sql, val)
        mydb.commit()
