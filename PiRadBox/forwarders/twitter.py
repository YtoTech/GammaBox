from twython import Twython

def forward(configuration, readings):
    print("Twitting... {0}.".format(readings))
    twitter = Twython(configuration['appKey'], configuration['appSecret'],
    	configuration['oauthToken'], configuration['oauthTokenSecret'])
    twitter.update_status(
        status='My #RadBox now reads: '
        '{0} uSv/h +/- {1} -- {2} CPM'.format(
            readings['uSvh'], readings['uSvhError'], readings['cpm']))
    print('Twitter Ok.')
