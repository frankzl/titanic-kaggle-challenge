
def predict(model, test_data):
    return model.predict(test_data)

def train(model, train_data, labels):
    return model.train(train_data, labels)

def save( filename, header, data_ids, data_labels ):
    import pandas as pd
    submission = pd.DataFrame({header[0]: data_ids, header[1]: data_labels})
    submission.to_csv(filename, index=False)
    print("Saved file: " + filename)
