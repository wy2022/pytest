import requests

s = requests.Session()
r = s.get("https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1550126506&di=25948efd9c527b82eae14815fcb40b15&src=http://photo.16pic.com/00/11/25/16pic_1125468_b.jpg")

with open("H:/1.jpg","wb") as f:
    f.write(r.content)