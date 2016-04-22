# See https://sourceforge.net/p/pyradmon-reborn/code/ci/master/tree/PyRadmon%20-%20No%20Audio/PyRadmon.py#l464
# Create a lib specifically to wrap the Radmon "API", so we can easily publish
# in a high-level fashion.
import requests

def forward(configuration, readings):
    print("Radmoning... {0}.".format(readings))
    r = requests.get('http://www.radmon.org/radmon.php', params={
        user: configuration['radmon']['username'],
        password: configuration['radmon']['password'],
        function: 'submit',
        datetime: datetime.datetime.strptime(readings['timestamp'],
            "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d%%20%H:%M:%S"),
        value: readings['cpm'],
        unit: 'CPM'
    }, headers={ 'User-Agent': 'RadBox 0.1' })
    # TODO 200?
    print(r.status_code)
    if 'incorrect login' in r.text.lower():
        raise RuntimeError('Bad login-password combination for radmon.org')
    else:
        print("Radmon Ok.")
