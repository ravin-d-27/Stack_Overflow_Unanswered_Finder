from django.shortcuts import render
import requests


def home(request):
    response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
    lst = []
    for data in response.json()['items']:
        if (data["answer_count"]==0):
            rec = []
            rec.append(data['title'])
            rec.append(data['link'])
            string = ""

            for i in data["tags"]:
                string+="#"+i+" "
            rec.append(string)

            usertype = data["owner"]["display_name"]
            profile = data["owner"]["profile_image"]

            rec.append(usertype)
            rec.append(profile)

            lst.append(rec)
        else:
            pass
    return render(request, "finder/home.html", {"resp":lst})
