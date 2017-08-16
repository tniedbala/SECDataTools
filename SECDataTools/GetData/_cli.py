import sys, argparse

parser = argparse.ArgumentParser(
    description='''Download and extract zip archive(s) from 
    https://www.sec.gov/dera/data/financial-statement-data-sets.html.''')

parser.add_argument(
    '-path',
    type=str,
    help='''Directory path that zip archives will be saved to. May be absolute 
    or relative. Defaults to (creates) an ./sec_zip subdirectory within the 
    current working directory when no argument is specified.''')

parser.add_argument(
    '-destination', '-dest',
    type=str,
    help='''Directory path to a folder that extracted data files will be saved 
    to. May be absolute or relative. Defaults to the current working directory 
    if no argument is provided.''')

parser.add_argument(
    '-qtr',
    type=str,
    help='''Single financial quarter (ie: 2017q1) to be downloaded from sec.gov. 
    When used, qtr overrides -startqtr and -endqtr arguments if also used. Use 
    -qtr latest to download the latest available quarter.''')

parser.add_argument(
    '-startqtr', '-start',
    type=str,
    default='2009q1',
    help='''The starting financial quarter when downloading a range of zip 
    archives from sec.gov. Defaults to 2009q1, the earliest financial period 
    available.''')

parser.add_argument(
    '-endqtr', '-end',
    type=str,
    help='''The ending financial quarter when downloading a range of zip 
    archives from sec.gov. Defaults to the latest available quarter when no 
    argument is specified.''')

parser.add_argument(
    '-singledir', '-s',
    action='store_true',
    help='''By default zip archives are extracted to subdirectories that mirror 
    each individual archive. Use the -singledir switch to extract all data files 
    directly to -destination, appending filenames with the applicable financial 
    period.''')

parser.add_argument(
    '-rmzip', '-r',
    action='store_true',
    help='''By default zip archives will persist after extraction. Use the 
    -rmzip switch to remove each archive after extraction, as well as any 
    parent directory specified by -path (if empty) after extraction.''')

parser.add_argument(
    '-download', '-d',
    action='store_true',
    help='''Use the -download switch to download the specified zip archive(s) 
    without subsequent file extraction.''')

parser.add_argument(
    '-extract', '-e',
    action='store_true',
    help='''Use the -extract switch to extract the specified zip archive(s) (no 
    download).''')


