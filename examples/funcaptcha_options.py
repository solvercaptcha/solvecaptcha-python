import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from solvecaptcha import Solvecaptcha

# In this example, we store the API key in environment variables, which can be set as follows:
# On Linux or macOS:
# export APIKEY_SOLVECAPTCHA=1abc234de56fab7c89012d34e56fa7b8
# On Windows:
# set APIKEY_SOLVECAPTCHA=1abc234de56fab7c89012d34e56fa7b8
# Alternatively, you can directly assign the API key to a variable:
# api_key = "1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_SOLVECAPTCHA', 'YOUR_API_KEY')

solver = Solvecaptcha(api_key, defaultTimeout=180, pollingInterval=15)

try:
    result = solver.funcaptcha(
        sitekey='1C2BB537-D5F7-4A66-BC74-25881B58F1D6',
        url='https://agoda-api.arkoselabs.com/v2/1C2BB537-D5F7-4A66-BC74-25881B58F1D6/api.js',
        surl='https://client-api.arkoselabs.com',
        userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        # **{'data[key]': 'value'},  #optional data param used by some websites
        # proxy={
        #     'type': 'HTTP',
        #     'uri': 'login:password@123.123.123.123:8080'
        # }
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
