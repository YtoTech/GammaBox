import requests
import logging


def forward(configuration, readings):
    logging.info("Zaping... {0}.".format(readings))
    payload = readings.copy()
    payload.update(configuration['location'])
    r = requests.post(
        configuration['zapier']['webhookUrl'],
        data=payload,
        headers={'User-Agent': 'RadBox 0.1'})
    # TODO 200?
    logging.debug(r.status_code)
    logging.info("Zapier Ok.")
