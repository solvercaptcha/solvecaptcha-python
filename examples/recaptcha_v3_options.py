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


config = {
            'server':           'solvecapcha.com',
    		'apiKey':            api_key,
    		# 'callback':         'https://your.site/result-receiver', # If set, the solver will return only the `captchaId` without polling the API for the answer.
    		'defaultTimeout':    120,
    		'recaptchaTimeout':  600,
    		'pollingInterval':   10,
	    }

solver = Solvecaptcha(**config)

try:
    result = solver.recaptcha(
        sitekey='6LfdxboZAAAAAMtnONIt4DJ8J1t4wMC-kVG02zIO',
        url='https://mysite.com/page/with//recaptcha-v3',
        version='v3',
        action='verify',
        # proxy={
        #        'type': 'HTTPS',
        #        'uri': 'login:password@IP_address:PORT'
        # }
        )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
