"""
    Copyright 2015 Impera

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Contact: bart@impera.io
"""
from impera.plugins.base import plugin
from operator import attrgetter

@plugin
def bind_zone_name(zone : "dns::Zone") -> "std::hoststring":
    """
        Generate the bind zonename
    """
    if hasattr(zone, "ip_prefix"):
        parts = zone.ip_prefix.split(".")
        parts.reverse()
        addr = ".".join(parts)

        return addr + ".in-addr.arpa"

    return zone.domain

@plugin
def ip_to_arpa(ip_addr : "ip::ip") -> "std::hoststring":
    """
        Convert an ip to the addr.arpa notation
    """
    parts = ip_addr.split(".")
    parts.reverse()
    addr = ".".join(parts)

    return addr + ".in-addr.arpa"

@plugin
def records_in_zone(records : "list", zone : "dns::zone") -> "list":
    """
        Return all the records that belong in the given zone
    """
    return_list = []
    for record in records:
        if record.record[-len(zone):] == zone:
            return_list.append(record)

    return_list = sorted(return_list, key = attrgetter('record'))

    return return_list

@plugin
def filter_record(record : "std::hoststring", zone : "dns::zone") -> "std::hoststring":
    """
        Filter the zone part from the record
    """
    return record[:-(len(zone) + 1)]

