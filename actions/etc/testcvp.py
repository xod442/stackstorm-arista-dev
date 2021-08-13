#
from cvprac.cvp_client import CvpClient
import urllib3
# Disable Insecure request warning messages
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


cvp='10.132.0.6'
cvp_user = 'cvpadmin'
cvp_word = 'siesta3'


client = CvpClient()
# Connect to the CVP server
client.connect([cvp], cvp_user, cvp_word)

print(client)


response_data = client.api.get_cvp_info()
print("==================================================================")
print('getting version')
print(response_data)

response_data = client.api.get_inventory()
print("==================================================================")
print('getting inventory')
print(response_data[0]['ipAddress'])


