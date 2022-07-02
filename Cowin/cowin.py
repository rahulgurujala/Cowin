from typing import Generator
from requests import Session, Response
from datetime import date


class Cowin:
    def states(self) -> Response:
        """states method

        Returns:
            Response: This method return Response object of state codes.
        """

        session = Session()
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "content-type": "application/json; charset=utf-8",
        }
        return session.get(
            "https://cdn-api.co-vin.in/api/v2/admin/location/states", headers=headers
        )

    def districts(self, state_id: int) -> Response:
        """Districts method

        Args:
            state_id (int): State id

        Returns:
            Response: This method return Response object of districts codes.
        """
        session = Session()
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "content-type": "application/json; charset=utf-8",
        }
        return session.get(
            f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}",
            headers=headers,
        )

    def slotes(self, district_id: int, date: date) -> Response:
        """Slots method

        Args:
            district_id (int): District id
            date (date): date object

        Returns:
            Response: This method return Response object of data.
        """
        session = Session()
        date = date.strftime("%d-%m-%Y")
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "content-type": "application/json; charset=utf-8",
        }
        return session.get(
            f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date}",
            headers=headers,
        )

    def avail_slots(self, district_id: int, date: date) -> Generator:
        """avail_slots method

        Args:
            district_id (int): district id
            date (date): date object

        Returns:
            Generator: This method return Generator object of data
        """
        slotes = self.slotes(district_id, date).json()

        for center in slotes["centers"]:
            avail = center["sessions"][0]["available_capacity"]

            if isinstance(avail, int) and avail > 0:
                yield {
                    "Message": "Slot/s Available",
                    "Center Name": center["name"],
                    "Block Name": center["block_name"],
                    "Pincode": center["pincode"],
                    "Available Slotes": avail,
                    "Fee Type": center["fee_type"],
                    "Slot Timing": center["sessions"][0]["slots"],
                    "Min Age Group": center["sessions"][0]["min_age_limit"],
                    "Vaccine Name": center["sessions"][0]["vaccine"],
                    "First Dose Capacity": center["sessions"][1][
                        "available_capacity_dose1"
                    ],
                    "Second Dose Capacity": center["sessions"][1][
                        "available_capacity_dose2"
                    ],
                    "Fees": [
                        [
                            {"Vaccine": fee["vaccine"], "Fees": fee["fee"]}
                            for fee in center["vaccine_fees"]
                        ][0]
                        if "vaccine_fees" in center
                        else None
                    ],
                }

            else:
                yield {
                    "Message": "Slots Not Available",
                    "Center Name": center["name"],
                    "Block Name": center["block_name"],
                }

        return "Booking not available"


if __name__ == "__main__":
    cowin = Cowin()

    # bidar = cowin.avail_slots(395, date(2021, 6, 1))
    # print('Mumbai', [i for i in bidar])
    print(list(cowin.avail_slots(392, date(2021, 6, 1))))
