![solvecaptcha-python](https://github.com/user-attachments/assets/5270c365-83fd-4b37-9ff1-ff554e75442e)

<a href="https://github.com/solvercaptcha/solvecaptcha-python"><img src="https://github.com/user-attachments/assets/a737d428-5233-4605-9d09-211fa213d069" width="82" height="30"></a>
<a href="https://github.com/solvercaptcha/solvecaptcha-javascript"><img src="https://github.com/user-attachments/assets/4d3b4541-34b2-4ed2-a687-d694ce67e5a6" width="36" height="30"></a>
<a href="https://github.com/solvercaptcha/solvecaptcha-go"><img src="https://github.com/user-attachments/assets/ab22182e-6cb2-41fa-91f4-d5e89c6d7c6f" width="63" height="30"></a>
<a href="https://github.com/solvercaptcha/solvecaptcha-ruby"><img src="https://github.com/user-attachments/assets/0270d56f-79b0-4c95-9b09-4de89579914b" width="75" height="30"></a>
<a href="https://github.com/solvercaptcha/solvecaptcha-cpp"><img src="https://github.com/user-attachments/assets/36de8512-acfd-44fb-bb1f-b7c793a3f926" width="45" height="30"></a>
<a href="https://github.com/solvercaptcha/solvecaptcha-php"><img src="https://github.com/user-attachments/assets/e8797843-3f61-4fa9-a155-ab0b21fb3858" width="52" height="30"></a>
<a href="https://github.com/solvercaptcha/solvecaptcha-java"><img src="https://github.com/user-attachments/assets/a3d923f6-4fec-4c07-ac50-e20da6370911" width="50" height="30"></a>
<a href="https://github.com/solvercaptcha/solvecaptcha-csharp"><img src="https://github.com/user-attachments/assets/f4d449de-780b-49ed-bb0a-b70c82ec4b32" width="38" height="30"></a>

# Python library for interacting with the Solvecaptcha API (captcha-solving service)

A simple and efficient method to integrate the [Solvecaptcha] captcha-solving service into your code, enabling the automation of solving various types of captchas.
Examples of API requests for different captcha types can be found on the [Python captcha solver](https://solvecaptcha.com/captcha-solver/python-captcha-solver-bypass) page.

## ✅ Supported captcha solvers
To get started quickly, check out the [Captcha Solver API](https://solvecaptcha.com/captcha-solver-api) documentation.

### Helpful links:
- [reCAPTCHA v2 solver (Python + Selenium)](https://solvecaptcha.com/captcha-solver/recaptcha-v2-solver-bypass)
- [reCAPTCHA v3 solver](https://solvecaptcha.com/captcha-solver/recaptcha-v3-solver-bypass)
- [hCaptcha solver (Playwright-ready)](https://solvecaptcha.com/captcha-solver/hcaptcha-solver-bypass)
- [Text & Image captcha solver (Base64 / file input)]()
- [Cloudflare captcha / Turnstile solver](https://solvecaptcha.com/captcha-solver/cloudflare-captcha-solver-bypass)
- [Amazon captcha (WAF & login forms)](https://solvecaptcha.com/captcha-solver/amazon-captcha-solver-bypass)
- [GeeTest slider solver](https://solvecaptcha.com/captcha-solver/slider-captcha-solver-bypass)
- [FunCaptcha (Arkose Labs)](https://solvecaptcha.com/captcha-solver/funcaptcha-solver-bypass)
- [Other custom captcha types](https://solvecaptcha.com/)

## 🛠️ Features
- Fast and fully automated captcha bypass
- Works in **Python** environments
- Compatible with **Selenium**, **Playwright**, and other browser automation tools
- Lightweight SDK with modern **async/await** support
- Pay only for successful solves
- 99.9% uptime
- 24/7 support for developers and integration teams

## 📦 Use cases

- Web scraping behind reCAPTCHA or Cloudflare walls
- Automated form submission and login flows
- QA pipelines and headless browser testing
- Bypassing captchas in research or bot-detection evaluation
- Custom browser automations using Python

Need help integrating with your Python app or automation tools? [Open an issue](https://github.com/solvercaptcha/solvecaptcha-python/issues) or fork this repo to contribute.

- [Python Library for Interacting with the Solvecaptcha API](#python-library-for-interacting-with-the-solvecaptcha-api-captcha-solving-service)
  - [Installation](#installation)
  - [Configuration](#configuration)
    - [Solvecaptcha instance options](#solvecaptcha-instance-options)
  - [Solve captcha](#solve-captcha)
    - [Captcha options](#captcha-options)
    - [Normal Captcha](#normal-captcha)
    - [Text Captcha](#text-captcha)
    - [reCAPTCHA v2](#recaptcha-v2)
    - [reCAPTCHA v3](#recaptcha-v3)
    - [hCaptcha](#hcaptcha)
    - [FunCaptcha](#funcaptcha)
    - [GeeTest](#geetest)
    - [GeeTest v4](#geetest-v4)
    - [Cloudflare Turnstile](#cloudflare-turnstile)
    - [KeyCaptcha](#keycaptcha)
    - [Grid](#grid)
    - [ClickCaptcha](#clickcaptcha)
    - [Rotate](#rotate)
  - [Other methods](#other-methods)
    - [send / get_result](#send--get_result)
    - [balance](#balance)
    - [report](#report)
  - [Error handling](#error-handling)
  - [Proxies](#proxies)
  - [Async calls](#async-calls)
  - [Examples](#examples)
  - [Examples using Selenium](#examples-using-selenium)
  - [Useful articles](#useful-articles)
  - [Get in touch](#get-in-touch)
  - [License](#license)

## Installation

This package can be installed using Pip:

```bash
pip3 install solvecaptcha-python
```
or You can install this package directly from GitHub using `pip`:  

```sh
pip install git+https://github.com/solvercaptcha/solvecaptcha-python.git
```
## Configuration

An instance of `Solvecaptcha` can be created as follows:

```python
from solvecaptcha import Solvecaptcha

solver = Solvecaptcha('YOUR_API_KEY')
```

Additionally, there are several options available for configuration:

```python
config = {
            'server':           'solvecaptcha.com',
            'apiKey':           'YOUR_API_KEY',
            'callback':         'https://your.site/result-receiver',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
            'extendedResponse':  False
        }
solver = Solvecaptcha(**config)
```

### Solvecaptcha instance options

| Option           | Default value      | Description    |
| ---------------- | ------------------ | -------------- |
| server           | `solvecaptcha.com` | API server. You can configure it to `solvecaptcha.com` if your account is registered on this platform. |
| callback         | -                  | The URL of your web server that receives the captcha recognition result. This URL must first be registered in your account's [pingback settings]. |
| defaultTimeout   | 120                | Polling timeout in seconds for all captcha types except reCAPTCHA. Specifies the duration for which the module attempts to retrieve the response from the `res.php` API endpoint. |
| recaptchaTimeout | 600                | Polling timeout for reCAPTCHA in seconds. Specifies the duration for which the module attempts to retrieve the response from the `res.php` API endpoint. |
| pollingInterval  | 10                 | Interval in seconds between requests to the `res.php` API endpoint. It is not recommended to set a value lower than 5 seconds. |
| extendedResponse | None               | Set to `True` to receive the response with additional fields or in a more structured format (enables `JSON` response from the `res.php` API endpoint). Recommended for [ClickCaptcha](#clickcaptcha) and [Canvas](#canvas). |

> [!IMPORTANT]
> Once `callback` is defined for the `Solvecaptcha` instance, all methods return only the captcha ID and DO NOT poll the API to get the result. The result will be sent to the callback URL.

To get the answer manually, use the [get_result method](#send--get_result).

## Solve captcha

When submitting any image-based CAPTCHA, you can provide additional options to assist Solvecaptcha workers in solving it correctly.

### Captcha options

| Option        | Default Value | Description                                                                                   |
| ------------- | ------------- | --------------------------------------------------------------------------------------------- |
| numeric       | 0             | Specifies whether the captcha consists only of numbers or includes other symbols. More details are available in the [API documentation][post options]. |
| minLen        | 0             | Sets the minimum length of the expected answer.                                               |
| maxLen        | 0             | Sets the maximum length of the expected answer.                                               |
| phrase        | 0             | Indicates whether the response consists of multiple words.                                    |
| caseSensitive | 0             | Determines if the response must match the original case.                                      |
| calc          | 0             | Specifies if the captcha involves a mathematical calculation.                                 |
| lang          | -             | Defines the language of the captcha. Refer to the [list of supported languages].              |
| hintImg       | -             | Provides an additional image as a hint for workers alongside the captcha.                     |
| hintText      | -             | Displays a text hint or task description for workers along with the captcha.                  |


Below, you can find basic examples for each captcha type. For more examples with all available options, check the [examples directory].

### Normal Captcha

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_normal_captcha)</sup>

To solve a standard captcha (distorted text on an image), use the following method. This method can also be applied for text recognition in any image.


```python
result = solver.normal('path/to/captcha.jpg', param1=..., ...)
# OR
result = solver.normal('https://site-with-captcha.com/path/to/captcha.jpg', param1=..., ...)
```

```python
result = solver.audio('path/to/captcha.mp3', lang = 'lang', param1=..., ...)
# OR
result = solver.audio('https://site-with-captcha.com/path/to/captcha.mp3', lang = 'lang', param1=..., ...)
```

### Text Captcha

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_text_captcha)</sup>

This method can be used to solve captchas that require answering a question presented in plain text.

```python
result = solver.text('If tomorrow is Saturday, what day is today?', param1=..., ...)
```

### reCAPTCHA v2

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_recaptchav2_new)</sup>

Use the following method to solve reCAPTCHA V2 and retrieve a token for bypassing the protection.

```python
result = solver.recaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                          url='https://mysite.com/page/with/recaptcha',
                          param1=..., ...)
```

### reCAPTCHA v3

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_recaptchav3)</sup>

This method offers a reCAPTCHA V3 solver and returns a token.

```python
result = solver.recaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                            url='https://mysite.com/page/with/recaptcha-v3',
                            version='v3',
                            param1=..., ...)
```

### hCaptcha

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_hcaptcha)</sup>

Use the following method to solve hCaptcha and retrieve a token for bypassing the protection.

```python
result = solver.hcaptcha(sitekey='bf8ccfbf-6a05-45f6-982a-7a7964c2f50c',
                         url='https://portalunico.siscomex.gov.br',
                         invisible=0,
                         domain='hcaptcha.com',
                         # proxy={
                         #     'type': 'HTTPS',
                         #     'uri': 'login:password@IP_address:PORT'
                         # }
                         )
```

### FunCaptcha

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_funcaptcha_new)</sup>

FunCaptcha (Arkoselabs) solving method that returns a token.

```python
result = solver.funcaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                            url='https://mysite.com/page/with/funcaptcha',
                            param1=..., ...)

```

### GeeTest

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_geetest)</sup>

Method for solving GeeTest puzzle captcha. Returns a set of tokens in JSON format.

```python
result = solver.geetest(gt='f1ab2cdefa3456789012345b6c78d90e',
                        challenge='12345678abc90123d45678ef90123a456b',
                        url='https://www.site.com/page/',
                        param1=..., ...)

```

### GeeTest v4

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_geetest_v4)</sup>

Use this method to solve GeeTest v4. The response is returned in JSON format.

```python
result = solver.geetest_v4(captcha_id='e392e1d7fd421dc63325744d5a2b9c73',
                            url='https://www.site.com/page/',
                            param1=..., ...)

```

### Cloudflare Turnstile

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_cloudflare_turnstile)</sup>

Use this method to solve Cloudflare Turnstile. The response is returned as JSON containing the token.

```python
result = solver.turnstile(sitekey='0x1AAAAAAAAkg0s2VIOD34y5',
                            url='http://mysite.com/',
                            data='foo',
                            pagedata='bar',
                            action='challenge',
                            useragent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
```

### KeyCaptcha

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_keycaptcha)</sup>

Token-based method for solving KeyCaptcha.

```python
result = solver.keycaptcha(s_s_c_user_id=10,
    				   s_s_c_session_id='493e52c37c10c2bcdf4a00cbc9ccd1e8',
    				   s_s_c_web_server_sign='9006dc725760858e4c0715b835472f22-pz-',
    				   s_s_c_web_server_sign2='2ca3abe86d90c6142d5571db98af6714',
    				   url='https://www.keycaptcha.ru/demo-magnetic/',
    				   param1=..., ...)

```

### Grid

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_grid)</sup>

The grid method was initially known as the Old reCAPTCHA V2 method. It can be used to bypass any captcha that requires selecting specific grid boxes on an image. Returns the numbers of the selected boxes.

```python
result = solver.grid('path/to/captcha.jpg', param1=..., ...)
```

### ClickCaptcha

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_clickcaptcha)</sup>

The ClickCaptcha method returns the coordinates of specific points on the captcha image. It is useful when solving captchas that require clicking on designated areas within the image.

```python
result = solver.coordinates('path/to/captcha.jpg', param1=..., ...)
```

### Rotate

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#solving_rotatecaptcha)</sup>

This method is used to solve captchas that require rotating an object. It is primarily utilized for bypassing FunCaptcha and returns the rotation angle.

```python
result = solver.rotate('path/to/captcha.jpg', param1=..., ...)
```

### Canvas

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#canvas)</sup>

The canvas method is used for captchas that require drawing a line around an object in an image. It returns a set of point coordinates for constructing a polygon.

```python
result = solver.canvas('path/to/captcha.jpg', param1=..., ...)
```

## Other methods

### send / get_result

These methods allow manual captcha submission and answer polling. The `send()` method supports sending any captcha type. To specify the captcha type, you must manually set the `method` parameter, for example, `method='recaptcha'` for solving reCAPTCHA.  
You can find the available values for the `method` parameter in the [API documentation](https://solvecaptcha.com/captcha-solver-api).

Example of manually solving a Normal captcha:

```python
import time
. . . . .


id = solver.send(file='path/to/captcha.jpg')
time.sleep(20)

code = solver.get_result(id)
```

### balance

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#additional)</sup>

Use this method to retrieve your account balance.

```python
balance = solver.balance()
```

### report

<sup>[API method description.](https://solvecaptcha.com/captcha-solver-api#complain)</sup>

Use this method to report whether a captcha answer was correct or incorrect.

```python
solver.report(id, True) # captcha solved correctly
solver.report(id, False) # captcha solved incorrectly
```

## Error handling

If an error occurs, the captcha solver throws an exception. Proper error handling is essential. We recommend using `try except` to manage exceptions.  
A complete list of possible errors can be found in the [API documentation](https://solvecaptcha.com/captcha-solver-api#error_handling).

```python
try:
    result = solver.text('If tomorrow is Saturday, what day is today?')
except ValidationException as e:
    # invalid parameters passed
	print(e)
except NetworkException as e:
	# network error occurred
	print(e)
except ApiException as e:
    # api respond with error
	print(e)
except TimeoutException as e:
    # captcha is not solved so far
	print(e)
```

## Proxies

You can provide your proxy as an additional argument for the following methods: reCAPTCHA, FunCaptcha, GeeTest, GeeTest v4, KeyCaptcha, hCaptcha, Turnstile, Amazon WAF, and other captchas.  

The proxy will be passed to the API to facilitate captcha solving.  

We also offer our own proxies that you can use.

```python
proxy={
    'type': 'HTTPS',
    'uri': 'login:password@IP_address:PORT'
}
```

## Async calls

You can also perform asynchronous calls using [asyncio], for example:

```python
import asyncio
import concurrent.futures
from solvecaptcha import Solvecaptcha

API_KEY = "YOUR_API_KEY"
image = "data:image/png;base64,iVBORw0KGgoA..."

async def captchaSolver(image):
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, lambda: Solvecaptcha(API_KEY).normal(image))
        return result

captcha_result = asyncio.run(captchaSolver(image))
```

## Examples

Examples of solving all supported captcha types can be found in the [examples] directory.

## Examples using Selenium

We also have a separate repository where you can find examples of captcha solving using the [Selenium](https://pypi.org/project/selenium/) \ [seleniumbase](https://seleniumbase.io/) library. 
- [Python hCaptcha Solver: Bypass hCaptcha with Proxy using Selenium and SolveCaptcha SDK](https://github.com/solvercaptcha/hcaptcha-solver-seleniumbase-python)

## Useful articles

- [Solve and bypass Google reCAPTCHA, hCaptcha, Image CAPTCHA,  Cloudflare Challenge and any captcha in Selenium with captcha solver.](https://solvecaptcha.com/captcha-solver/selenium-captcha-solver-bypass)
- [Solve and bypass Google reCAPTCHA, hCaptcha, Arkose FunCaptcha, Cloudflare Turnstile, and any captcha in Puppeteer with captcha solver.](https://solvecaptcha.com/captcha-solver/puppeteer-captcha-solver-bypass)

## Get in touch

<a href="mailto:info@solvecaptcha.com"><img src="https://github.com/user-attachments/assets/539df209-7c85-4fa5-84b4-fc22ab93fac7" width="80" height="30"></a>
<a href="https://solvecaptcha.com/support/faq#create-ticket"><img src="https://github.com/user-attachments/assets/be044db5-2e67-46c6-8c81-04b78bd99650" width="81" height="30"></a>

## License

The code in this repository is licensed under the MIT License. For more details, see the [LICENSE](./LICENSE) file.

<!-- Shared links for README.md -->
[Solvecaptcha]: https://solvecaptcha.com/
[pingback settings]: https://solvecaptcha.com/captcha-solver-api#manage_pingback
[post options]: https://solvecaptcha.com/captcha-solver-api#normal_post
[list of supported languages]: https://solvecaptcha.com/captcha-solver-api#language
[examples directory]: /examples
[asyncio]: https://docs.python.org/3/library/asyncio.html
[examples]: ./examples
