import json
import datetime
import logging
import threading
from .forwarders import twitter, safecast, plotlyf, radmon, gammaapi, zapier


def run_forwarder(forwader, configuration, readings):
    threading.Thread(target=forwader, args=(configuration, readings)).start()


class Forwarder(object):
    """Forward the Geiger Counter readings to miscellaneous external services.
    In a better world, this should be an independant application
    (like an Erlang one) that receives the readings through a broker
    (like ZeroMQ) and then dispatch them to the several ends.
    Here we may have threading issues, and it may not be totally
    reliable."""

    def __init__(self, configuration_file_path):
        self.configuration_file_path = configuration_file_path
        self.configuration = None
        self.next_publication_at = datetime.datetime.now()
        self.reload_configuration()

    def reload_configuration(self):
        try:
            with open(self.configuration_file_path, "rb") as file:
                self.configuration = json.load(file)
        except Exception as exc:  # pylint: disable=broad-except
            logging.warning(
                "Failed to load configuration file %s. Cause: %s",
                self.configuration_file_path,
                exc,
            )
            self.configuration = None
        self.next_publication_at = datetime.datetime.now()

    def dispatch(self, readings):
        # Prevent to publish zeros and not stabilized data.
        if readings["uSvh"] <= 0 or readings["duration"] < 120:
            return
        # No forwarding if configuration has not been initialized.
        if not self.configuration:
            return
        # Do the time have elapsed since last publication?
        if datetime.datetime.now() > self.next_publication_at:
            self.do_dispatch(readings, True)
            self.next_publication_at = datetime.datetime.now(
            ) + datetime.timedelta(
                minutes=int(self.configuration["publication"]["period"]))
        else:
            self.do_dispatch(readings, False)

    def do_dispatch(self, readings, period_elapsed):
        # Naive dispatching.
        if period_elapsed:
            if self.configuration["twitter"]["enabled"]:
                run_forwarder(twitter.forward, self.configuration, readings)
            if self.configuration["safecast"]["enabled"]:
                run_forwarder(safecast.forward, self.configuration, readings)
            if self.configuration["radmon"]["enabled"]:
                run_forwarder(radmon.forward, self.configuration, readings)
        if self.configuration["plotly"]["enabled"]:
            run_forwarder(plotlyf.forward, self.configuration, readings)
        if self.configuration["gammaapi"]["enabled"]:
            run_forwarder(gammaapi.forward, self.configuration, readings)
        if self.configuration["zapier"]["enabled"]:
            run_forwarder(zapier.forward, self.configuration, readings)
