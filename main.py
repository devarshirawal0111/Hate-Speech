from flask import Flask, render_template
import json


app = Flask(__name__)

username = "malaikaaroraofficial"
path = "Data/" + username + "/posts.json"
path2 = "Data/" + username + "/comments.json"

with open(path) as fileptr:
    data = json.loads(fileptr.read())
with open(path2) as fileptr:
    comments = json.loads(fileptr.read())
all_data=[]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/twitter')
def twitter():
    return render_template('twitter.html')

@app.route('/instagram')
def instagram():
    # all_data = []
    # # temp=[]
    # count = 0
    # # print(len(data))
    # for i in data:
    #     print(len(i),i)
    #     if count % 3 == 0:
    #         if count > 0:
    #             all_data.append(temp)
    #         temp = []
    #     if 'image_versions2' in i.keys():
    #         i['img_src']=i['image_versions2']
    #         del i['image_versions2']
    #         temp.append(i)
    #     print(temp)
    #     count += 1
    #     if count == len(data):
    #         all_data.append(temp)
    print((all_data))
    global comments
    return render_template("instagram.html", data=all_data, length=range(len(all_data)))

@app.route('/instagram/comments/<index>')
def instaComments(index):
    global comments
    index = int(index)
    return render_template('instaComments.html', comments=comments[index])

def data_format():
    global all_data
    # temp=[]
    count = 0
    # print(len(data))
    for i in data:
        # print(len(i), i)
        if count % 5 == 0:
            if count > 0:
                all_data.append(temp)
            temp = []

        if 'error' in i.keys():
            if i['error'] is False:
                if 'carousel_media' in i.keys():
                    if 'video_versions' in i['carousel_media'][0]:
                        i['type'] = "carousel_video"
                    else:
                        i['type'] = "carousel_image"
                    amt = 0
                    for j in i['carousel_media']:
                        if amt:
                            j['skip']=True
                        else:
                            j['skip']=False
                        j['media_count'] = str(amt)
                        amt+=1


                else:
                    if 'video_versions' in i.keys():
                        i['type'] = 'video'
                    else:
                        i['type'] = 'image'
                i['href'] = "#"+i['id']

                temp.append(i)
                print(temp)
                count += 1
        print(count)
        if count == len(data):
                    all_data.append(temp)
    all_data.append(temp)


if __name__=='__main__':
    data_format()
    app.run(debug=True)