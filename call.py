from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players

print()
print()
print()

x = players.find_players_by_full_name('Lebron James')
player_id = x[0]['id']

player_info = commonplayerinfo.CommonPlayerInfo(player_id= player_id)

player_dict = player_info.player_headline_stats.get_dict()

zip_object = zip(player_dict['headers'],player_dict['data'][0])

counter = 0
for header, stat in zip_object:
    if counter == 0:
        counter += 1
        pass
    else:
        print(f'{header}' + ": " + f'{stat}')

print()
print()
print()