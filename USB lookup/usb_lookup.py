"""Script to lookup USB vendor and product values."""
from __future__ import print_function
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import argparse

__authors__=""
__date__ = 20181027
__description__ = "USB vid/pid lookup utility"


def main(vid, pid):
    url = 'http://www.linux-usb.org/usb.ids'
    usbs = {}
    usb_file = urlopen(url)
    curr_id = ''

    for line in usb_file:
        if isinstance(line, bytes):
            line = line.decode('latin-1')
        if line.startswith('#') or line in ('\n', '\t'):
            continue
        else:
            if not(line.startswith('\t')) and line[0].isalnum():
                uid, name = line.strip().split(' ', 1)
                curr_id = uid
                usbs[uid] = [name.strip(), {}]
            elif line.startswith('\t') and line.count('\t') == 1:
                uid, name = line.strip().split(' ', 1)
                usbs[curr_id][1][uid] = name.strip()

    search_key(vid, pid, usbs)


def search_key(vendor_key, product_key, usb_dict):
    vendor = usb_dict.get(vendor_key, None)
    if vendor is None:
        print('Vendor ID not found')
        exit()

    product = vendor[1].get(product_key, None)
    if product is None:
        print('Vendor: {}\nProduct Id not found.'.format(
            vendor[0]))
        exit(0)

    print('Vendor: {}\nProduct: {}'.format(vendor[0], product))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__description__,
        epilog='Built by {}. Version {}'.format(
            ", ".join(__authors__), __date__),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('vid', help="VID value")
    parser.add_argument('pid', help="pID value")
    args = parser.parse_args()
    main(args.vid, args.pid)
