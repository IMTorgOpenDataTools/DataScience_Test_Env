#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

from pathlib import Path



def test_initialize():
    """Python initialization."""
    import sys
    print(f"The python version is: {sys.version}")
    assert len(sys.version) > 0
    print("test started succesffully")
    

def test_sqlitedb():
    """Create and connect to sqlitedb."""
    from pathlib import Path
    import sqlite3

    dbfile = Path('./tmp/test.db')
    conn = sqlite3.connect(dbfile)
    assert conn.cursor()
    print(sqlite3.version)
    print("sqlitedb successfully created")


def test_request_to_server():
    """Make request to public server."""
    import requests

    hdrs = {
        "User-Agent": "user",
        "From": "user@gmail.com",
        "Accept-Encoding": "gzip, deflate"
    }
    cik = "0000072971"
    acct = "FinancingReceivableAllowanceForCreditLosses"
    url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{acct}.json"

    edgar_resp = requests.get(url, headers=hdrs)
    assert edgar_resp.status_code == 200
    print("successful response returned from public server")


def test_file_copy():
    import shutil

    src = './new_file.csv'
    dst = './tmp/report.csv'

    with open(src, 'w') as f:
        f.write('This is a new report')
    shutil.copyfile(src, dst)
    assert Path(dst).is_file() == True
    print('copy file to shared drive was successful')