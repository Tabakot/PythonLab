import re

def check_date(date):
    print(f'{date} - Да, является' if re.match(r'(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[1-2])/((1[6-9]|[2-9]\d)\d\d)', date)
      else f'{date} - Нет, не является')

check_date("29/02/2000")
check_date("30/04/2003")
check_date("01/01/2003")
check_date("29/02/1599")
check_date("30-04-2003")
check_date("1/1/1899")