# Copyright 2013 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_log import versionutils

from keystone.catalog.backends import sql

_OLD = 'keystone.contrib.endpoint_filter.backends.sql.EndpointFilter'
_NEW = 'sql'


class EndpointFilter(sql.Catalog):
    @versionutils.deprecated(
        as_of=versionutils.deprecated.MITAKA,
        in_favor_of=_NEW,
        what=_OLD,
        remove_in=2)
    def __init__(self, *args, **kwargs):
        super(EndpointFilter, self).__init__(*args, **kwargs)
