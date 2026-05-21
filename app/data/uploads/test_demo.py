import sqlite3
import time


password = "admin123"


def get_user(user_id):

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE id = {user_id}"

    cursor.execute(query)

    result = cursor.fetchall()

    conn.close()

    return result


def process_large_list(data):

    results = []

    for i in range(len(data)):

        for j in range(len(data)):

            results.append(data[i] * data[j])

    return results


def blocking_function():

    while True:

        print("Running...")

        time.sleep(5)


def unused_function():

    x = 10

    y = 20

    z = x + y

    return z


if __name__ == "__main__":

    users = get_user(1)

    print(users)

    data = [1, 2, 3, 4, 5]

    print(process_large_list(data))