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
from impera.plugins import plugin
from operator import attrgetter

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
def filter_record(record : "std::hoststring", zone : "dns::Zone") -> "std::hoststring":
    """
        Filter the zone part from the record
    """
    return record[:-(len(zone) + 1)]

@plugin
def quote(data: "string") -> "string":
    return "\"" + data + "\""
