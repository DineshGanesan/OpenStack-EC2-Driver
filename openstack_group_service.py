# Copyright (c) 2014 ThoughtWorks
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

class OpenstackGroupService():

    def __init__(self, security_group_manager):
        self.security_group_manager = security_group_manager

    def get_group(self, group_name):
        return [group for group in self.security_group_manager.list() if group.name == group_name][0]