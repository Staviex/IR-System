import math

def tf_idf(tf, df, n):
    return tf * math.log(n / df)
