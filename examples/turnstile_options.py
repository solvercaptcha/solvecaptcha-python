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
            'server':           'solvecaptcha.com',
    		'apiKey':            api_key,
    		# 'callback':         'https://your.site/result-receiver', # If set, the solver will return only the `captchaId` without polling the API for the answer.
    		'defaultTimeout':    120,
    		'recaptchaTimeout':  600,
    		'pollingInterval':   10,
	    }

solver = Solvecaptcha(**config)

try:
    result = solver.turnstile(sitekey='0x4AAAAAAADnPIDROrmt1LDg',
                              url='https://dexscreener.com/',
                              data="8ffc47422ae4e297",
                              pagedata="JD.BAzfWHWAX2ZIXTgOkwU7SIJIXB3TYI6x0fplCxPo-1736508032-1.3.1.1-2Qy7twd2XO5laG9G6QrjYSQ.g3LszfU1A1osszzbbz.EHIJLRM4lHyZMnyTex7nIl7U8xVZrb99.lVWJ6RSSWG.0x_95kiDv.kqnQACTDl072eVFdyd1IRA.3SJsKl0ptevnsQx6pShakPgm2HWX65d5Jv.CDvbLLPSDz1SJk35ULnsY0fC9B_7NfgjEai5D2sYdYx5XxIIOOrQLkOHD963SqC6DQu9VXq09o8qlWsjHEORy_4VOsxf.7hjBw9y3Auziyh7ISo2mgAEHqCnYMjJtyLDqc4CGSnmYBRvSGMj96KvTLfSx2PCNxwWpUiEHb1WcM9Y1zjyz6.JVos.mjx5MDQ3UADASMJbtdWHMpH0yDfiDgtWNpxW1F.chfJ.q5MhSip4lLAXMVYLMDi.10C0pjIhwOHM0tuFhbyjAoq7MOfvL9t0sNQLKlrk1RUayK6alVy2Y0Zf1BH4p7lOSPQ",
                              action="managed",
                              useragent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                              # proxy={
                              #        'type': 'HTTPS',
                              #        'uri': 'login:password@IP_address:PORT'
                              # }
                            )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
