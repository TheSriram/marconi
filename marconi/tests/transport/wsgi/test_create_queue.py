# Copyright (c) 2013 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import falcon
from falcon import testing

import marconi
from marconi.tests import util


class TestCreateQueue(util.TestBase):

    def setUp(self):
        super(TestCreateQueue, self).setUp()

        conf_file = self.conf_path('wsgi_reference.conf')
        boot = marconi.Bootstrap(conf_file)
        transport = boot.transport

        self.app = transport.app
        self.srmock = testing.StartResponseMock()

    def test_simple(self):
        env = testing.create_environ('/v1/480924/queues/fizbat',
                                     method="PUT")

        self.app(env, self.srmock)
        self.assertEquals(falcon.HTTP_200, self.srmock.status)
