import traceback
import time
import requests
import json


workers_link = 'https://api.emcd.io/v1/btc/workers/c9390e75-1845-4066-a510-47785af028c6'
date_link = 'https://api.emcd.io/v1/btc/income/c9390e75-1845-4066-a510-47785af028c6'


def getInfo():

    def createRequest(type: str):
        try:
            answer = requests.get(
                workers_link if type.lower() == 'workers' else date_link)

            if str(answer.status_code).startswith('2'):
                return answer.json()
            else:
                return None
        except Exception as ex:
            print(traceback.format_exc())
            return None

    workers_data = createRequest('workers')

    sorted_details = sorted(workers_data['details'], key=lambda x: x['worker'])
    workers_data['details'] = sorted_details

    date_data = createRequest('date')

    return (workers_data, date_data)


def formJson(worker_data, date_data):

    def convertHashrate(hashrate):
        try:
            hashrate = list(str(worker_data['hashrate']))
            hashrate.insert(2, '.')
            hashrate = round(float(''.join(hashrate)), 2)
            return hashrate
        except Exception as ex:
            print(traceback.format_exc())
            return None

    json_pattern = {"image": "https://github.com/web3mining/nft-collection/blob/main/wm_m50_active_optim.gif",
                    "name": f"W3M Worker {worker_data['worker']}",
                    "description": "Web3Mining is a real BTC mining, where you choose the power and energy efficiency of the equipment. You don't have to worry about choosing a supplier, delivering and connecting equipment, its expensive maintenance and energy costs.",
                    "attributes": [
                        {
                            "trait_type": "Hashrate",
                            "value": f"{convertHashrate(worker_data['hashrate1h'])} TH/s",
                        },
                        {
                            "trait_type": "Hashrate 24h",
                            "value": f"{convertHashrate(worker_data['hashrate24h'])} TH/s"
                        },
                        {
                            "trait_type": "Status",
                            "value": "🟢 Active" if worker_data['active'] == 1 else '🔴 Inactive'
                        },
                        {
                            "trait_type": "Income",
                            "value": "{:.8f} BTC/24h".format(round(date_data['income'][0]['income']/100, 9))
                        },
                        {
                            "trait_type": "Date income",
                            "value": date_data['income'][0]['gmt_time']
                        },
                        {
                            "trait_type": "Rewards type",
                            "value": 'fpps'
                        },
                        {
                            "trait_type": "Consumption",
                            "value": '386W ±10%'
                        },
                        {
                            "trait_type": "Algorythm",
                            "value": 'SHA-256'
                        }
                    ],
                    "content_url": "https://github.com/web3mining/nft-collection/main/video_active.mp4",
                    "content_type": "video/mp4"
                    }

    return json_pattern


def writeJson(data, number):
    with open(f'{number}.json', 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():
    while True:
        try:
            info = getInfo()
            if info and len(info) == 2:
                workers_data = info[0]
                date_data = info[1]
                counter = 0
                for worker in workers_data['details']:

                    formated_json = formJson(worker, date_data)
                    for i in range(counter, counter+9):
                        writeJson(formated_json, i)
                        print(f'{i}.', worker['worker'])

                    counter += 9
        except:
            print(traceback.format_exc())
        time.sleep(3600)


if __name__ == '__main__':
    main()
