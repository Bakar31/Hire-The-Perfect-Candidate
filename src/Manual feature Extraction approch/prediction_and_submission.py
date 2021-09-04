import pandas as pd
from model import rf, test_df

def submission(model, test_sentences):
    test1 = pd.read_csv('dataset/test.csv')
    preds = model.predict(test_sentences)
    prediction = pd.DataFrame(preds, columns = ['Match Percentage'])
    sub_df = pd.concat([test1, prediction], axis = 1)
    return sub_df

sub = submission(rf, test_df)
sub.to_csv('submission file/Submission-4.csv')
print(sub.head())