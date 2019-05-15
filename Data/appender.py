
def appendUserFeed(final, userFeed):
    if userFeed['num_results']==0:
        return final
    i=0
    while 1:
        if i==userFeed['num_results']-1:
            break

        final.append(userFeed['items'][i])
        i=i+1
    return final
