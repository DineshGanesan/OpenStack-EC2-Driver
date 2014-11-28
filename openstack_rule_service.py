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

class OpenstackRuleService:
    def __init__(self, group_service, openstack_rule_transformer):
        self.group_service = group_service
        self.openstack_rule_transformer = openstack_rule_transformer

    def get_rules_for_group(self, group_name):
        openstack_group = self.group_service.get_group(group_name)
        return set([self.openstack_rule_transformer.to_rule(rule) for rule in openstack_group.rules])
        # return self.group_service.get_group(group_name).rules