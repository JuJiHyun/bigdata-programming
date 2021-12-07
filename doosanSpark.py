import sys
import csv

from pyspark import SparkContext, SparkConf

# Encoding to UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')

# Create Spark Context
conf = SparkConf().setAppName("Doosan Bears Word Count")
sc = SparkContext(conf = conf)

# Create RDD and Split words
tokens = sc.textFile("hdfs:///user/maria_dev/doosanbears_11_filter.csv").flatMap(lambda line: line.split(" "))

# Count words
word_counts = tokens.map(lambda word: (word, 1)).reduceByKey(lambda v1, v2: v1 + v2)

# Collect counted words to keywords
keywords = word_counts.collect()

# Save keywords to CSV
fp = open("doosan_word_output_11.csv", "w")
writer = csv.writer(fp, dialect="excel")
writer.writerows(keywords)
fp.close()