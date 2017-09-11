import numpy as np
import cv2
import datetime


minSum=999999999;
maxSum=0;
frameNum=0;
cap = cv2.VideoCapture(0)
numStr="";
firstMatch=False;
prevSum=-1;
currBit=0;
def bin2num(str):
    num=int(str[3])*2*2*2+int(str[2])*2*2+int(str[1])*2+int(str[0]);
    return num;

startFlag=False;
while(True):
    start = datetime.datetime.now()

    ret, origMat = cap.read()
    ret, origMat = cap.read()
    
    blueMat=cv2.inRange(origMat, (128, 255-20, 128), (255, 255, 255));
    
    sum=np.sum(blueMat[0:480, 0:640])
    if(frameNum>5 and frameNum<10):
        if(minSum>sum):
            minSum=sum;
        if(maxSum<sum):
            maxSum=sum;
    elif(frameNum>10):
        
        sum=sum/(640*480)
        if(prevSum>0):
            if(sum-prevSum>0.5):
                numStr=numStr+'1';
                currBit=1;
            elif(prevSum-sum>0.5):
                numStr=numStr+'0';
                currBit=0;
            else:
                if(currBit==0):
                    numStr=numStr+'0';
                else:
                    numStr=numStr+'1';
        prevSum=sum;
        if(startFlag==False):            
            if(numStr[-3:]=='110'):
                print("prefix:"+str(numStr[-3:]));
                numStr="";
                startFlag=True;
        elif(len(numStr)==4 and startFlag==True):
            print("Binary", numStr[::-1]);
            print('Frame:'+str(frameNum));
            print('GetNum:'+str(bin2num(numStr)));
            numStr="";
            startFlag=False;
    frameNum=frameNum+1;    
    
    cv2.imshow("blueMat", blueMat);
    end = datetime.datetime.now()
    diff = end - start        
    delayDiff=int(diff.total_seconds() * 1000);

    if(delayDiff>200):
        cv2.waitKey(1);
    else:
        cv2.waitKey(200-delayDiff);