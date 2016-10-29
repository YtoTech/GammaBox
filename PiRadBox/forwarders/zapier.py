import requests

def forward(configuration, readings):
    print("Zaping... {0}.".format(readings))
    payload = readings.copy()
    payload.update(configuration['location'])
    r = requests.post(configuration['zapier']['webhookUrl'], data=payload,
        headers={ 'User-Agent': 'RadBox 0.1' })
    # TODO 200?
    print(r.status_code)
    print("Zapier Ok.")
