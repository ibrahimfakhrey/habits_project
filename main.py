import requests
from datetime import datetime
USER_NAME="ibrahimf"
TOKEN="gdfgdfgsdfdgdgasder"
PIXLA_ENDINGPOINT="https://pixe.la/v1/users"
user_params={
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
graph_endingpoint=f"{PIXLA_ENDINGPOINT}/{USER_NAME}/graphs"
graph_config={
    "id":"graph1",
    "name":"programing time",
    "unit":"hours",
    "type":"int",
    "color":"momiji"
}
headers={
    "X-USER-TOKEN":TOKEN
}
today=datetime.now()
todays_formated=today.strftime("%Y%m%d")
adding_graph="https://pixe.la/v1/users/ibrahimf/graphs/graph1"
adding_config={
    "date":todays_formated,
    "quantity":"6"
}

updating=f"{PIXLA_ENDINGPOINT}/{USER_NAME}/graphs/graph1/20211215"
updatin_config={
    "quantity": "5"
}
response=requests.put(url=updating,json=updatin_config,headers=headers )
print(response.text)

