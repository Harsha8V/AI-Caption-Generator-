import pandas as pd

def get_hashtags(category):
    df = pd.read_csv("hashtags.csv")
    return df[df['category'] == category]['hashtag'].tolist()
