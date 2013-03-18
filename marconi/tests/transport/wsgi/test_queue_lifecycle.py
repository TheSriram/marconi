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

import json

import falcon
from falcon import testing
from testtools import matchers

import marconi
from marconi.tests import util
from marconi import transport


class TestCreateQueue(util.TestBase):

    def setUp(self):
        super(TestCreateQueue, self).setUp()

        conf_file = self.conf_path('wsgi_reference.conf')
        boot = marconi.Bootstrap(conf_file)

        self.app = boot.transport.app
        self.srmock = testing.StartResponseMock()

    def test_simple(self):
        doc = '{"messages": {"ttl": 600}}'
        env = testing.create_environ('/v1/480924/queues/gumshoe',
                                     method="PUT", body=doc)

        self.app(env, self.srmock)
        self.assertEquals(self.srmock.status, falcon.HTTP_201)

        location = ('Location', '/v1/480924/queues/gumshoe')
        self.assertThat(self.srmock.headers, matchers.Contains(location))

        env = testing.create_environ('/v1/480924/queues/gumshoe')
        result = self.app(env, self.srmock)
        self.assertEquals(self.srmock.status, falcon.HTTP_200)
        self.assertEquals(result, [doc])

    def test_no_metadata(self):
        env = testing.create_environ('/v1/480924/queues/fizbat', method="PUT")

        self.app(env, self.srmock)
        self.assertEquals(self.srmock.status, falcon.HTTP_400)

    def test_too_much_metadata(self):
        doc = '{"messages": {"ttl": 600}, "padding": "%s"}'
        padding_len = transport.MAX_QUEUE_METADATA_SIZE - (len(doc) - 2) + 1
        doc = doc % ('x' * padding_len)
        env = testing.create_environ('/v1/480924/queues/fizbat',
                                     method="PUT", body=doc)

        self.app(env, self.srmock)
        self.assertEquals(self.srmock.status, falcon.HTTP_400)

    def test_way_too_much_metadata(self):
        doc = '{"messages": {"ttl": 600}, "padding": "%s"}'
        padding_len = transport.MAX_QUEUE_METADATA_SIZE * 100
        doc = doc % ('x' * padding_len)
        env = testing.create_environ('/v1/480924/queues/gumshoe',
                                     method="PUT", body=doc)

        self.app(env, self.srmock)
        self.assertEquals(self.srmock.status, falcon.HTTP_400)

    def test_custom_metadata(self):
        # Set
        doc = '{"messages": {"ttl": 600}, "padding": "%s"}'
        padding_len = transport.MAX_QUEUE_METADATA_SIZE - (len(doc) - 2)
        doc = doc % ('x' * padding_len)
        env = testing.create_environ('/v1/480924/queues/gumshoe',
                                     method="PUT", body=doc)

        self.app(env, self.srmock)
        self.assertEquals(self.srmock.status, falcon.HTTP_201)

        # Get
        env = testing.create_environ('/v1/480924/queues/gumshoe')
        result = self.app(env, self.srmock)
        result_doc = json.loads(result[0])
        self.assertEquals(result_doc, json.loads(doc))

    def test_update_metadata(self):
        # Create
        doc1 = '{"messages": {"ttl": 600}}'
        env = testing.create_environ('/v1/480924/queues/xyz',
                                     method="PUT", body=doc1)

        self.app(env, self.srmock)

        # Update
        doc2 = '{"messages": {"ttl": 100}}'
        env = testing.create_environ('/v1/480924/queues/xyz',
                                     method="PUT", body=doc2)

        self.app(env, self.srmock)

        # Get
        env = testing.create_environ('/v1/480924/queues/xyz')
        result = self.app(env, self.srmock)
        result_doc = json.loads(result[0])
        self.assertEquals(result_doc, json.loads(doc2))
