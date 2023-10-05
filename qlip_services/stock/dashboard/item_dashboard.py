from __future__ import unicode_literals

import frappe
from erpnext.stock.dashboard.item_dashboard import get_data

@frappe.whitelist()
def qlip_get_data(item_code=None, warehouse=None, item_group=None,
	start=0, sort_by='actual_qty', sort_order='desc'):

    return get_data(
        item_code=item_code,
        warehouse=warehouse,
        item_group=item_group,
        start=start,
        sort_by=sort_by,
        sort_order=sort_order)
