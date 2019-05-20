from instagram_private_api import Client, ClientCompatPatch
import json
import os
from appender import appendUserFeed
from reformat import reformatUserFeed, reformatCommentList


user_name = 'devarshi.raval'
password = 'tvtokyo7'

api = Client(user_name, password)

#Extracting UserId from username
username = "amitabhbachchan"
command = "mkdir " + username
if not os.path.exists(username):
    os.system(command)

name = api.username_info(username)
userid = name['user']['pk']

#**********************************************************************
#Extracting user posts of "username"
#**********************************************************************
print("Fetching posts of user: ", username)
final = []
i=1
userFeed = api.username_feed(username)
maxId = userFeed['next_max_id']
minTime = userFeed['items'][userFeed['num_results']-1 ]['device_timestamp']
final = appendUserFeed(final, userFeed)
kwargs = {"max_id": maxId}
while 1:
    #try:
    userFeed = api.username_feed(username, **kwargs)
    #except:
    #    pass
    final = appendUserFeed(final, userFeed)
    #with open("data.json", "a") as outfile:
    #    json.dump(userFeed, outfile, indent=4)
    if userFeed['more_available']:
        #print(i, userFeed['more_available'], maxId, minTime)
        i = i + 1
    else:
        print("All posts fetched. Total: ", len(final))
        break
    maxId = userFeed['next_max_id']
    minTime = userFeed['items'][userFeed['num_results']-1]['device_timestamp']
    kwargs = {"max_id": maxId}

final = reformatUserFeed(final)
with open("./{}/posts.json".format(username), "w") as outfile:
    json.dump(final, outfile,indent=4)
print("Data written in 'posts.json'")
#********************************END***************************



#**************************************************************
#Extracting comments from posts
#**************************************************************
# print("Starting comments fetching.................")
# i=0
# error = 0
# commentList = []
# temp = {}
# while 1:
#     if i == len(final)-1:
#         print("All comments fetched")
#         break
#     #media_id = final[i]['id']
#     #com = api.media_n_comments(final[i]['id'], final[i]['comment_count'])
#     try:
#         com = api.media_n_comments(final[i]['id'], final[i]['comment_count'])
#     except:
#         i=i+1
#         print("Error Occured")
#         error = error+1
#         continue
#     #com2 = {"user_id" : com['user_id'], "text" : com['text']}
#     com = reformatCommentList(com)
#     #temp['media_id'] = final[i]['id']
#     #temp['comments'] = com
#     commentList.append({"media_id": final[i]['id'], "index_in_List": i, "comment_count": len(com), "comments": com})
#     i=i+1
#     print(i, final[i]['id'])
#
# with open("./{}/comments.json".format(username), "w") as outfile:
#     json.dump(commentList, outfile, indent=4, ensure_ascii=False)
# print("Comments written to 'comments.json'")
# print("Total errors: ", error)


#*************************END**********************************
