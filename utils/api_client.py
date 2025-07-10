import requests


class APIClient:
    def __init__(self,base_url,token=None):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
        if token:
            self.headers['Authorization'] = f'Bearer {token}'

    def post(self,endpoint,data):
        response = requests.post(f"{self.base_url}{endpoint}",json=data,headers=self.headers)
        return response


    def get(self,endpoint):
        get_response = requests.get(f"{self.base_url}{endpoint}",headers=self.headers)
        assert get_response.status_code == 200
        return get_response

    def put(self, endpoint, data,headers=None):
        if headers is None:
            headers = self.headers
        response = requests.put(f"{self.base_url}{endpoint}", json=data, headers= headers)
        return response