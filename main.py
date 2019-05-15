from flask import Flask, render_template
import json

app = Flask(__name__)

with open('posts.json') as fileptr:
    data = json.loads(fileptr.read())
all_data=[]
@app.route('/')
def index():
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
    # print(len(all_data))
    return render_template("index.html",data=all_data,length=range(len(data)))

def data_format():
    global all_data
    # temp=[]
    count = 0
    # print(len(data))
    for i in data:
        # print(len(i), i)
        if count % 3 == 0:
            if count > 0:
                all_data.append(temp)
            temp = []
        if 'image_versions2' in i.keys():
            i['img_src'] = i['image_versions2']
            del i['image_versions2']
            temp.append(i)
        # print(temp)
        count += 1
        if count == len(data):
            all_data.append(temp)


if __name__=='__main__':
    data_format()
    app.run(debug=True)