#!/usr/bin/python3

import sys
import os
import csv


OPERATOR_NAME = 'Daria TM'
CMD_LINE = 'wpull %s --strip-session-id --no-check-certificate --no-robots --page-requisites --no-parent --sitemaps --inet4-only --timeout 20 --tries 3 --waitretry 5 --recursive --level inf --span-hosts --retry-connrefused --retry-dns-error --delete-after --warc-append --warc-cdx -U "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" -d -a %s/%s.log --database %s/sitearchive-%s.db --warc-file "%s/%s" --warc-header "operator: %s" --warc-header "downloaded-by: DTM" --domains %s --concurrent 4&'

def run(filename):
    f = open(filename, 'r', encoding='utf8')
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        run_domain(row['url'].strip(), row['domain'].strip())
    f.close()
    pass

def run_domain(url, domain):
    print('Launching wpull for domain %s, url %s' % (domain, url))
    os.makedirs(domain, exist_ok=True)
    os.system(CMD_LINE % (url, domain, domain, domain, domain, domain, domain, OPERATOR_NAME, domain))
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        print('wpull_mass.py <filename>')
