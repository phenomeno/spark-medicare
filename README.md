# spark-medicare
Analyzing Medicare data from CMS via Spark.

## Introduction
This is a short example for me to learn Spark while analyzing (recently)publicly available claims data for Medicare. It processes a list of HCPCS/CPT codes and their short descriptions in the order of total service line counts. The total sum of unique members (unique per each physician/provider) is also provided, as is a quick calculation to see the utilization of a particular code.

The use of Spark allows the manipulation of about 9 million rows in a short amount of time using the Spark variant of SQL. Adjust the SQL portion of the python file to generate different results for your purposes.

## How to run
Run the following command line to download the dependent data (CMS-provided Provider Utilization File from 2013).
```
$ ./download_data.sh
```

Then, run the following command line to submit the python file to the Spark cluster of your choice.
```
$ spark-submit --master (spark_cluster_url) --packages com.databricks:spark-csv_2.10:1.1.0 spark-medicare.py
```

For those who don't have a Spark cluster (like myself), use the following command line to run on all logical cores on your computer.
```
$ spark-submit --master local[*] --packages com.databricks:spark-csv_2.10:1.1.0 spark-medicare.py
```

The resulting file will be saved into `hcpcs.csv`. Watch the progress at `http://localhost:4040`.

If the resulting file is fragmentized as a directory, use the following command line to reassemble the result files.

```
$ (echo "HCPCS,DESC,LINE_SRVC_SUM,BENE_UNIQUE_SUM,UTILIZATION"; cat hcpcs.csv/part-*) > result.csv
```

## License

MIT License

Copyright (c) 2015 Grace Lee

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
