import json
import threading
import datetime
from .forwarders import twitter, safecast, plotlyf, radmon, zapier

class Forwarder(object):
    """Forward the Geiger Counter readings to miscellaneous external
    services.
    In a better world, this should be an independant application (like an Erlang one)
    that receives the readings through a broker (like ZeroMQ) and then dispatch them
    to the several ends. Here we may have threading issues, and it may not be totally
    reliable."""
    def __init__(self, configurationFileName):
        self.configurationFileName = configurationFileName
        self.configuration = None
        self.nextPublicationAt = datetime.datetime.now()
        self.reloadConfiguration()

    def reloadConfiguration(self):
        with open(self.configurationFileName, 'rb') as f:
            self.configuration = json.load(f)
        self.nextPublicationAt = datetime.datetime.now()

    def dispatch(self, readings):
    	# Prevent to publish zeros.
    	if readings['uSvh'] <= 0:
    		return
        # TODO Do something to choose when to dispatch following the integration.
        if self.configuration['zapier']['enabled']:
            self.runForwarder(zapier.forward, self.configuration, readings)
        # Do the time have elapsed since last publication?
        if datetime.datetime.now() > self.nextPublicationAt:
            self.doDispatch(readings)
            self.nextPublicationAt = datetime.datetime.now() \
                + datetime.timedelta(
                    minutes=int(self.configuration['publication']['period']))

    def doDispatch(self, readings):
        # Naive dispatching.
        if self.configuration['twitter']['enabled']:
            self.runForwarder(twitter.forward, self.configuration, readings)
        if self.configuration['safecast']['enabled']:
            self.runForwarder(safecast.forward, self.configuration, readings)
        if self.configuration['plotly']['enabled']:
            self.runForwarder(plotlyf.forward, self.configuration, readings)
        if self.configuration['radmon']['enabled']:
            self.runForwarder(radmon.forward, self.configuration, readings)

    def runForwarder(self, f, configuration, readings):
        threading.Thread(target=f, args=(configuration, readings)).start()
