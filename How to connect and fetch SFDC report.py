import pandas as pd
import numpy as np
from pandas import DataFrame, Series 
from simple_salesforce import Salesforce #imported salesforce
sf = Salesforce(username='youremail@domain.com', password='enter_password', security_token = 'Salesforce_token') #loggedin,
#salesforce token is received in email everytime you change your password.
import requests #imported requests
session = requests.Session() #starting sessions
from io import StringIO #to read web data

error_report_defined = session.get("https://na4.salesforce.com/xxxxxxxxxxxx?export=1&enc=UTF-8&xf=csv".format('xxxxxxxxxxxx'), headers=sf.headers, cookies={'sid': sf.session_id})
df_sfdc_error_report_defined = pd.DataFrame.from_csv(StringIO(error_report_defined.text))
df_sfdc_error_report_defined = df_sfdc_error_report_defined.to_csv('defined.csv', encoding = 'utf-8')
error_report = pd.read_csv('defined.csv') #your report is saved in csv format 
print (error_report)
