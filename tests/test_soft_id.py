#!/usr/bin/env python3
import unittest

try:
    from .abstract import AbstractTest, ApiClient
    from solvecaptcha import Solvecaptcha
except ImportError:
    from abstract import AbstractTest, ApiClient
    from solvecaptcha import Solvecaptcha


class SoftIdTest(AbstractTest):
    '''Regression test: a custom softId must reach the API request.'''

    def test_custom_soft_id_is_sent(self):

        solver = Solvecaptcha('API_KEY', softId=999, pollingInterval=1)
        solver.api_client = ApiClient()

        b64 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        solver.normal(file=b64)

        self.assertEqual(solver.api_client.incomings['soft_id'], 999)


if __name__ == '__main__':

    unittest.main()
