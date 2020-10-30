import os
from urllib.parse import urlparse

from functions import download_file

a = ['https://vnusoftware.com/iclaimmax/assets/upload/claim/8_VNUPEHPG.869375402960_duly_signed_doc_1603511124.pdf',
     'https://vnusoftware.com/iclaimmax/assets/upload/claim/1603516999_101676374_3943.pdf']

files, mss_no = [], 'MSS-1001210'
for i, j in enumerate(a):
    file_name = os.path.basename(urlparse(j).path)
    download_file(j, f'attach/{mss_no}/{file_name}')
    files.append(os.path.abspath(f'attach/{mss_no}/{file_name}'))
pass