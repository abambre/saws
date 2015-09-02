# -*- coding: utf-8
from __future__ import unicode_literals
import os
import re
from optparse import OptionParser, OptionError, OptionGroup


# Global AWS built-in commands, listed for syntax highlighting
# TODO: Move this to SOURCES.txt
GLOBAL_OPTIONS = [
    '--debug',
    '--endpoint-url',
    '--no-verify-ssl',
    '--no-paginate',
    '--output',
    '--profile',
    '--region',
    '--version',
    '--color',
    '--query',
    '--no-sign-request',
]

# AWS built-in commands, listed for syntax highlighting
# TODO: Generate a full list of these commands and store them
# in data/SOURCES.TXT
RESOURCE_OPTIONS = [
    '--instance-ids',
    '--bucket',
    '--load-balancer-names',
]

# AWS CLI entry point, listed for syntax highlighting
AWS_COMMAND = [
    'aws',
]

# iawscli docs
AWS_DOCS = [
    'docs',
]

# iawscli shortcuts
SHORTCUTS = {
    'ls',
}

# iawscli mapping of shortcuts to full commands
SHORTCUTS_MAP = {
    'aws ec2 ls': 'aws ec2 describe-instances',
    'aws dynamodb ls': 'aws dynamodb list-tables',
    'aws emr ls': 'aws emr list-clusters',
    'aws elb ls': 'aws elb describe-load-balancers',
}

def generate_all_commands():
    p = os.path.dirname(os.path.realpath(__file__))
    f = os.path.join(p, 'data/SOURCES.txt')
    commands = []
    sub_commands = []
    COMMANDS_INDEX = 2
    SUB_COMMANDS_INDEX = 3
    parsing_sub_commands = False
    with open(f) as fp:
        for line in fp:
            line = re.sub('\n', '', line)
            if '[commands]' in line:
                continue
            if '[sub_commands]' in line:
                parsing_sub_commands = True
                continue
            if not parsing_sub_commands:
                commands.append(line)
            else:
                sub_commands.append(line)
    return sorted(list(commands)), sorted(list(sub_commands))