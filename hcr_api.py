import time
import requests

##### Analyze an Image ####

subscription_key = "157501f71bff49adb2291c994041f5da"
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"

# image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Cursive_Writing_on_Notebook_paper.jpg/800px-Cursive_Writing_on_Notebook_paper.jpg"
image_url = "https://scontent.fbkk5-3.fna.fbcdn.net/v/t1.15752-9/31578001_1698928540198834_3785842912114245632_n.jpg?_nc_cat=0&oh=7ca98c81ec96a2978d7c224280c907e9&oe=5B5F2C7A"

text_recognition_url = vision_base_url + "recognizeText"
# print(text_recognition_url)

###### HTTP Request and Response
headers  = {'Ocp-Apim-Subscription-Key': subscription_key}
params   = {'handwriting' : True}
data     = {'url': image_url}
response = requests.post(text_recognition_url, headers=headers, params=params, json=data)
# print(response.raise_for_status())
# print(response.headers)

###### ตรวจสอบลิ้งที่เก็บข้อมูลการ Detect ทีแนบมากับ Header ไฟล์
operation_url = response.headers["Operation-Location"]
# print("Operation-Location >> " + operation_url)

###### extract ข้อมูลการประมวลผล การแปลตัวอักษรทั้งหมดจากลิ้ง Operation Lcation
analysis = {}
while not "recognitionResult" in analysis:
    response_final = requests.get(response.headers["Operation-Location"], headers=headers)
    analysis       = response_final.json()
    time.sleep(1)   
# print (analysis)

######  ทำการดึงข้อความที่ได้ออกมาในรูปแบบ tuple of list
polygons = [(line["text"]) for line in analysis["recognitionResult"]["lines"]]
print(polygons)
print(polygons[0])
print(polygons[1])
print(polygons[2])
print(polygons[3])
print(polygons[4])
