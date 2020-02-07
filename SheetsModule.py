import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from gspread.exceptions import APIError

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    '../coppiettebot-861ce3e90b40.json', scope)
gc = gspread.authorize(credentials)


def getSheet():
    gc = gspread.authorize(credentials)
    return gc.open("Coppiometro").sheet1


def dateToday():
    return date.today().strftime("%d/%m/%Y")


def noCpp():
    sheet = getSheet()
    dates = sheet.col_values(1)
    if dates[-1] != dateToday():
        sheet.update_cell(len(dates)+1, 1, dateToday())
        sheet.update_cell(len(dates)+1, 2, 0)
        return 0
    return -1


def addCoppietta():
    sheet = getSheet()
    dates = sheet.col_values(1)
    if dates[-1] != dateToday():
        sheet.update_cell(len(dates)+1, 1, dateToday())
        sheet.update_cell(len(dates)+1, 2, 1)
        return 1
    else:
        currentCopNum = int(sheet.col_values(2)[-1])
        sheet.update_cell(len(dates), 2, currentCopNum+1)
        return currentCopNum + 1
