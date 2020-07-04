#!/usr/bin/env python3
import json
import urllib.request


def get_urls(url):
    urls = []
    response = urllib.request.urlopen(url)
    for url in response.readlines():
        decoded_url = url.decode('utf-8').replace('\n', '')
        if not decoded_url.startswith('#'):
            urls.append(decoded_url)
    return urls


def blocklist_to_hohser_json(blocklist, method):
    blocked_urls = []
    for url in blocklist:
        blocked_urls.append({'domainName': url, 'display': method})
    return blocked_urls


def main():
    url = input('URL: ')
    urls = get_urls(url)
    method = input('Highlight, Set Back, Hide, (Default: Hide)')
    print('Creating list...')
    if method.lower() == 'highlight':
        blocked_urls = blocklist_to_hohser_json(blocklist=urls, method='HIGHLIGHT')
    elif method.lower() == 'set back':
        blocked_urls = blocklist_to_hohser_json(blocklist=urls, method='PARTIAL_HIDE')
    else:
        blocked_urls = blocklist_to_hohser_json(blocklist=urls, method='FULL_HIDE')

    with open('hohser_blocklist.json', 'w') as outfile:
        json.dump(blocked_urls, outfile)

    print('Finished.')


if __name__ == '__main__':
    main()
