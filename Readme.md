## SECDataTools


Simple Python utility that downloads and extracts financial statement zip archives made publicly available by the US Securities and Exchange Comission (SEC) at https://www.sec.gov/dera/data/financial-statement-data-sets.html. 

### Requirements

- Python version 3.3 or higher
- Modern version of Windows, Mac OS X, Linux


### Quick Start

*SECDataTools/GetData* may be run as a standalone script. With no arguments provided all available datasets are downloaded to an *./sec_zip* subdirectory within the current working directory, and then extracted to the cwd:

```
$ python SECDataTools/GetData
````
The same can be achieved from within a Python module as follows:

``` python
import SECDataTools as sec

sec.download()
sec.extract()
```

Additional command line and module functionality is available. See [documentation](/docs) for additional details.


### Documentation

1. [Command Line Reference](docs/command_line.md)
2. [Module Reference](docs/module_reference.md)
3. [Extract Options](docs/extract_options.md)


### Project Status

SECDataTools currently retrieves SEC financial statement datasets and is available for Python version 3.3 or higher. Expected updates include:

- Python 2.7 support
- Database tools and utilities
- Support for additional datasets available at https://www.sec.gov/data


### License

[MIT](/License)


### Disclaimer

This software has been created for informational/educational purposes only and is not intended for use in making investment decisions. I make absolutely no guarantees regarding the accuracy, reliability or completeness of information generated in connection with the software and place an added emphasis on all language found within the software's [License](License).