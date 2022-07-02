from requests import Response
import requests
import hashlib
import json

BASE_API_URL = "https://cdn-api.co-vin.in/api/"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}


def generate_otp(mobile_num: str) -> Response:

    payload = json.dumps({"mobile": mobile_num})
    return requests.request(
        "POST",
        f"{BASE_API_URL}v2/auth/public/generateOTP",
        headers=headers,
        data=payload,
    )


def confirm_otp(otp: int, txnId: str) -> Response:

    payload = json.dumps(
        {
            "otp": hashlib.sha256(bytes(otp, encoding="utf-8")).hexdigest(),
            "txnId": txnId,
        }
    )
    return requests.request(
        "POST",
        f"{BASE_API_URL}v2/auth/public/confirmOTP",
        headers=headers,
        data=payload,
    )


txnId = generate_otp("7506329256")
otp = input("Please enter your otp: ")
token = confirm_otp(otp, txnId.json()["txnId"])
with open("credentials.py", "w") as f:
    f.write(
        f"""
        txtID = {txnId}
        token = {token}
    """
    )
