import requests
import threading
import concurrent.futures
from colorama import Fore, init
init(convert=True)

#banner
intro = f"""{Fore.RED}
 ▄▄▄▄    ██▓     ██▓▒███████▒▒███████▒ ▄▄▄       ██▀███  ▓█████▄ 
▓█████▄ ▓██▒    ▓██▒▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░▒████▄    ▓██ ▒ ██▒▒██▀ ██▌
▒██▒ ▄██▒██░    ▒██▒░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌
▒██░█▀  ▒██░    ░██░  ▄▀▒   ░  ▄▀▒   ░░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌
░▓█  ▀█▓░██████▒░██░▒███████▒▒███████▒ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ 
░▒▓███▀▒░ ▒░▓  ░░▓  ░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
▒░▒   ░ ░ ░ ▒  ░ ▒ ░░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ 
 ░    ░   ░ ░    ▒ ░░ ░ ░ ░ ░░ ░ ░ ░ ░  ░   ▒     ░░   ░  ░ ░  ░ 
 ░          ░  ░ ░    ░ ░      ░ ░          ░  ░   ░        ░    
      ░             ░        ░                            ░      
{Fore.YELLOW}Doxxing tool made by Sky Files{Fore.RESET}
"""
print(intro)
print_lock = threading.Lock()

target = str(input("Ingresa un nombre: "))
 
#Instagram
instagram = f"https://www.instagram.com/{target}/"
#Facebook
facebook = f"https://www.facebook.com/{target}/"
#Twitter
twitter = f"https://twitter.com/{target}"
#Youtube
youtube = f"https://www.youtube.com/user/{target}"
#Blogger
blogger = f"https://{target}.blogspot.com"
#Google+
google_plus = f"https://plus.google.com/s/{target}/top"
#Reddit
reddit = f"https://www.reddit.com/user/{target}"
#Wordpress
wordpress = f"https://{target}.wordpress.com"
# PINTEREST
pinterest = f'https://www.pinterest.com/{target}'
# GITHUB
github = f'https://www.github.com/{target}'
# TUMBLR
tumblr = f'https://{target}.tumblr.com'
# FLICKR
flickr = f'https://www.flickr.com/people/{target}'
# STEAM
steam = f'https://steamcommunity.com/id/{target}'
# VIMEO
vimeo = f'https://vimeo.com/{target}'
# SOUNDCLOUD
soundcloud = f'https://soundcloud.com/{target}'
# DISQUS
disqus = f'https://disqus.com/by/{target}'
# MEDIUM
medium = f'https://medium.com/@{target}'
# DEVIANTART
deviantart = f'https://{target}.deviantart.com'
# VK
vk = f'https://vk.com/{target}'
# ABOUT.ME
aboutme = f'https://about.me/{target}'
# IMGUR
imgur = f'https://imgur.com/user/{target}'
# FLIPBOARD
flipboard = f'https://flipboard.com/@{target}'
# SLIDESHARE
slideshare = f'https://slideshare.net/{target}'
# FOTOLOG
fotolog = f'https://fotolog.com/{target}'
# SPOTIFY
spotify = f'https://open.spotify.com/user/{target}'
# MIXCLOUD
mixcloud = f'https://www.mixcloud.com/{target}'
# SCRIBD
scribd = f'https://www.scribd.com/{target}'
# BADOO
badoo = f'https://www.badoo.com/en/{target}'
# PATREON
patreon = f'https://www.patreon.com/{target}'
# BITBUCKET
bitbucket = f'https://bitbucket.org/{target}'
# DAILYMOTION
dailymotion = f'https://www.dailymotion.com/{target}'
# ETSY
etsy = f'https://www.etsy.com/shop/{target}'
# CASHME
cashme = f'https://cash.me/{target}'
# BEHANCE
behance = f'https://www.behance.net/{target}'
# GOODREADS
goodreads = f'https://www.goodreads.com/{target}'
# INSTRUCTABLES
instructables = f'https://www.instructables.com/member/{target}'
# KEYBASE
keybase = f'https://keybase.io/{target}'
# KONGREGATE
kongregate = f'https://kongregate.com/accounts/{target}'
# LIVEJOURNAL
livejournal = f'https://{target}.livejournal.com'
# ANGELLIST
angellist = f'https://angel.co/{target}'
# LAST.FM
last_fm = f'https://last.fm/user/{target}'
# DRIBBBLE
dribbble = f'https://dribbble.com/{target}'
# CODECADEMY
codecademy = f'https://www.codecademy.com/{target}'
# GRAVATAR
gravatar = f'https://en.gravatar.com/{target}'
# PASTEBIN
pastebin = f'https://pastebin.com/u/{target}'
# FOURSQUARE
foursquare = f'https://foursquare.com/{target}'
# ROBLOX
roblox = f'https://www.roblox.com/user.aspx?username={target}'
# GUMROAD
gumroad = f'https://www.gumroad.com/{target}'
# NEWSGROUND
newsground = f'https://{target}.newgrounds.com'
# WATTPAD
wattpad = f'https://www.wattpad.com/user/{target}'
# CANVA
canva = f'https://www.canva.com/{target}'
# CREATIVEMARKET
creative_market = f'https://creativemarket.com/{target}'
# TRAKT
trakt = f'https://www.trakt.tv/users/{target}'
# 500PX
five_hundred_px = f'https://500px.com/{target}'
# BUZZFEED
buzzfeed = f'https://buzzfeed.com/{target}'
# TRIPADVISOR
tripadvisor = f'https://tripadvisor.com/members/{target}'
# HUBPAGES
hubpages = f'https://{target}.hubpages.com'
# CONTENTLY
contently = f'https://{target}.contently.com'
# HOUZZ
houzz = f'https://houzz.com/user/{target}'
#BLIP.FM
blipfm = f'https://blip.fm/{target}'
# WIKIPEDIA
wikipedia = f'https://www.wikipedia.org/wiki/User:{target}'
# HACKERNEWS
hackernews = f'https://news.ycombinator.com/user?id={target}'
# CODEMENTOR
codementor = f'https://www.codementor.io/{target}'
# REVERBNATION
reverb_nation = f'https://www.reverbnation.com/{target}'
# DESIGNSPIRATION
designspiration = f'https://www.designspiration.net/{target}'
# BANDCAMP
bandcamp = f'https://www.bandcamp.com/{target}'
# COLOURLOVERS
colourlovers = f'https://www.colourlovers.com/love/{target}'
# IFTTT
ifttt = f'https://www.ifttt.com/p/{target}'
# EBAY
ebay = f'https://www.ebay.com/usr/{target}'
# SLACK
slack = f'https://{target}.slack.com'
# OKCUPID
okcupid = f'https://www.okcupid.com/profile/{target}'
# TRIP
trip = f'https://www.trip.skyscanner.com/user/{target}'
# ELLO
ello = f'https://ello.co/{target}'
# TRACKY
tracky = f'https://tracky.com/user/~{target}'
# BASECAMP
basecamp = f'https://{target}.basecamphq.com/login'
 
WEBSITES = [
instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus,
medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
]
 
def dox(url):
    source = requests.get(url).text
    if target in source:
        with print_lock:
            print(f"{Fore.YELLOW}Found target in:{Fore.CYAN} {url}\n")
    else:
        pass
 
with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
    for url in WEBSITES:
        executor.submit(dox, url)