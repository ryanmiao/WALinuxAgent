# Windows Azure Linux Agent
#
# Copyright 2014 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Requires Python 2.4+ and Openssl 1.0+
#

import os
import re
import platform

def get_distro():
    if 'FreeBSD' in platform.system():
        release = re.sub('\-.*\Z', '', str(platform.release()))
        osinfo = ['freebsd', release, '', 'freebsd']
    if 'linux_distribution' in dir(platform):
        osinfo = list(platform.linux_distribution(full_distribution_name=0))
        full_name = platform.linux_distribution()[0].strip()
        osinfo.append(full_name)
    else:
        osinfo = platform.dist()

    #The platform.py lib has issue with detecting oracle linux distribution.
    #Merge the following patch provided by oracle as a temparory fix.
    if os.path.exists("/etc/oracle-release"):
        osinfo[2] = "oracle"
        osinfo[3] = "Oracle Linux"

    #Remove trailing whitespace and quote in distro name
    osinfo[0] = osinfo[0].strip('"').strip(' ').lower()
    return osinfo

AGENT_NAME = "AzureLinuxAgent"
agent_long_name = "Azure Linux Agent"
AGENT_VERSION = '2.1.1-pre'
agent_long_version = "{0}-{1}".format(AGENT_NAME, AGENT_VERSION)
agent_description = """\
The Azure Linux Agent supports the provisioning and running of Linux
VMs in the Azure cloud. This package should be installed on Linux disk
images that are built to run in the Azure environment.
"""

__distro__ = get_distro()
DISTRO_NAME = __distro__[0]
DISTRO_VERSION = __distro__[1]
DISTRO_CODE_NAME = __distro__[2]
DISTRO_FULL_NAME = __distro__[3]

