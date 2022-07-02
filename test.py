data = {
    "center_id": 594392,
    "name": "H N Reliance Hospital",
    "address": "Raja Rammohan Roy Road Prarthana Samaj Girgaon",
    "state_name": "Maharashtra",
    "district_name": "Mumbai",
    "block_name": "Ward C Corporation - MH",
    "pincode": 400004,
    "lat": 18,
    "long": 72,
    "from": "09:00:00",
    "to": "13:00:00",
    "fee_type": "Paid",
    "sessions": [
        {
            "session_id": "58041469-5e19-46f8-a89f-f47339b1edd6",
            "date": "17-05-2021",
            "available_capacity": 50,
            "min_age_limit": 45,
            "vaccine": "COVISHIELD",
            "slots": [
                "09:00AM-10:00AM",
                "10:00AM-11:00AM",
                "11:00AM-12:00PM",
                "12:00PM-01:00PM",
            ],
            "available_capacity_dose1": 0,
            "available_capacity_dose2": 50,
        },
        {
            "session_id": "d47b54ac-63b1-418c-a914-1bb8875b2427",
            "date": "17-05-2021",
            "available_capacity": 21,
            "min_age_limit": 18,
            "vaccine": "COVISHIELD",
            "slots": [
                "09:00AM-10:00AM",
                "10:00AM-11:00AM",
                "11:00AM-12:00PM",
                "12:00PM-01:00PM",
            ],
            "available_capacity_dose1": 0,
            "available_capacity_dose2": 21,
        },
    ],
    "vaccine_fees": [{"vaccine": "COVISHIELD", "fee": "700"}],
}


def el(e):
    fees = []
    if "vaccine_fees" in e:
        fees.extend(
            {"Vaccine": fee["vaccine"], "Fees": fee["fee"]} for fee in e["vaccine_fees"]
        )

    return fees


# d = el(data)

d = [
    [{"Vaccine": fee["vaccine"], "Fees": fee["fee"]} for fee in data["vaccine_fees"]][0]
    if "vaccine_fees" in data
    else None
]

print(d)
