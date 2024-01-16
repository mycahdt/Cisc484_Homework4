import sys
import matplotlib.pyplot as pl

try:
	DATASET = sys.argv[1]
	PREDICT = sys.argv[2]
except:
	print("Error! Use the command: python plot.py [Test_set] [prediction_file]")
################################################################################

# Read dataset and return 3 lists corresponding to classification, x and y
def opendataset(dataset):
    
    fid = open(dataset,'r')
    
    c = []
    x = []
    y = []
    
    for line in fid:
        c.append(float(line.split()[0]))
        x.append(float(line.split()[1]))
        y.append(float(line.split()[2]))

    fid.close()

    return c,x,y

# Read predict output 
def openpredict(predictfile):

    fid = open(predictfile,'r')

    predict = []

    for line in fid:
        predict.append(float(line))

    return predict

# Show plot
def showplot(c,x,y,predict):

    x_tp, x_tn, y_tp, y_tn = [],[],[],[]
    x_fp, x_fn, y_fp, y_fn = [],[],[],[]
    
    # Confusion matrix
    for i in range(len(c)):
        if c[i] > 0 and predict[i] > 0:
            x_tp.append(x[i])
            y_tp.append(y[i])
        elif c[i] < 0 and predict[i] < 0:
            x_tn.append(x[i])
            y_tn.append(y[i])
        elif c[i] < 0 and predict[i] > 0:
            x_fp.append(x[i])
            y_fp.append(y[i])
        elif c[i] > 0 and predict[i] < 0:
            x_fn.append(x[i])
            y_fn.append(y[i])
        else:
            print('Error! Check your predict file!')

    p_tp, = pl.plot(x_tp,y_tp,'ro') # True positive -> Red dot
    p_tn, = pl.plot(x_tn,y_tn,'bo') # True negative -> Blue dot
    p_fp, = pl.plot(x_fp,y_fp,'g^') # False positive -> Green triangle
    p_fn, = pl.plot(x_fn,y_fn,'ms') # False negative -> magenta square

    pl.legend([p_tp, p_tn, p_fp, p_fn],
              ['True Positive', 'True Negative','False Positive','False Negative'],
              loc = 3,
              ncol = 2,
              mode = 'expand',
              numpoints=1,
              borderaxespad=0.,
              bbox_to_anchor=(0., 1.01, 1., .102))

    
    pl.show()
    
    return None

def main():
    c,x,y = opendataset(DATASET)
    p = openpredict(PREDICT)
    showplot(c,x,y,p)

main()
            







