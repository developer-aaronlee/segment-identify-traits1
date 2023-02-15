import csv
import json
import requests

url = 'https://api.segment.io/v1/identify'
API_KEY = 'Basic akplVGEyU0FUb1V6c0NFYVNXQ01BREY2TTB0M2drcmU6'
headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

with open('pvolve_server_7.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in spamreader:
        if len(row)==0:
            continue
        temp = row[0].split(",")

        dic = {}

        if temp[0] == "userId":
            continue
        if temp[1] != "":
            dic["email"] = temp[1]
        if temp[2] != "":
            dic["app_subscription_status"] = temp[2]


        # obj = {}
        #
        # if temp[5] != "":
        #     obj["country"] = temp[5]
        # if temp[6] != "":
        #     obj["state"] = temp[6]
        # if temp[7] != "":
        #     obj["city"] = temp[7]
        #
        # if len(obj) == 0:
        #     obj = ""
        # dic["default_address"] = obj

        new = {
               "userId": temp[0],
               "traits": dic
        }

        body = json.dumps(new)
        print(body)
        response = requests.post(url, data=body, headers=headers)
        print(response.json())

        # if temp[6] != "":
        #     new = {
        #         "userId": temp[0],
        #         "traits": dic,
        #         "timestamp": temp[6]
        #     }
        #
        #     body = json.dumps(new)
        #     # print(body)
        #     response = requests.post(url, data=body, headers=headers)
        #     print(response.json())
        #
        # else:
        #     new = {
        #         "userId": temp[0],
        #         "traits": dic,
        #     }
        #
        #     body = json.dumps(new)
        #     # print(body)
        #     response = requests.post(url, data=body, headers=headers)
        #     print(response.json())


        # if temp[2] != "":
        #     dic["app_subscription_platform"] = temp[2]
        # if temp[3] != "":
        #     dic["app_trial_platform"] = temp[3]
        # if temp[4] != "":
        #     dic["app_subscription_status"] = temp[4]
        # if temp[5] != "":
        #     dic["app_subscription_partner_code"] = temp[5]
        # if temp[6] != "":
        #     dic["app_trial_term"] = temp[6]
        # if temp[7] != "":
        #     dic["app_trial_start_date"] = temp[7]
        # if temp[8] != "":
        #     dic["app_trial_end_date"] = temp[8]
        # if temp[9] != "":
        #     dic["app_trial_cancel_date"] = temp[9]
        # if temp[10] != "":
        #     dic["app_subscription_term"] = temp[10]
        # if temp[11] != "":
        #     dic["app_subscription_start_date"] = temp[11]
        # if temp[12] != "":
        #     dic["app_subscription_cancel_date"] = temp[12]
        # if temp[13] != "":
        #     dic["app_subscription_expire_date"] = temp[13]
        # if temp[14] != "":
        #     dic["app_current_series_name"] = temp[14]
        # if temp[15] != "":
        #     dic["app_workouts_completed_count"] = int(temp[15])

        # if temp[2] != "":
        #     dic["default_address.city"] = temp[2]
        # if temp[3] != "":
        #     dic["default_address.country"] = temp[3]
        # if temp[4] != "":
        #     dic["default_address.postalCode"] = temp[4]
        # if temp[5] != "":
        #     dic["default_address.state"] = temp[5]
        # if temp[6] != "":
        #     dic["default_address.street"] = temp[6]