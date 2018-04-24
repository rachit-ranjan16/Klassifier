Parameters = {'Algorithm' : 'SVM'}
def TrainMyClassifer(XEstimate, XValidate, Parameters):
    (SVMY_Pred,RVMY_Pred,GPY_Pred,cvsvm.best_params_,cvrvm.best_params_,cvgpc.best_params_,
     SVMEstConfMat,RVMEstConfMat,GPEstConfMat,SVMConfMatrix,RVMConfMatrix,GPConfMatrix) = MyCrossValidate(XEstimate, XValidate, 5)
    print SVMY_Pred,RVMY_Pred,GPY_Pred,cvsvm.best_params_,cvrvm.best_params_,cvgpc.best_params_
