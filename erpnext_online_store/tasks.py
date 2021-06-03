import json
import requests
import frappe


def update_items_info():
    data_dict = json.loads(requests.get('http://pixels.er16.ru/loads.json').text)
    for good in data_dict['good']:
        item = frappe.new_doc('Item')
        # item.stock_uom = 'Nos'
        item.item_group = 'Consumable'
        for field in good['field']:
            if field['@name'] == 'Название':
                item.item_name = field['#text']
            if field['@name'] == 'Цена':
                item.valuation_rate = field['#text']
            if field['@name'] == 'Артикул':
                item.item_code = field['#text']
        print(item.__dict__)
        item.insert(ignore_if_duplicate=True)
