# Copyright 2013 Rackspace, Inc.
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

import marconi
from marconi.tests import util as testing


class TestSimple(testing.TestBase):

    def test_simple(self):
        """Doesn't really test much."""
        conf_file = self.conf_path('wsgi_reference.conf')
        boot = marconi.Bootstrap(conf_file)
        transport = boot.transport
        wsgi_app = transport.app
        self.assertTrue(True)
