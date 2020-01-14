from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('RatingsHistogram')
sc = SparkContext(conf=conf)

lines = sc.textFile('../datasets/ml-100k/u.data')
ratings = lines.map(lambda x: x.split('\t')[2])
result = ratings.countByValue()

for k, v in sorted(result.items()):
    print(k, v)
