from datetime import datetime
a = '28/10/2020'
b = datetime.strptime(a,'%d/%m/%Y').strftime('%m/%d/%Y')
pass