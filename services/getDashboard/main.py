import requests
import json

def getDashboard(grafanaLoginURL, grafanaUserAcnt, grafanaUserPass):
    session          = requests.session()
    session.auth     = (grafanaUserAcnt, grafanaUserPass) 
    dashboardSession = session.get(f"{grafanaLoginURL}", verify=False)
    return dashboardSession