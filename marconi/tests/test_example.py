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

from marconi.tests import util as testing


class TestExample(testing.TestBase):

    def setUp(self):
        """Run before each test method."""
        super(TestExample, self).setUp()

        # [Your code here]

    def tearDown(self):
        """Run after each test method."""
        # [Your code here]

        super(TestExample, self).tearDown()

    def test_simple(self):
        """Doesn't really test much."""
        self.assertTrue(True)
