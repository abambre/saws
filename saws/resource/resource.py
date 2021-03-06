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
import subprocess
import traceback
from abc import ABCMeta, abstractmethod


class Resource():
    """Encapsulates an AWS resource.

    Abstract base class for resources.

    Attributes:
        * OPTION: A string representing the option that will cause the resource
            completions to be displayed when typed.
        * QUERY: A string representing the AWS query to list all resources
        * resources: A list of resources.
        * log_exception: A callable log_exception from SawsLogger.
    """

    __metaclass__ = ABCMeta

    OPTION = ''
    QUERY = ''

    def clear_resources(self):
        """Clears the resource.

        Args:
            * None.

        Returns:
            None.
        """
        self.resources[:] = []

    @abstractmethod
    def query_resource(self):
        """Queries and stores resources from AWS.

        Args:
            * None.

        Returns:
            None.
        """
        pass

    def _query_aws(self, query):
        """Sends the given query to the shell for processing.

        The awscli will process the command and output its results.  The
        results are captured and returned.

        Args:
            * command: A string representing the given query.

        Returns:
            A string representing the awscli output.
        """
        try:
            return subprocess.check_output(query,
                                           universal_newlines=True,
                                           shell=True)
        except Exception as e:
            self.log_exception(e, traceback)
