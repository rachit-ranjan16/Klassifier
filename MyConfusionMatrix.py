from sklearn import metrics
import numpy as np
confusion_matrix=metrics.confusion_matrix(Y,ClassNames)
overall_accuracy=metrics.accuracy_score(Y,ClassNames)
acc_each_class=metrics.precision_score(Y,ClassNames,average=None)
average_accuracy=np.mean(acc_each_class)
print('Confusion matrix: \n',confusion_matrix)
print('Average accuracy: \n',average_accuracy)

