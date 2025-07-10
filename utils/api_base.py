from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import playwright

Orderspayload = {"orders": [{"country": "India", "productOrderedId": "67a8dde5c0d3e6622a297cc8"}]}


class APIutils:

    def get_token(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/auth/login",data = {"userEmail": "rahulshetty@gmail.com","userPassword":"Iamking@000"})
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body['token']

    def createOrder(self,playwright:Playwright):
        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=Orderspayload,headers={"Authorization":token,
                                 "content-type":"application/json"})
        response_body = response.json()
        order_id = response_body['orders']
        return order_id



