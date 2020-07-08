from hdfs.ext.kerberos import KerberosClient
import requests
import logging

logger = logging.basicConfig(level=logging.DEBUG)

session = requests.Session()
session.verify = False

client = KerberosClient(url='http://x.x.x.x:abcd', session=session,
mutual_auth='REQUIRED',principal='abcdef@LMNOPQ')

lists = client.list('/user/')

logger.debug(lists)