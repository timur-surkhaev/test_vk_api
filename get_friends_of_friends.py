# exec(open('test_vk_api.py').read())

# Gets friends of friends of some user and saves them to json.
# Additionally calculates the ratio of friends number of current user
# to average friends number of his friends. See "Friendship Paradox". 

import vk_api
import time


USER_ID = <id_to_investigate>
COUNT = 10000

FILE_TAIL = '_friends_of_friends.json'

# unsafe
vk_session = vk_api.VkApi(<login>,
                          <password>)
vk_session.auth()

vk = vk_session.get_api()

friends = vk.friends.get(user_id=USER_ID, count=COUNT)

friends_of_friends = {}
for friend in friends['items']:
    try:
        frnds = vk.friends.get(user_id=friend, count=COUNT)['items']
    except:
        frnds = 'Something wrong'
    print('id' + str(friend) + ' ' + str(len(frnds)))   
    
    friends_of_friends[friend] = frnds    
    time.sleep(0.1)  


lengths = []  
for friend in friends_of_friends.values():
    if(friend != 'Something wrong'):
        print(friend)
        lengths.append(len(friend))

ratio = round((sum(lengths)/len(lengths))/friends['count'],2)
print(ratio)    
    
filename = str(USER_ID) + FILE_TAIL   
with open(filename, 'w') as f:
    f.write(json.dumps(friends_of_friends))    
    