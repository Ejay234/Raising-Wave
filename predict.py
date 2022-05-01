import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('sealevel.csv')
# print(df.head())

all_feats = df[['GMSL_noGIA', 'StdDevGMSL_noGIA',
                'GMSL_GIA', 'StdDevGMSL_GIA']]
years = df['Year']

x_train, x_test, y_train, y_test = train_test_split(
    all_feats, years, test_size=0.2, random_state=1)

lr = LinearRegression()
lr.fit(x_train, y_train)


def helpMe(gmsl, sd_gmsl, gia, sd_gia):
    year = np.array([gmsl, sd_gmsl, gia, sd_gia]).reshape(1, -1)
    predict = lr.predict(year)
    return predict
#year_predict = lr.predict(x_test)

# gmsl = {}
# sd_gmsl = {}
# gia = {}
# sd_gia ={}


# User's input on the features
# By order, GMSL_noGIA, StdDevGMSL_noGIA, GMSL_GIA, StdDevGMSL_GIA
#year = np.array([gmsl, sd_gmsl, gia, sd_gia]).reshape(1, -1)
# lr.predict(year)
#pickle.dump(lr, open('model.pkl', 'wb'))
#model = pickle.load(open('model.pkl', 'rb'))
