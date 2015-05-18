import requests
import json


class GetInformation:

    def __init__(self):
        pass

    def make_requests(self):
        response = requests.get("https://hackbulgaria.com/api/students/")
        data = json.loads(response.text)
        return data

if __name__ == '__main__':
    a = GetInformation()
    print(a.make_requests())
