import _cli
from _getdata import latest_qtr, download, extract

args = _cli.parser.parse_args()

# download only
if args.download:
    download(
        qtr=args.qtr,
        startqtr=args.startqtr,
        endqtr=args.endqtr,
        path=args.path)

# extract only
elif args.extract:
    extract(
        path=args.path,
        destination=args.destination,
        singledir=args.singledir,
        rmzip=args.rmzip)

# download & extract
else:
    download(
        qtr=args.qtr,
        startqtr=args.startqtr,
        endqtr=args.endqtr,
        path=args.path)

    extract(
        path=args.path,
        destination=args.destination,
        singledir=args.singledir,
        rmzip=args.rmzip)