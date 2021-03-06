#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2015 Donne Martin. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from __future__ import unicode_literals
from __future__ import print_function
import unittest
from test_completer import CompleterTest  # NOQA
from test_commands import CommandsTest  # NOQA
from test_resources import ResourcesTest  # NOQA
from test_options import OptionsTest  # NOQA
from test_saws import SawsTest  # NOQA
from test_toolbar import ToolbarTest  # NOQA
from test_keys import KeysTest  # NOQA
from test_saws2 import SawsTest  # NOQA
try:
    from test_cli import CliTest  # NOQA
except:
    # pexpect import fails on Windows
    pass


if __name__ == '__main__':
    unittest.main()
