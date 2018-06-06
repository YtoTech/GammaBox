import logging
import requests


def forward(configuration, readings):
    logging.info("Zaping... %s.", readings)
    payload = readings.copy()
    payload.update(configuration["location"])
    request = requests.post(
        configuration["zapier"]["webhookUrl"],
        data=payload,
        headers={"User-Agent": "RadBox 0.1"},
    )
    # TODO 200?
    if request.status_code < 300:
        logging.info("Zapier Ok.")
    else:
        logging.error("Zapier failed: %s - %s", request.status_code, request.text)
