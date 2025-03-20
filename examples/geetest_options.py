import sys
import os
import requests
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

solver = Solvecaptcha(api_key,
                      defaultTimeout=300,
                      pollingInterval=10,
                      extendedResponse=True)

"""
**Important:** The value of the `challenge` parameter is dynamic. You must obtain a new value for each request to our API.
"""

resp = requests.get("https://mysite.com/api/v1/ captcha-demo/gee-test/init-params")
challenge = resp.json()['challenge']

try:
    result = solver.geetest(
        gt='81388ea1fc187e0c335c0a8907ff2625',
        apiServer='http://api.geetest.com',
        challenge=challenge,
        url='https://mysite.com/page/with//geetest',
        #  proxy={
        #      'type': 'HTTPS',
        #      'uri': 'login:password@IP_address:PORT'
        #  }
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))