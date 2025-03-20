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

solver = Solvecaptcha(api_key)

try:
    result = solver.turnstile(
        sitekey='0x4AAAAAAAFhFmVSpJiMM20Z',
        url='https://tvboom.net/packages/view/id/1/packages/view/id/1/',
        useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    )

# {"sitekey":"0x4AAAAAAAFhFmVSpJiMM20Z","pageurl":"https:\/\/tvboom.net\/packages\/view\/id\/1\/packages\/view\/id\/1\/","pagedata":"","captchatype":"turnstile","data":"","action":"",","proxy":"","proxytype":"HTTP"}

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
