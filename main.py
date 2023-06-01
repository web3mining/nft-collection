import traceback
import time
import requests
import json


workers_link='https://api.emcd.io/v1/btc/workers/c9390e75-1845-4066-a510-47785af028c6'
date_link='https://api.emcd.io/v1/btc/income/c9390e75-1845-4066-a510-47785af028c6'


def getInfo():

    def createRequest(type:str):
        try:
            answer=requests.get(workers_link if type.lower()=='workers' else date_link)

            if str(answer.status_code).startswith('2'):
                return answer.json()
            else:
                return None
        except Exception as ex:
            print(traceback.format_exc())
            return None

    workers_data=createRequest('workers')
    date_data=createRequest('date')

    return (workers_data,date_data)



def formJson(worker_data,date_data):

    def convertHashrate(hashrate):
        try:
            hashrate=list(str(worker_data['hashrate']))
            hashrate.insert(2,'.')
            hashrate=round(float(''.join(hashrate)),2)
            return hashrate
        except Exception as ex:
            print(traceback.format_exc())
            return None


    json_pattern={"name": f"Worker {worker_data['worker']}",
                  "description": "Произвольный текст",
                  "attributes": [
                      {
                          "trait_type": "Hashrate",
                          "value": f"{convertHashrate(worker_data['hashrate'])} TH/s",
                      },
                      {
                          "trait_type": "24h",
                          "value": f"{convertHashrate(worker_data['hashrate24h'])} TH/s"
                      },
                      {
                          "trait_type": "Status",
                          "value": "Active" if worker_data['active']==1 else 'Inactive'
                      },
                      {
                          "trait_type": "Income",
                          "value": "{:.9f}".format(round(date_data['income'][0]['income']/90,9))
                      },
                      {
                          "trait_type": "Date",
                          "value": date_data['income'][0]['gmt_time']
                      },
                      {
                          "trait_type": "Rewards type",
                          "value": 'fpps'
                      }
    ]
    }

    return json_pattern


def writeJson(data,number):
    with open(f'{number}.json','w',encoding='utf8') as f:
        json.dump(data,f,indent=4,ensure_ascii=False)



def main():
    while True:
        try:
            info=getInfo()
            if info and len(info)==2:
                workers_data = info[0]
                date_data=info[1]
                for worker in workers_data['details']:

                    formated_json=formJson(worker,date_data)
                    writeJson(formated_json,int(worker['worker']))
        except:
            print(traceback.format_exc())
        time.sleep(3600)

if __name__=='__main__':
    main()