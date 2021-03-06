import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle

from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score

def plot_pr_curve(Y,P,classes, save=None):
    # setup plot details
    colors = cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'b'])
    lw = 2

    # Binarize the output
    n_classes = np.shape(Y)[1]

    # Compute Precision-Recall and plot curve
    precision = dict()
    recall = dict()
    average_precision = dict()

    for c in range(n_classes):
        precision[c], recall[c], _ = precision_recall_curve(Y[:, c],
                                                            P[:, c])
        average_precision[c] = average_precision_score(Y[:, c], P[:, c])

    # Compute weighted-average ROC curve and ROC area
    precision["weighted"], recall["weighted"], _ = precision_recall_curve(Y.ravel(),
        P.ravel())
    average_precision["weighted"] = average_precision_score(Y, P, average="weighted")


    # # Plot Precision-Recall curve
    # plt.clf()
    # plt.plot(recall[0], precision[0], lw=lw, color='navy',
    #          label='Precision-Recall curve')
    # plt.xlabel('Recall')
    # plt.ylabel('Precision')
    # plt.ylim([0.0, 1.05])
    # plt.xlim([0.0, 1.0])
    # plt.title('Precision-Recall example: AUC={0:0.2f}'.format(average_precision[0]))
    # plt.legend(loc="lower left")
    # plt.show()

    # Plot Precision-Recall curve for each class
    plt.clf()
    # plt.plot(recall["micro"], precision["micro"], color='gold', lw=lw,
    #          label='micro-average Precision-recall curve (area = {0:0.2f})'
    #                ''.format(average_precision["micro"]))
    # plt.plot(recall["weighted"], precision["weighted"], color='gold', lw=lw,
    #          label='weighted-average Precision-recall curve (area = {0:0.2f})'
    #                ''.format(average_precision["weighted"]))
    for i, color in zip(range(n_classes), colors):
        plt.plot(recall[i], precision[i], color=color, lw=lw,
                 label="%s (AP/AUC: %0.4f)" % (classes[i], average_precision[i]))

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Extension of Precision-Recall curve to multi-class')
    plt.legend(loc="lower left")
    if save is not None:
        plt.savefig(save, dpi=300, facecolor='w', edgecolor='w', orientation='portrait', pad_inches=0.1)
    plt.show()
