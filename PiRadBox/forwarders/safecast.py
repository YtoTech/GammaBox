import SafecastPy
import datetime

def forward(configuration, readings):
    print("Safecasting... {0}.".format(readings))
    if configuration['production']:
        SAFECAST_INSTANCE = SafecastPy.PRODUCTION_API_URL
    else:
        SAFECAST_INSTANCE = SafecastPy.DEVELOPMENT_API_URL
    safecast = SafecastPy.SafecastPy(api_key=API_KEY, api_url=SAFECAST_INSTANCE)
    # TODO Allows to configurate the device.
    device_id = safecast.add_device(json={
        'manufacturer': 'Radiation Watch',
        'model': 'Pocket Geiger Type 5',
        'sensor': 'FirstSensor X100-7 SMD'
    }).get('id')
    # TODO Get location from configuration.
    payload = {
        'latitude': MY_LOCATION['latitude'],
        'longitude': MY_LOCATION['longitude'],
        'value': readings['uSvh'],
        'unit': SafecastPy.UNIT_USV,
        'captured_at': datetime.datetime.utcnow().isoformat() + '+00:00',
        'device_id': device_id,
    }
    if MY_LOCATION_NAME:
        payload['location_name'] = MY_LOCATION_NAME
    if HEIGHT:
        payload['height'] = HEIGHT
    measurement = safecast.add_measurement(json=payload)
    print("Safecast Ok. Measurement published with id {0}".format(
                    measurement['id']))
