
def encode_categories( df, column ):
    encoding = {}
    for idx, val in enumerate(df[column].unique()):
        encoding[val] = idx
    return df[column].map(encoding), encoding

def set_NaN(df, column, value):
    return df[column].fillna(value)

def get_mean(df, column):
    return df[column].mean()

def select( df, features ):
    return df[features]
