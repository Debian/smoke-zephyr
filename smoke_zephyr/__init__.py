#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  smoke_zephyr/__init__.py
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the project nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import collections

# Semantic Versioning: http://semver.org/spec/v2.0.0.html
version_info = collections.namedtuple('version_info', ['major', 'minor', 'micro'])(1, 2, 1)
"""A tuple representing the version information in the format ('major', 'minor', 'micro')"""

version_label = ''
"""A version lable such as alpha or beta."""
version = "{0}.{1}.{2}".format(version_info.major, version_info.minor, version_info.micro)
"""A string representing the full version information."""

# distutils_version is compatible with distutils.version classes
distutils_version = version
"""A string sutiable for being parsed by :py:mod:`distutils.version` classes."""

if version_label:
	version += '-' + version_label
	distutils_version += version_label[0]
	if version_label[-1].isdigit():
		distutils_version += version_label[-1]
	else:
		distutils_version += '0'

__version__ = distutils_version
