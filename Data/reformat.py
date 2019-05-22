

def reformatUserFeed(results):
    keys = ['pk', 'device_timestamp', 'media_type',  'code', 'client_cache_key', 'filter_type' \
             , 'comment_likes_enabled', 'has_more_comments', 'max_num_visible_preview_comments', 'preview_comments'\
            , 'can_view_more_preview_comments', 'inline_composer_display_condition', 'inline_composer_imp_trigger_time'\
            , 'user', 'can_viewer_reshare', 'comment_threading_enabled'\
            , 'caption_is_edited', 'has_liked', 'top_likers', 'facepile_top_likers', 'direct_reply_to_author_enabled'\
            , 'can_viewer_save', 'organic_tracking_token']

    #print(results['items'][0]['taken_at'])


    i=0
    while 1:
        if (i == len(results) - 1):
            break
        try:
            for key in keys:
                #print(results['items'][i]['taken_at'])
                del results[i][key]
        except Exception as e:
           # print('Exception:', e)
            pass
        i=i+1


    return results


def reformatCommentList(com):
    i=0
    com2 = []
    while 1:
        if i==len(com)-1:
            break
        try:
            com3 = {"user_id": com[i]['user_id'], "username":com[i]['user']['username'], "comment_id": com[i]['pk'],"text": com[i]['text']}
            com2.append(com3)
        except:
            i=i+1
            continue

        i=i+1

    return com2