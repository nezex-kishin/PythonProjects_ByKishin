import calendar
a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')
with open('calendar.html', 'w') as g:
    print(a.formatyear(2024, width=4), file=g)