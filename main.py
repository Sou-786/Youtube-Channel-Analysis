from youtube_statistics import YTstats


API_KEY = '##########################################'
channel_id = 'UCGXsku75ELWndSG7kEihspg'

yt = YTstats(API_KEY, channel_id)
yt.extract_all()
yt.dump()
