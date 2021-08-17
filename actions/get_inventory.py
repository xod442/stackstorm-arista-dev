# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"


from lib.actions import AristaBaseAction

class get_inventory(AristaBaseAction):
    def run(self):
        inventory = self.client.api.get_inventory()
        if isinstance(inventory, list):
            # Create a empty list for inventory
            selectInventory = []
            # Loop through the switch inventory and pick the fields we want
            for switch in inventory:
                out = {
                       'u_version': switch['version'],
                       'u_systemMacAddress': switch['systemMacAddress'],
                       'u_deviceStatus': switch['deviceStatus'],
                       'u_modelName': switch['modelName'],
                       'u_hostname': switch['hostname'],
                       'u_type': switch['type'],
                       'u_ztpMode': switch['ztpMode'],
                       'u_serialNumber': switch['serialNumber'],
                       'u_ipAddress': switch['ipAddress'],
                       }
                selectInventory.append(out)

            return (True, selectInventory)
        return (False, selectInventory)
