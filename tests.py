#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tio
import asyncio
import unittest

site = Tio.Tio()

class TestOutput(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def test_hello(self):
        async def go(self):
            req = site.new_request('python3', "print('Hello World')")
            res = site.send(req)
            async_res = await site.async_send(req)
            self.assertEqual(res.split('\n')[0], async_res.split('\n')[0], 'Hello World')
        self.loop.run_until_complete(go(self))

    def tearDown(self):
        self.loop.close()

    def test_cflags(self):
        code = "#include <iostream>\nint main() {int a {2};}"
        req = site.new_request('cpp-gcc', code, cflags=['-std=c++98'])
        res = site.send(req)
        self.assertIn("warning: extended initializer lists only available with -std=c++11 or -std=gnu++11", res)

    def test_options(self):
        req = site.new_request('python3', "assert 2 > 3", options=['-OO'])
        res = site.send(req)
        self.assertNotIn("AssertionError", res)

    def test_inputs(self):
        req = site.new_request('python3', "print(input())", inputs='there')
        res = site.send(req)
        self.assertEqual(res.split('\n')[0], 'there')
