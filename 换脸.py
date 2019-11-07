import json
import requests
import simplejson
import base64

image1 = r"C:/Users/Administrator/Desktop/1.jpg"
image2 = r"C:/Users/Administrator/Desktop/2.jpg"

#第一步 获取人脸关键点

def find_face(imgpath):

    print('finding')
    http_url = 'https://console.faceplusplus.com.cn/app/apikey/list'
    data = {"api_key":'NfHYj_YBScGz7fZyO_QgWHIQgZyNULQ9',
            "api_secret":'Q1BZoc1bSdBmr6JEvF5kGXYx0W3nN-in',
            "image_url":imgpath,"return_landmark":1
        }
    files = {"image_file":open(imgpath,'rb')}
    response = requests.post(http_url,data = data,files=files)
    req_con = response.content.decode('utf-8')
    print(type(req_con))

    this_json = simplejson.loads(req_con)
    print(this_json)
    faces = this_json['faces']
    list0 = faces[0]
    rectangle = list0['face_rectangle']
    print(rectangle)
    return rectangle
    #find_face(image1)
#第二步 换脸部分 图片大小不超过2M
def merge_face(image_url1,image_url2,image_url,number):#number决定换脸相似度
    ff1 = find_face(image_url1)
    ff2 = find_face(image_url2)
    rectangle1 = str(str(ff1['top']) + ',' + str(ff1['left']) + ',' + str(ff1['width']) + ','+str(ff1['height']))
    rectangle2= str(str(ff2['top']) + ',' + str(ff2['left']) + ',' + str(ff2['width']) + ',' + str(ff2['height']))
    f1 = open(image_url1,'rb')
    f1_64 = base64.b64encode(f1.read())#进行编码
    f1.close()
    f2 = open(image_url2, 'rb')
    f2_64 = base64.b64encode(f2.read())  # 进行编码
    f2.close()
    url_add = 'https://api-cn.faceplusplus.com/imagepp/v1/mergeface'
    data = {"api_key": 'NfHYj_YBScGz7fZyO_QgWHIQgZyNULQ9',
            "api_secret": 'Q1BZoc1bSdBmr6JEvF5kGXYx0W3nN-in',
            "template_base":f1_64,"template_rectangle":rectangle1,
            "merge_base": f2_64, "merge_rectangle": rectangle2,"merge_rate":number
            }

    response1 =requests.post(url_add,data=data)
    req_con1 = response1.content.decode('utf-8')
    print(req_con1)

    req_dict = json.JSONDecoder().decode(req_con1)
    result = req_dict['result']

    imgdata = base64.b64decode(result)

    file = open(image_url,'wb')
    file.write(imgdata)
    file.close()
image1 = r"C:/Users/Administrator/Desktop/1.jpg"
image2 = r"C:/Users/Administrator/Desktop/2.jpg"
image = r"C:/Users/Administrator/Desktop/face.jpg"

merge_face(image1 , image2 , image , 100)