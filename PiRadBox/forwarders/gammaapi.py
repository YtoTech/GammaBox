# Forward to https://gamma.ytotech.com/
# See https://github.com/MonsieurV/gamma-api
import requests

def forward(configuration, readings):
    print("Gamma API forwarding... {0}.".format(readings))
    r = requests.post('https://gamma.ytotech.com/api/v1/events', json={
        'position': {
            'latitude': configuration['location']['latitude'],
            'longitude': configuration['location']['longitude']
        },
        'type': 'gamma',
        'timestamp': readings['timestamp']
    }, headers={ 'User-Agent': 'RadBox 0.1' },
    auth=(
        configuration['gammaapi']['username'],
        configuration['gammaapi']['password']))
    if r.status_code is 201:
        print("Gamma API Ok.")
    else:
        print("Gamma API Failed", r.text)
