import json
import threading
import datetime
from .forwarders import twitter, safecast, plotlyf, radmon, gammaapi, zapier


class Forwarder(object):
    """Forward the Geiger Counter readings to miscellaneous external services.
    In a better world, this should be an independant application
    (like an Erlang one) that receives the readings through a broker
    (like ZeroMQ) and then dispatch them to the several ends.
    Here we may have threading issues, and it may not be totally
    reliable."""

    def __init__(self, configurationFileName):
        self.configurationFileName = configurationFileName
        self.configuration = None
        self.nextPublicationAt = datetime.datetime.now()
        self.reloadConfiguration()

    def reloadConfiguration(self):
        try:
            with open(self.configurationFileName, 'rb') as f:
                self.configuration = json.load(f)
        except Exception as e:
            # TODO Use a true logger.
            print('Failed to load configuration file {}. Cause:'.format(
                self.configurationFileName))
            print(e)
            self.configuration = None
        self.nextPublicationAt = datetime.datetime.now()

    def dispatch(self, readings):
        # Prevent to publish zeros and not stabilized data.
        if readings['uSvh'] <= 0 or readings['duration'] < 120:
            return
        # No forwarding if configuration has not been initialized.
        if not self.configuration:
            return
        # Do the time have elapsed since last publication?
        if datetime.datetime.now() > self.nextPublicationAt:
            self.doDispatch(readings, True)
            self.nextPublicationAt = datetime.datetime.now() \
                + datetime.timedelta(
                    minutes=int(self.configuration['publication']['period']))
        else:
            self.doDispatch(readings, False)

    def doDispatch(self, readings, periodElapsed):
        # Naive dispatching.
        if periodElapsed:
            if self.configuration['twitter']['enabled']:
                self.runForwarder(twitter.forward, self.configuration,
                                  readings)
            if self.configuration['safecast']['enabled']:
                self.runForwarder(safecast.forward, self.configuration,
                                  readings)
            if self.configuration['radmon']['enabled']:
                self.runForwarder(radmon.forward, self.configuration, readings)
        if self.configuration['plotly']['enabled']:
            self.runForwarder(plotlyf.forward, self.configuration, readings)
        if self.configuration['gammaapi']['enabled']:
            self.runForwarder(gammaapi.forward, self.configuration, readings)
        if self.configuration['zapier']['enabled']:
            self.runForwarder(zapier.forward, self.configuration, readings)

    def runForwarder(self, f, configuration, readings):
        threading.Thread(target=f, args=(configuration, readings)).start()
