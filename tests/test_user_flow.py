import json

from tests.conftest import config, check_inDate
from utils.auth_helper import *

class TestBooking:
    def create_booking(self,api_client,config,check_inDate,check_outDate):
        self.checkIndate = check_inDate
        self.checkOutdate = check_outDate
        self.data = {
        "firstname" : "John",
        "lastname" : "White",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : self.checkIndate,
            "checkout" : self.checkOutdate
            }
        }
        create_booking = api_client.post("/booking",self.data)
        assert create_booking.status_code == 200
        self.booking_details = create_booking.json()
        print("Before Updating Booking First Name: ",self.booking_details)

    def update_booking(self,api_client,check_inDate,check_outDate,get_Token):
        token = get_Token
        bookingInfo = self.booking_details
        booking_id = bookingInfo['bookingid']
        self.checkIndate = check_inDate
        self.checkOutdate = check_outDate
        self.data = {
            "firstname" : "Jack",
            "lastname" : "White",
            "totalprice" : 111,
            "depositpaid" : True,
            "bookingdates" : {
                "checkin" : self.checkIndate,
                "checkout" : self.checkOutdate
                }
            }
        self.headers = {
            "Content-Type": "application/json",
            "Accept" : "application/json",
            "Cookie": f"token={token}"
        }
        update_booking = api_client.put(f"booking/{booking_id}",self.data,self.headers)
        assert update_booking.status_code == 200
        assert self.data['firstname'] == update_booking.json()['firstname']
        self.updated_Name = update_booking.json()['firstname']
        self.updated_Booking_Info = update_booking.json()
        print("After Updating Booking First Name: ",self.updated_Booking_Info)


    def get_booking(self,api_client):
        bookingInfo = self.booking_details
        booking_id = bookingInfo['bookingid']
        get_booking = api_client.get(f"booking/{booking_id}")
        assert get_booking.status_code == 200
        assert self.updated_Name == get_booking.json()['firstname']
        get_Booking_info = get_booking.json()
        print("After Update getting the latest booig details: ",self.updated_Booking_Info)
        for key in ['firstname', 'lastname', 'totalprice', 'depositpaid']:
            assert get_Booking_info[key] == self.updated_Booking_Info[key], f"Mismatch in '{key}': {get_Booking_info[key]} != {self.updated_data[key]}"
        for key in ['checkin','checkout']:
            assert get_Booking_info['bookingdates'][key] == self.updated_Booking_Info['bookingdates'][key],f"Mismatch in bookingdates.{key}: {get_Booking_info['bookingdates'][key]} != {self.updated_Booking_Info['bookingdates'][key]}"


    def test_full_booking_flow(self,config,api_client,check_inDate,check_outDate,get_Token):
        self.create_booking(api_client,config,check_inDate,check_outDate)
        self.update_booking(api_client,check_inDate,check_outDate,get_Token)
        self.get_booking(api_client)


