# See https://sourceforge.net/p/pyradmon-reborn/code/ci/master/tree/PyRadmon%20-%20No%20Audio/PyRadmon.py#l464
# Create a lib specifically to wrap the Radmon "API", so we can easily publish
# in a high-level fashion.
import requests
import datetime
import logging

def forward(configuration, readings):
    logging.info("Radmoning... {0}.".format(readings))
    payload = {
        'user': configuration['radmon']['username'],
        'password': configuration['radmon']['password'],
        'function': 'submit',
        'datetime': datetime.datetime.strptime(readings['timestamp'],
            "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d%%20%H:%M:%S"),
        'value': readings['cpm'],
        'unit': 'CPM'
    }
    logging.debug(datetime.datetime.strptime(readings['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ"))
    logging.info(payload)
    r = requests.get('http://www.radmon.org/radmon.php', params=payload,
        headers={ 'User-Agent': 'RadBox 0.1' })
    if r.status_code != 200 or 'incorrect login' in r.text.lower():
        raise RuntimeError('{0}: Bad login-password combination for radmon.org'.format(
            r.status_code))
    else:
        logging.info("Radmon Ok.")
