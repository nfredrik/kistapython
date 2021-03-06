import argparse

def ping(tags, region=None, ami=None):
    # some AWS/boto code here
    return True

def create_parser():
    parser = argparse.ArgumentParser(
        description='Ping a number of servers in AWS based on tags'
    )

    parser.add_argument(
        'tags', nargs='+',
        help='Tags to search for in AWS'
    )

    parser.add_argument(
        '-R', '--region', type=str, required=False,
        help='AWS region to limit search to'
    )

    parser.add_argument(
        '-A', '--ami', type=str, required=False,
        help='AWS AMI to limit search to'
    )

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    ping(args.tags, args.region, args.ami)

if __name__ == '__main__':
    main()
