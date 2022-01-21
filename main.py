"""
A simple IP address locator created by KryptonK#3428
Features: Stores information in a json file + Easy and fast.
"""
import os
import requests
import json

class IpLocator(object):

    def __init__(self, IP: str) -> None:
        self.clear = lambda: os.system("cls; clear")
        self.session = requests.Session()
        self.IP = IP
        self.URL = "https://ipinfo.io/{}".format(self.IP)

    def get_data(self):
        try:
            self.clear()
            data = self.session.get(
                self.URL
            ).json()
            json.dump(data, open("{}_info.json".format(self.IP), "w+"), indent=4)
            print("Finished dumping {}'s data.".format(self.IP)); input(); os._exit(0)
        except Exception as error:
            print("> Error: {}".format(error))

if __name__ == "__main__":
    client = IpLocator(
        IP = input("> IP Address: ")
    )
    client.get_data()
