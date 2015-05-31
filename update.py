#!/usr/bin/env python3


import json
import sys

OLD_INTEREST = '2b6b0e77-01fa-4830-9420-3ee44602e5a9'
NEW_INTEREST = '9968a4e6-6fb9-4bd3-9193-783b9ed3aa32'

OLD_FREELANCING = '19aba6b8-f026-472a-978a-6e3d284c4097'
NEW_FREELANCING = 'a7bef6f7-1ac3-47a6-84e0-54494a5d53ff'


with open(sys.argv[1]) as oldfp:
    with open(sys.argv[2]) as newfp:
        old = json.load(oldfp)
        new = json.load(newfp)

        tx = old['transactions']
        ntx = new['transactions']
        old_interest_tx = filter(lambda x: OLD_INTEREST in x['tag_ids'], tx)

        for t_id in map(lambda x: x['id'], old_interest_tx):
            t = list(filter(lambda x: x['id'] == t_id, ntx))[0]
            if NEW_INTEREST not in t['tag_ids']:
                t['tag_ids'].append(NEW_INTEREST)

        old_freelancing_tx = filter(lambda x: OLD_FREELANCING in x['tag_ids'], tx)
        for t_id in map(lambda x: x['id'], old_freelancing_tx):
            t = list(filter(lambda x: x['id'] == t_id, ntx))[0]
            if NEW_FREELANCING not in t['tag_ids']:
                t['tag_ids'].append(NEW_FREELANCING)

        print(json.dumps(new, indent=4))
