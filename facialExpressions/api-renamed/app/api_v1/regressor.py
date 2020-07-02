import json
import pandas as pd
import json
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, Normalizer, StandardScaler, MinMaxScaler
from pyspark.ml.regression import DecisionTreeRegressionModel
from pyspark.ml.evaluation import RegressionEvaluator


spark = SparkSession \
    .builder \
    .appName("regression out") \
    .config("spark.some.config.option", "") \
    .getOrCreate()
def fun(jsonObj):
    # j = json.loads(jsonStr)
    df = pd.json_normalize(jsonObj)
    df_sp = spark.createDataFrame(df)
    # vectorAssembler = VectorAssembler(inputCols = ['joy', 'fear', 'disgust', 'sadness', 'anger', 'surprise', 'contempt', 'valence', 'engagement', 'smile', 'innerBrowRaise', 'browRaise', 'browFurrow', 'noseWrinkle', 'upperLipRaise', 'lipCornerDepressor', 'chinRaise', 'lipPucker', 'lipPress', 'lipSuck', 'mouthOpen', 'smirk', 'eyeClosure', 'eyeWiden', 'cheekRaise', 'lidTighten', 'dimpler', 'lipStretch', 'jawDrop', 'relaxed', 'smiley', 'laughing', 'kissing', 'disappointed'], outputCol = 'features')
    vectorAssembler = VectorAssembler(inputCols = ['joy', 'fear', 'disgust', 'sadness', 'anger', 'surprise', 'contempt', 'valence', 'engagement', 'smile', 'innerBrowRaise', 'browRaise', 'browFurrow', 'noseWrinkle', 'upperLipRaise', 'lipCornerDepressor', 'chinRaise', 'lipPucker', 'lipPress', 'lipSuck', 'mouthOpen', 'smirk', 'eyeClosure', 'eyeWiden', 'cheekRaise', 'lidTighten', 'dimpler', 'lipStretch', 'jawDrop'], outputCol = 'features')
    vface_df = vectorAssembler.transform(df_sp)
    # vface_df.take(1)
    m = DecisionTreeRegressionModel.load('/Users/rt/iCloud Drive (Archive)/Documents/myPersonalProjects/gayan/decisionTreeModel1.pckl')
    dt_predictions1 = m.transform(vface_df)
    
    return dt_predictions1.select('prediction').describe().collect()[1]['prediction']