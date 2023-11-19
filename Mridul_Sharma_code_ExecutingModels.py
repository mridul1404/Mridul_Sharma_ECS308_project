import warnings
warnings.filterwarnings("ignore")

from ans import classification

clf=classification('/Users/mridu/PycharmProjects/Marketing Campaign/', clf_opt='knn',
                        no_of_selected_features=4)

clf.classification()