import requests

def  lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify",headers = headers, params = payload)
    return r.status_code


message = 'Notify from Line, HELLO WORLD'
token = 'fNWDAvowvgemplzQobwVde4qJTNOouW8VC95eJ19fIR'

lineNotifyMessage(token, message)