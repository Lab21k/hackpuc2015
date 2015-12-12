# coding: utf-8

def get_data():
    import requests
    import json
    import re
    import codecs
    import calendar
    import datetime
    print 'Starting getting crime data...'
    file = codecs.open('data_all.json', 'w', encoding='utf8')

    # (Year, Month)
    start = (2015, 12)
    stop = False

    txt_all = u'['

    while not stop:
        last_day = calendar.monthrange(start[0], start[1])[1]
        date_from = datetime.date(start[0], start[1], 1).strftime('%d/%m/%Y')
        date_to = datetime.date(start[0], start[1], last_day).strftime('%d/%m/%Y')
        print('Getting from {} to {}'.format(date_from, date_to))
        txt = requests.get('http://ondefuiroubado.com.br/rio-de-janeiro/RJ', params={'from': date_from, 'to': date_to}).text

        reg = r'OndeFuiRoubado\.Views\.CrimesIndexView\.initialize\(.*\}\]\)'
        res = re.findall(reg, txt)
        if len(res):
            res = res[0].replace('OndeFuiRoubado.Views.CrimesIndexView.initialize([', '')[0:-2]
            txt_all += unicode(res)
            txt_all += ','
        else:
            print('NAO TEM RESULTADO')

        if start[1] == 1:
            start = (start[0] - 1, 12)
        else:
            start = (start[0], start[1] - 1)

        if start[0] == 2010:
            stop = True

    txt_all = txt_all[0:-1] + u']'

    file.write(txt_all)
    file.close()
