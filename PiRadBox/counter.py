from PiPocketGeiger import RadiationWatch
from stream import onRadiation

radiationWatch = RadiationWatch(24, 23).setup()
radiationWatch.registerRadiationCallback(onRadiation)
# We need to close properly this resource at the appplication tear down.
