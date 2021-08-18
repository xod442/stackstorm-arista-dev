# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

import pymongo
from lib.actions import MongoBaseAction
import random import random


class loadDb(MongoBaseAction):
    def run(self, inventory):

        mydb = self.dbclient["app_db"]
        known = mydb["aristacvp"]

        new_inventory={}

        for inv in inventory:
            myquery = { "u_systemmacaddress" : inv['u_systemMacAddress'] }
            records = known.find(myquery).count()
            if records == 0:
                new_inventory['u_vendor']='arista'
                new_inventory['u_devicestatus']=inv['u_deviceStatus']
                new_inventory['u_hostname']=inv['u_hostname']
                new_inventory['u_ipaddress']=inv['u_ipAddress']
                new_inventory['u_modelname']=inv['u_modelName']
                new_inventory['u_serialnumber']=inv['u_serialNumber']
                new_inventory['u_systemmacaddress']=inv['u_systemMacAddress']
                new_inventory['u_type']=inv['u_type']
                new_inventory['u_version']=inv['u_version']
                new_inventory['u_ztpmode']=inv['u_ztpMode']
                new_inventory['u_process']='no'
                
                id = random()
                new_inventory['_id']=id   
               
                write_record = known.insert_one(new_inventory)
        return (records)
