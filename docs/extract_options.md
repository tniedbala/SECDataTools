## Extract Options

### Default Behavior

By default data files are extracted to subdirectories in a format that mirrors each zip archive.

- Command Line:

	```
    $ python SECDataTools/GetData -start 2017q1 -end 2017q2
    ```
    
- File Output:

        .
        ├── 2017q1
        │   ├── num.txt
        │   ├── pre.txt
        │   ├── readme.htm
        │   ├── sub.txt
        │   └── tag.zip
        ├── 2017q2
        │   ├── num.txt
        │   ├── pre.txt
        │   ├── readme.htm
        │   ├── sub.txt
        │   └── tag.zip
        └── sec_zip
            ├── 2017q1.zip
            └── 2017q1.zip


### -singledir Argument

By including the `-singledir` switch (`singledir=True`), all zip archives are extracted with the financial period appended to the filename. Only a single *readme.htm* file is extracted and is prepended with an underscore to sort to the top of the directory:

- Command Line:

	```
    $ python SECDataTools/GetData -start 2017q1 -end 2017q2 -singledir
    ```

- File Output:

      .
      ├── sec_zip
      │   ├── 2017q1.zip
      │   └── 2017q1.zip
      ├── _readme.htm
      ├── num_2017q1.txt
      ├── num_2017q2.txt
      ├── pre_2017q1.txt
      ├── pre_2017q2.txt
      ├── sub_2017q1.txt
      ├── sub_2017q2.txt
      ├── tag_2017q1.txt
      └── tag_2017q2.txt

