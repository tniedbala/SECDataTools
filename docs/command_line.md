## Command Line Reference

*SECDataTools/GetData* is meant to be run as a standalone script, specifying the following command line arguments:

```
$ python SECDataTools/GetData 	[-h] [-path PATH] [-destination DESTINATION] [-qtr QTR]
								[-startqtr STARTQTR] [-endqtr ENDQTR] [-singledir] [-rmzip]
								[-download] [-extract]
```

### Optional Arguments:

**-h, --help**         
Displays help message and exits.

**-path**          
Directory path that zip archives will be saved to. May be absolute or relative. Defaults to (creates) an *./sec_zip* subdirectory within the current working directory when no argument is specified.

**-destination, -dest**          
Directory path to a folder that extracted data files will be saved to. May be absolute or relative. Defaults to the current working directory if no argument is provided.

**-qtr**          
Single financial quarter (ie: `2017q1`) to be downloaded from sec.gov. When used, `qtr` overrides `-startqtr` and `-endqtr` arguments if also used. Use `-qtr latest` to download the latest available quarter.

**-startqtr, -start**          
The starting financial quarter when downloading a range of zip archives from sec.gov. Defaults to `2009q1`, the earliest financial period available.

**-endqtr, -end**          
The ending financial quarter when downloading a range of zip archives from sec.gov. Defaults to the latest available quarter when no argument is specified.

**-singledir, -s**          
By default zip archives are extracted to subdirectories that mirror each individual archive. Use the `-singledir` switch to extract all data files directly to `-destination`, appending filenames with the applicable financial period. See [Extract Options](extract_options.md) for additional detail.
 
**-rmzip, -r**          
By default zip archives will persist after extraction. Use the `-rmzip` switch to remove each archive after extraction, as well as any parent directory specified by `-path` (if empty) after extraction.

**-download, -d**          
Use the `-download` switch to download the specified zip archive(s) without subsequent file extraction.

**-extract, -e**          
Use the `-extract` switch to extract the specified zip archive(s) (no download).
<br><br>


## Examples

### Financial Periods:

1. Download all available financial periods to an ./sec_zip subdirectory in the current working directory, extracting archives to the cwd:
	```
    $ python SECDataTools/GetData
    ````

2. Download the zip archive for `2016q1` and extract to the cwd:
	```
    $ python SECDataTools/GetData -qtr 2016q1
    ````

3. Download the archive for the most recently available financial quarter:
	```
    $ python SECDataTools/GetData -qtr latest
    ```

4. Download all zip archives for periods `2016q1` through `2016q4`:
	```
    $ python SECDataTools/GetData -start 2016q1 -end 2016q1
    ```

### Directory/File Options:

1.	Download zip archives to a *./zip* subdirectory within the current working directory, extracting data files to a *./data* subdirectory in the cwd:
	```
    $ python SECDataTools/GetData -path zip -dest data
    ````
 
2. Download zip archives to the current working directory, extracting all data files directly to the cwd and removing zip archives after each extraction (see [Extract Options](extract_options.md) for additional detail):
	```
    $ python SECDataTools/GetData -path . -singledir -rmzip
    ````

3. Download zip archives to the current working directory (no extract):

	```
    $ python SECDataTools/GetData -path . -download
    ````
 
 4. Extract all zip archives from a *./zip* subdirectory within the cwd to an absolute path (no download):
	```
    $ python SECDataTools/GetData -path zip -dest /home/username/sec/data -extract
    ````
