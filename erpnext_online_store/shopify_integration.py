import frappe


@frappe.whitelist(allow_guest=True)
def trigger():
    doc = frappe.new_doc('Contact')
    doc.first_name = 'YRE YRE YRE'
    doc.insert()
    print(frappe.get_all('Contact'))
    return doc
