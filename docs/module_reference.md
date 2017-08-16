## Module Reference
 
*SECDataTools*.**latest_qtr()**

Returns string value indicating the latest available financial statement period available for download on sec.gov (ie: `'2017q1'`). This can be verified against available dataset posted at https://www.sec.gov/dera/data/financial-statement-data-sets.html.
<br><br>

*SECDataTools*.**download(**_qtr=None, startqtr='2009q1', endqtr=None, path=None_**)**

Download zip archive(s) from https://www.sec.gov/dera/data/financial-statement-data-sets.html. If no arguments are provided, all available financial statement zip archives will be downloaded to an *./sec_zip* subdirectory within the current working directory.

- **qtr:** string specifying a single financial quarter (ie: `'2017q1'`) to be downloaded from sec.gov. When used, `qtr` overrides `startqtr` and `endqtr` arguments if also used. Use `qtr='latest'` to download the latest available quarter.


- **startqtr:** string; the starting financial quarter when downloading a range of zip archives from sec.gov. Defaults to `'2009q1'`, the earliest financial period available.


- **endqtr:** string; the ending financial quarter when downloading a range of zip archives from sec.gov. Defaults to the latest available quarter when no argument is specified.


- **path:** string; directory path that zip archives will be saved to. May be absolute or relative. Defaults to (creates) an *./sec_zip* subdirectory within the current working directory when no argument is specified.
<br><br>

*SECDataTools*.**extract(**_path=None, destination=None, singledir=False, rmzip=False_**)**

Extract data files from financial statement zip archives. If no arguments are provided, `SECDataTools.extract()` will search the current working directory for an *./sec_zip* subdirectory and extract any zipfile contents to the cwd.


- **path:** string; path to a directory containing financial statement zip archives or path to an individual zip archive. May be absolute or relative. If no argument is provided an *./sec_zip* subdirectory must exist within the cwd.


- **destination:** string; directory path to a folder that extracted data files will be saved to. May be absolute or relative. Defaults to the current working directory if no argument is provided.


- **singledir:** boolean; by default zip archives are extracted to subdirectories that mirror each individual archive. When `singledir=True` individual files are extracted directly to `destination`, appending filenames with the applicable financial period. See [Extract Options](extract_options.md) for additional detail.


- **rmzip:** boolean; by default zip archives will persist after extraction. When `rmzip=True` zip archives will be removed after extraction, as well as any parent directory specified by `path` (if empty) after extraction.


## Examples

``` python
import SECDataTools as sec

# download all available datasets to the default ./sec_zip subdirectory
sec.download()

# download the latest available quarter to the default ./sec_zip subdirectory
sec.download('latest')

# download archives for 2016q1 - 2016q4 to a ./zip subdirectory
sec.download(startqtr='2016q1', endqtr='2016q4', path='zip')

# extract all archives in the default ./sec_zip subdirectory to the cwd
sec.extract()

# extract 2017q1.zip from a /zip directory to a /data directory
sec.extract(path='c:/zip/2017q1.zip', destination='c:/data')

# extract archives in the ./zip subdirectory to an ./extract subdirectory
# in the cwd, removing each zip archive after extraction
sec.extract(path='zip', destination='extract', rmzip=True)

# extract datafiles in ./zip directly to the cwd, appending filenames with financial quarters
sec.extract(path='zip', singledir=True)

```

