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

from marconi.common import config
from marconi.storage import reference as storage
from marconi.transport.wsgi import driver as wsgi


cfg = config.project('marconi').from_options()


class Main(object):
    """
    Defines the Marconi Kernel

    The Kernel loads up drivers per a given configuration, and manages their
    lifetimes.
    """

    def __init__(self, config_file=None):
        #TODO(kgriffs): Error handling
        cfg.load(config_file)

        #TODO(kgriffs): Determine driver types from cfg
        self.storage = storage.Driver()
        self.transport = wsgi.Driver(self.storage.queue_controller,
                                     self.storage.message_controller,
                                     self.storage.claim_controller)

    def run(self):
        self.transport.listen()
