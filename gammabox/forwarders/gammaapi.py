# Forward to https://gamma.ytotech.com/
# See https://github.com/MonsieurV/gamma-api
import logging
import requests


def forward(configuration, readings):
    logging.info("Gamma API forwarding... %s", readings)
    request = requests.post(
        "https://gamma.ytotech.com/api/v1/devices",
        json={
            "position": {
                "name": configuration["location"]["name"],
                "latitude": float(configuration["location"]["latitude"]),
                "longitude": float(configuration["location"]["longitude"]),
            },
            "manufacturer": "Radiation Watch",
            "model": "Pocket Geiger Type 5",
            "sensor": "FirstSensor X100-7 SMD",
        },
        headers={"User-Agent": "RadBox 0.1"},
        auth=(
            configuration["gammaapi"]["username"],
            configuration["gammaapi"]["password"],
        ),
    )
    if request.status_code != 200 and request.status_code != 201:
        logging.error("Gamma API Failed create device: %s", request.json())
        return
    request = requests.post(
        "https://gamma.ytotech.com/api/v1/events",
        json={
            "type": "gamma",
            "timestamp": readings["timestamp"],
            "deviceId": request.json()["_id"],
        },
        headers={"User-Agent": "RadBox 0.1"},
        auth=(
            configuration["gammaapi"]["username"],
            configuration["gammaapi"]["password"],
        ),
    )
    if request.status_code == 201:
        logging.info("Gamma API Ok.")
    else:
        logging.error("Gamma API Failed: %s", request.text)
