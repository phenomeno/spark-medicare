from pyspark import SparkContext
from pyspark.sql import SQLContext

if __name__ == '__main__':
	sc = SparkContext(appName='SparkMedicare')
	sqlContext = SQLContext(sc)

	df1 = sqlContext.read.format('com.databricks.spark.csv').options(header='true', delimiter="\t").load('puf.csv')
	df1.registerTempTable('puf')

	df2 = sqlContext.read.format('com.databricks.spark.csv').options(header='true', delimiter=",").load('cpt.csv')
	df2.registerTempTable('cpt')

	sqlContext.sql('SELECT a.HCPCS_CODE, b.DESCRIPTION, SUM(a.LINE_SRVC_CNT) AS LINE_SRVC_SUM, SUM(a.BENE_UNIQUE_CNT) AS BENE_UNIQUE_SUM, SUM(a.LINE_SRVC_CNT)/SUM(a.BENE_UNIQUE_CNT) FROM puf a INNER JOIN cpt b ON a.HCPCS_CODE = b.HCPCS GROUP BY a.HCPCS_CODE, b.DESCRIPTION ORDER BY LINE_SRVC_SUM DESC').write.format('com.databricks.spark.csv').save('hcpcs.csv')

	print "Result is saved at hcpcs.csv."
