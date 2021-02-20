from youtube_statistics import YTstats


API_KEY = 'AIzaSyDz8GYHVFFQ5G1n4nL1ss9F-JyW2y0f--4'
channel_id = 'UCGXsku75ELWndSG7kEihspg'

yt = YTstats(API_KEY, channel_id)
yt.extract_all()
yt.dump()