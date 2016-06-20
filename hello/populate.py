import requests

def populate():
    headers = {'x-api-key': 'c2ee00db1a75428981d49a5c74d24015'}
    r = requests.get('https://fulfil_demo.fulfil.io/api/v1/model/sale.sale?field=reference&field=shipment_address.subdivision.code&field=shipment_address.country.code&filter=[["state","=","processing"]]', headers=headers)
    data = r.json()
    temp_list = []
    # print data

    for x in data:
        state = x['shipment_address.subdivision.code']
        temp_list.append(state)

    print temp_list
    state_and_count = [[x ,temp_list.count(x)] for x in temp_list]
    print state_and_count
    formatted_array = [['Province', 'Total # of Orders']] + state_and_count
    return formatted_array
