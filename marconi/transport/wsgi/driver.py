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

from marconi.common import config
from marconi import transport


cfg = config.namespace('drivers:transport:wsgi').from_options(port=8888)


class Driver(transport.DriverBase):

    def __init__(self, queue_controller, message_controller,
                 claim_controller):

        # E.g.:
        #
        # self._queue_controller.create(tenant_id, queue_name)
        # self._queue_controller.set_metadata(tenant_id, queue_name, metadata)
        #
        self._queue_controller = queue_controller
        self._message_controller = message_controller
        self._claim_controller = claim_controller

        self.app = api = falcon.API()

    def listen(self):
        pass
