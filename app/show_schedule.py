import requests
import json
import operator
def appendZero(str):
	if int(str) < 10:
		str = "0"+str
	return str
def episode_details(episode,show):
	r = requests.get(episode)
	ep = json.loads(r.text)
	season = appendZero(str(ep['season']))
	episode = appendZero(str(ep['number']))
	name = show+" S"+season+"E"+episode+" "+ep['name']
	href = "+".join(show.split(" "))+"+s"+season+"e"+episode
	details = [ep['airdate'],name,href]
	return details
def show_details(show):
	urlshow = "%20".join(show.split(" "))

	base = 'http://api.tvmaze.com/singlesearch/shows?q='
	r = requests.get(base+urlshow)
	details = json.loads(r.text)
	#print(details['name'])
	#print(details['status'])
	next = []
	if(details['status'] == 'Running'):
		#print(details['schedule']['days'])
		prev_ep = details['_links']['previousepisode']['href']
		prev_details = episode_details(prev_ep,details['name'])
		next.append(prev_details)	

		try:	
			next_ep = details['_links']['nextepisode']['href']
			next_details = episode_details(next_ep,details['name'])
			next.append(next_details)
			
		except:
			pass
		return next
def airing_shows():
	list = ["curb enthusiasm","modern family","nathan for you","south park","westworld", "another period","brooklyn nine nine","big bang theory"]
	episodes = []
	for item in list:
		details = show_details(item)
		episodes.extend(details)
	episodes.sort(key=operator.itemgetter(0))
	return episodes