import os
import csv
import pandas as pd
import numpy as np
from shutil import copyfile,rmtree



def write2Csv(AllCsvName,AllImgDir):


    with open(AllCsvName,'w',newline='') as csvfile:

        for root, _, files in os.walk(AllImgDir):
            for file in files:
                className = root.split("\\")[-1]
                filePath = os.path.join(root,file)
                writer = csv.writer(csvfile)
                writer.writerow([filePath, className])
                print("Writing ...",filePath,"  ",className)


def StratifiedSplitCsv(csvfile, crossValidationCount, KFoldCsvPath):

    if os.path.exists(KFoldCsvPath):
        rmtree(KFoldCsvPath)
        os.makedirs(KFoldCsvPath)
    else:
        os.makedirs(KFoldCsvPath)

    data = pd.read_csv(csvfile, header=None)

    data = data.astype('str')
    g_data = data.groupby(1)


    groupValues = list(g_data.size().index)

    for i in range(crossValidationCount):
        trainDf = pd.DataFrame()
        testDf = pd.DataFrame()
        print("*" * 150)

        print("Cross", i+1 )

        for gv in groupValues:
            df = g_data.get_group(gv)

            gv_split_list = np.array_split(df, crossValidationCount)
            testDf = pd.concat([testDf,gv_split_list[i]])
            del gv_split_list[i]
            gvdf = pd.concat(gv_split_list)
            trainDf = pd.concat([trainDf, gvdf])

        print("Training Data Len:", trainDf.shape[0])
        print("Test Data Len:",testDf.shape[0])

        print("Saving Training csv (fold"+str(i+1)+") to",os.path.join(KFoldCsvPath, "KFold_{0:03d}_train.csv".format(i + 1)))
        print("Saving Test csv (fold" + str(i + 1) + ") to",os.path.join(KFoldCsvPath, "KFold_{0:03d}_test.csv".format(i + 1)))

        trainDf.to_csv(os.path.join(KFoldCsvPath, "KFold_{0:03d}_train.csv".format(i + 1)), header=None)
        testDf.to_csv(os.path.join(KFoldCsvPath, "KFold_{0:03d}_test.csv".format(i + 1)), header=None)

        print("*" * 150)
        print()


def moveKfoldFiles(KFoldCsvFolder, KFoldImgFolder, classList):

    if os.path.exists(KFoldImgFolder):
        rmtree(KFoldImgFolder)
        os.makedirs(KFoldImgFolder)
    else:
        os.makedirs(KFoldImgFolder)


    for root, _, files in sorted(os.walk(KFoldCsvFolder)):

        for file in files:

            foldCount = file.split("_")[-2]

            for cl in classList:

                if not os.path.exists(os.path.join(KFoldImgFolder,"KFold"+foldCount,"train",cl)):
                    os.makedirs(os.path.join(KFoldImgFolder,"KFold"+foldCount,"train",cl))

                if not os.path.exists(os.path.join(KFoldImgFolder,"KFold"+foldCount,"test",cl)):
                    os.makedirs(os.path.join(KFoldImgFolder,"KFold"+foldCount,"test",cl))


            trainOrTest = file.split("_")[-1].split(".")[0]

            print("Reading...",os.path.join(root,file))

            df = pd.read_csv(os.path.join(root,file),header=None,index_col=0)

            for path, clnm in zip(df.iloc[:, 0], df.iloc[:, 1]):

                newpath = os.path.join(KFoldImgFolder,"KFold"+foldCount,trainOrTest,str(clnm),path.split("\\")[-1])


                print("Moving",path,"to",newpath)
                copyfile(path,newpath)







