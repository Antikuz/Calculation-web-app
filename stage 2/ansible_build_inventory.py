#!/usr/bin/python3

# Parse ansible community.docker.docker_compose and build inventory file

import sys
import json
data = sys.argv[1]

data = json.loads(data)['services']
hosts = {}

for service in data:
    hosts[service] = {}
    for host in data[service]:
        hosts[service][host] = {}
        for network in data[service][host]['networks']:
            ip = data[service][host]['networks'][network]['IPAddress']
            try:
                hosts[service][host]['ip'].append(ip)
            except KeyError:
                hosts[service][host]['ip'] = []
                hosts[service][host]['ip'].append(ip)

with open('inventory', 'w', encoding='utf8') as fh:
    for service in hosts:
        fh.write(f'[{service}]\n')
        for host in hosts[service]:
            ip = hosts[service][host]['ip'][0]
            fh.write(f'{ip}\n')
        fh.write('\n')
