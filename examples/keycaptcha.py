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
    result = solver.keycaptcha(
        s_s_c_user_id=184015,
        s_s_c_session_id='e34ddd2c72e67593ac0b4ca8e4f44725',
        s_s_c_web_server_sign='a5ebd41ae22348b2cdbdc211792e982d',
        s_s_c_web_server_sign2='29255689423dd92990f8d06de50560d0',
        url='https://mysite.com/page/with//keycaptcha')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
