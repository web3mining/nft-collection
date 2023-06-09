import requests
import time
import sqlite3


def create_table():
    conn = sqlite3.connect('hashrate.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS hashrate
                 (user text, worker text, hashrate real, hashrate1h real, hashrate24h real, lastbeat int, reject real, active int)''')
    conn.commit()
    conn.close()


def insert_data(data):
    conn = sqlite3.connect('hashrate.db')
    c = conn.cursor()
    for row in data['details']:
        c.execute("INSERT INTO hashrate VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (row['user'], row['worker'], row['hashrate'], row['hashrate1h'], row['hashrate24h'], row['lastbeat'], row['reject'], row['active']))
    conn.commit()
    conn.close()


API_URL = 'https://api.emcd.io/v1/btc/workers/c9390e75-1845-4066-a510-47785af028c6'
INTERVAL = 3600


def main():
    while True:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            create_table()
            insert_data(data)
        time.sleep(INTERVAL)


if __name__ == '__main__':
    main()
