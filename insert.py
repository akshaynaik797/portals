import sqlite3

insurer, process = 'mediassist', 'discharge'
with sqlite3.connect('database1.db') as con:
    cur = con.cursor()
    with open('temp.csv') as fp:
        for i in fp:
            i = i.replace('\n', '')
            i = i.split(',')
            cur.execute(f"insert into paths values ('{insurer}', '{process}', '{i[0]}', '{i[1]}', '{i[2]}', '', '0')")
            pass