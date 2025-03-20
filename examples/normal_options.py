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

solver = Solvecaptcha(api_key, defaultTimeout=30, pollingInterval=5)

try:
    result = solver.normal(
        './images/normal_2.jpg',
        numeric=4,
        minLen=4,
        maxLen=20,
        phrase=0,
        caseSensitive=0,
        calc=0,
        lang='en',
        # hintImg='./images/normal_hint.jpg',
        # hintText='Type red symbols only',
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
