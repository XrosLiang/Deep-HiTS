import numpy as np
import cPickle as pickle

model_filename = '/home/shared/RF_5000/RF_model.pkl'
test_set_filename = '/home/shared/RF_5000/RF_test_set.pkl'

with open(model_filename, 'rb') as fid:
    clf = pickle.load(fid)
data = np.load(test_set_filename)
x_test = data['features']
y_test = data['labels']

#model_pbbs = clf.predict_proba(x_test)[:,1]
model_class = clf.predict(x_test)

acc = np.equal(model_class, y_test).astype(np.float).mean()
print acc
