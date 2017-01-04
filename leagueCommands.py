import pprint
from riotwatcher import RiotWatcher
from botInfo import riot_api_key

session = RiotWatcher(riot_api_key)

# check if we have API calls remaining
print(session.can_make_request())

me = session.get_summoner(name='Dwonger')


# takes list of summoner ids as argument, supports up to 40 at a time
# (limit enforced on riot's side, no warning from code)
# returns a dictionary, mapping from summoner_id to mastery pages
# unfortunately, this dictionary can only have strings as keys,
# so must convert id from a long to a string
def mastery_pages():
    my_mastery_pages = session.get_mastery_pages([me['id'], ])[str(me['id'])]
    print(my_mastery_pages)
def server_status(server):
    server = session.get_server_status('na')
    pprint.pprint(server)
