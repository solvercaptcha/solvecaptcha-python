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

solver = Solvecaptcha(api_key, defaultTimeout=100, pollingInterval=10)

try:
    result = solver.rotate(
        './images/rotate.jpg',
        angle=40,
        lang='en',
        # hintImg  = 'images/rotate_hint.jpg'
        hintText='Put the images in the correct way up')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
