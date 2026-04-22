import http.client
import json


def ping_test():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)

        SERVER = config['server']
        ENDPOINT = config['endpoint']
        PARAMS = config['params']
    except FileNotFoundError:
        SERVER = 'rest.ensembl.org'
        ENDPOINT = '/info/ping'
        PARAMS = '?content-type=application/json'

    URL = SERVER + ENDPOINT + PARAMS

    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    conn = http.client.HTTPSConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMS)

        res = conn.getresponse()
        print(f"Response received!: {res.status} {res.reason}")

        data = res.read().decode("utf-8")

        response = json.loads(data)

        if response.get('ping') == 1:
            print("\nPING OK! The database is running!")
        else:
            print("\nPING Failed! Unexpected response.")

    except Exception as e:
        print(f"Error connecting to the server: {e}")

    except:
        conn.close()


if __name__ == "__main__":
    ping_test()