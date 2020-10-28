import sqlite3

from settings import dbname


def save_mss_no_data(mss_no, data):
    query = f"insert into mss_no_data values ('{mss_no}', '{data}')"
    with sqlite3.connect(dbname) as con:
        cur = con.cursor()
        cur.execute(query)
        return True


def get_field_list(insname, process):
    query = f"select field from paths where insurer='{insname}' and process='{process}' and is_input=1"
    with sqlite3.connect(dbname) as con:
        cur = con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        result = [i[0] for i in result]
        return result


def get_xpath_dict(insname, process):
    query = f"select field, path_type, path_value from paths where insurer='{insname}' and process='{process}'"
    with sqlite3.connect(dbname) as con:
        cur = con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        result = {i[0]: {"type": i[1], "value": i[2]} for i in result}
        return result


def get_portal_details_dict(insname, process):
    query = f"select username, password, website from portals where insurer='{insname}' and process='{process}'"
    with sqlite3.connect(dbname) as con:
        cur = con.cursor()
        cur.execute(query)
        result = cur.fetchone()
        result = {'username':result[0], 'password':result[1], 'website':result[2]}
        return result



if __name__ == "__main__":
    get_xpath_dict('mediassist', 'Claim')
    get_portal_details_dict('mediassist', 'Claim')

