import frappe
import datetime
import frappe
import requests

@frappe.whitelist(allow_guest=True)
def check_qty(**data):
    print(data)
    quantity = int(data['variants']['inventory_quantity'])
    if quantity >= 10:
        return {}
    title = data['title']
    items_values = frappe.get_all('Item', fields=['item_code', 'item_name', 'valuation_rate'])
    right_item = None
    for node in items_values:
        if title in node['item_name']:
            right_item = frappe.get_doc('Item', node['item_code'])
            break
    if not right_item:
        return {}
    for value_dict in items_values:
        if (
                title.lower() in value_dict['item_name'].lower() and right_item.valuation_rate > value_dict[
            'valuation_rate']):
            right_item = frappe.get_doc('Item', {'item_code': value_dict['item_code']})

    if not right_item:
        return {}

    invoice = frappe.get_doc(
        {'doctype': 'Purchase Invoice', 'supplier': frappe.get_all('Supplier')[0]['name'],
         'due_date': datetime.datetime.now(), 'amount': 100, 'base_rounded_total': 100,
         'credit_to': "Creditors - F",
         'base_total': 0.0})
    item_purchase_data = right_item.as_dict()
    item_purchase_data['qty'] = 10
    invoice.append('items', {
        'item_code': right_item.item_code,
        'qty': 10 - quantity,
        'rate': right_item.valuation_rate
    })
    invoice.insert(ignore_permissions=True)
    requests.get(f'https://sms.ru/sms/send?api_id=c34f67e7-bde5-3454-75ea-f2a1dccbdc64&to=79872748258&msg=Сформирован '
                 f'чек {invoice.name} &json=1')
    return invoice.as_dict()
