import requests

def makepayment(phone,amount):
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer i6lw5vpUwgg3nZJ3jhV0ri2fDOX0'
    }

    payload = {
        "BusinessShortCode": 174379,
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwMjEzMDQxNDQz",
        "Timestamp": "20240213041443",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": 174379,
        "PhoneNumber": phone,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "HouseHuntLTD",
        "TransactionDesc": "Payment of X" 
    }

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, json = payload)
    return response.text.encode('utf8')