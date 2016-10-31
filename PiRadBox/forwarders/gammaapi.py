# Forward to https://gamma.ytotech.com/
# See https://github.com/MonsieurV/gamma-api
import requests

def forward(configuration, readings):
    print("Gamma API forwarding... {0}.".format(readings))
    r = requests.post('https://gamma.ytotech.com/api/v1/devices', json={
        'position': {
            'name': configuration['location']['name'],
            'latitude': float(configuration['location']['latitude']),
            'longitude': float(configuration['location']['longitude'])
        },
        'manufacturer': 'Radiation Watch',
        'model': 'Pocket Geiger Type 5',
        'sensor': 'FirstSensor X100-7 SMD'
    }, headers={ 'User-Agent': 'RadBox 0.1' },
    auth=(
        configuration['gammaapi']['username'],
        configuration['gammaapi']['password']))
    if r.status_code is not 200 and r.status_code is not 201:
        print("Gamma API Failed create device.", r.json())
        return
    r = requests.post('https://gamma.ytotech.com/api/v1/events', json={
        'type': 'gamma',
        'timestamp': readings['timestamp'],
        'deviceId': r.json()['_id']
    }, headers={ 'User-Agent': 'RadBox 0.1' },
    auth=(
        configuration['gammaapi']['username'],
        configuration['gammaapi']['password']))
    if r.status_code is 201:
        print("Gamma API Ok.")
    else:
        print("Gamma API Failed", r.text)
