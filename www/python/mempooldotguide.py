from flask import Blueprint, render_template, redirect
from user_management import check_logged_in
from enable_disable_functions import *
from device_info import *
from application_info import *
from systemctl_info import *
import subprocess
import os


mynode_mempooldotguide = Blueprint('mynode_mempooldotguide',__name__)


### Page functions (have prefix /app/<app name/)
@mynode_mempooldotguide.route("/info")
def mempooldotguide_page():
    check_logged_in()

    app = get_application("mempooldotguide")
    app_status = get_application_status("mempooldotguide")
    app_status_color = get_application_status_color("mempooldotguide")

    # Load page
    templateData = {
        "title": "myNode - " + app["name"],
        "ui_settings": read_ui_settings(),
        "app_status": app_status,
        "app_status_color": app_status_color,
        "app": app
    }
    return render_template('/app/generic_app.html', **templateData)

