import SafecastPy

def forward(configuration, readings):
    print("Safecasting... {0}.".format(readings))
    if configuration['safecast']['production']:
        safecastInstance = SafecastPy.PRODUCTION_API_URL
    else:
        safecastInstance = SafecastPy.DEVELOPMENT_API_URL
    safecast = SafecastPy.SafecastPy(
        api_key=configuration['safecast']['apiKey'], api_url=safecastInstance)
    # TODO Allows to configurate the device.
    device_id = safecast.add_device(json={
        'manufacturer': 'Radiation Watch',
        'model': 'Pocket Geiger Type 5',
        'sensor': 'FirstSensor X100-7 SMD'
    }).get('id')
    # TODO Get location from configuration.
    payload = {
        'latitude': configuration['location']['latitude'],
        'longitude': configuration['location']['longitude'],
        'value': readings['uSvh'],
        'unit': SafecastPy.UNIT_USV,
        'captured_at': readings['timestamp'],
        'device_id': device_id,
    }
    if configuration['location']['name']:
        payload['location_name'] = configuration['location']['name']
    if configuration['location']['height']:
        payload['height'] = configuration['location']['height']
    measurement = safecast.add_measurement(json=payload)
    print("Safecast Ok. Measurement published with id {0}".format(
                    measurement['id']))
