# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for hooks."""

from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_online_store"
app_title = "ERPNext Online Store"
app_publisher = "Monogramm"
app_description = "TODO_APP_DESCRIPTION"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "opensource@monogramm.io"
app_license = "AGPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_online_store/css/erpnext_online_store.css"
# app_include_js = "/assets/erpnext_online_store/js/erpnext_online_store.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_online_store/css/erpnext_online_store.css"
# web_include_js = "/assets/erpnext_online_store/js/erpnext_online_store.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_online_store.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_online_store.install.before_install"
# after_install = "erpnext_online_store.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_online_store.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    "daily": [
        "erpnext_online_store.tasks.update_items_info"
    ],
    "cron": {
        '* * * * *': [
            "erpnext_online_store.tasks.update_items_info"
        ]
    }
}

# Testing
# -------

# before_tests = "erpnext_online_store.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_online_store.event.get_events"
# }
