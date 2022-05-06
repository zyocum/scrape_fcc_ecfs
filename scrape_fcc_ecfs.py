#!/usr/bin/env python3

"""Scrape Federal Communications Commssion (FCC) Express Comments Filing
System (ECFS) via https://publicapi.fcc.gov/ecfs/filings"""

import json
import os
import sys

import requests

from time import ctime, time, sleep
from getpass import getpass

URL = 'https://publicapi.fcc.gov/ecfs/filings'

def get_filings(proceedings_name, api_key, limit=25, offset=0, timeout=3600):
    """Generate {limit} filings starting from {offset}."""
    params = {
        'api_key': api_key,
        'express_comment': '1',
        'limit': limit,
        'offset': offset,
        'proceedings.name': proceedings_name,
        'sort': 'date_received,ASC'
    }
    response = requests.get(URL, params=params)
    while response.status_code in {429, 503}:
        now = time()
        later = now + timeout
        message = (
            f'{ctime(now)}: HTTP status {response.status_code} '
            f'({response.reason}). '
            f'Retrying in {timeout} seconds at {ctime(later)} ...'
        )
        print(message, file=sys.stderr)
        sleep(timeout)
        response = requests.get(URL, params=params)
    if response.status_code == 200:
        try:
            yield from response.json().get('filing', [])
        except Exception:
            raise StopIteration
    else:
        message = (
            f'{ctime(now)}: HTTP status {response.status_code} '
            f'({response.reason}): {response.url}'
        )
        print(message, file=sys.stderr)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__doc__
    )
    parser.add_argument(
        '-p', '--proceedings-name',
        required=True,
        help='Proceedings docket ID (e.g., "17-108")'
    )
    parser.add_argument(
        '-k', '--api-key',
        default=None,
        help=(
            'data.gov public API key (you can request a key from '
            "https://api.data.gov/signup if you don't have one already; also "
            'you can set a DATA_DOT_GOV_API_KEY environment variable to '
            'avoid entering your key)'
        )
    )
    parser.add_argument(
        '-l', '--limit',
        default=25,
        type=int,
        help='The number of filings to get per request (max=10000)'
    )
    parser.add_argument(
        '-m', '--max-offset',
        default=25,
        type=int,
        help='The maximum offset (should be a multiple of --limit)'
    )
    args = parser.parse_args()
    api_key = (
        os.environ.get('DATA_DOT_GOV_API_KEY') or
        args.api_key or
        getpass(prompt='api.data.gov API key: ')
    )
    for offset in range(0, args.max_offset, args.limit):
        # get all the filings in range(offset, offset+limit)
        filings = get_filings(
            args.proceedings_name,
            api_key,
            limit=args.limit,
            offset=offset
        )
        # print records to stdout as JSON
        for filing in filings:
            print(json.dumps(filing, ensure_ascii=False))
