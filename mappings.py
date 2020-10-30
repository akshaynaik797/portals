import db_functions
from make_log import log_exceptions


def query_reply(data_dict, insname, process, mss_no, claim_no):
    try:
        if 'Query Replied' in data_dict:
            docs = []
            for i in data_dict['Query Replied']:
                for j in i['Doc']:
                    docs.append(j['Doc'])

            response = {
                'mss_no': mss_no,
                'claim_no': claim_no,
                'insname': insname,
                'process': process,
                'remark': 'Query reply',
                'docs': docs,
                'login_details': db_functions.get_portal_details_dict(insname, process)
            }
            return response
        else:
            return {}
    except:
        log_exceptions(insname=insname, process=process, mss_no=mss_no, claim_no=claim_no)
        return {}


def final_bills(data_dict, insname, process, mss_no, claim_no):
    try:
        if 'Claim' in data_dict:
            doa, dod = data_dict['Claim'][0]['Date_Of_Admission'], data_dict['Claim'][0]['Date_Of_Discharge']
            amount, remark = data_dict['Claim'][0]['Cliamed_Amount'], data_dict['Claim'][0][
                'Remark']
            docs = [i['Doc'] for i in data_dict['Claim'][0]['Doc']]
            response = {
                'mss_no': mss_no,
                'claim_no': claim_no,
                'insname': insname,
                'process': process,
                'doa': doa,
                'dod': dod,
                'amount': amount,
                'remark': 'final bill',
                'docs': docs,
                'login_details': db_functions.get_portal_details_dict(insname, process)
            }
            return response
        else:
            return {}
    except:
        log_exceptions(insname=insname, process=process, mss_no=mss_no, claim_no=claim_no)
        return {}
