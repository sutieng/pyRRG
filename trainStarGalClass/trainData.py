'''
This script will train the data at the moment using a very simple
logisitic regression

'''

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import generateTrainingData as gt
import pickle as pkl

def trainData():

    trainingFeatures, trainingAnswers = \
      gt.generateTrainingData()

    print("Size of training data is %i with %i features" %\
              (trainingFeatures.shape[0], trainingFeatures.shape[1]))
    clf = SVC( )
    
    fitClassifier = clf.fit( trainingFeatures, trainingAnswers)
    
    pkl.dump(fitClassifier, open('starGalaxyModel.pkl','wb'))

    
