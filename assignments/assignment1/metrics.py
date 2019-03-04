def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, accuracy, f1 - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0
    
    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    
    accuracy = (prediction == ground_truth).mean()
    
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    
    for i in range(len(prediction)): 
        if ground_truth[i]==prediction[i]==True:
            TP += 1
        if prediction[i]==1 and ground_truth[i]!=prediction[i]:
            FP += 1
        if ground_truth[i]==prediction[i]==False:
            TN += 1
        if prediction[i]==0 and ground_truth[i]!=prediction[i]:
            FN += 1
    
    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    
    f1 = 2*precision*recall/(precision+recall)
    
    return accuracy, precision, recall, f1


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    accuracy = (prediction == ground_truth).mean()
    return accuracy
