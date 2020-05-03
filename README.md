<h3>This script is aimed at doing stratified split to images based on K-Fold<h3>

<ol>
  <li><pre>First, Preparing all your images into one folder.
The structure of the folder would be like ↓↓↓ 
   
   FolderA
        |
        |-----classA
        |       |-img1.jpg
        |       |-img2.jpg
        |       |-....
        |
        |
        |-----classB
        |       |-img1.jpg
        |       |-img2.jpg
        |       |-....
        |
        |-.....
  </pre>
  </li>
  <li>
  <pre>import KfoldSplit_Generator as kfg</pre>
  </li>
  <li>
  <pre>Call "write2Csv" function
This function needs 2 arguments "AllCsvName" and "AllImgDir"
<br>
csvName:
Name of a csv file which will be created after finishing the function.
The csv file has no index column and header, and includes 2 columns.
The first column includes all your images path, and the second column includes your the classes of the images.
<br>
imgDir:
The top folder including all your images.
Taking the first step for example, pass "FolderA" to an imgDir argument.
<br>
So, after finishing write2Csv function you'll get a csv file.
  </pre>
  </li>
  <li>
  <pre>Call "StratifiedSplitCsv" function
This function needs 3 arguments "csvfile", "crossValidationCount" and "KFoldCsvPath"
<br>
csvfile:
The name of the csv file created from step2.
<br>
crossValidationCount:
The number of K-Fold crossvalidation.
<br>
KFoldCsvPath:
If I set crossValidationCount as 10, you'll get 10 training csv files and 10 testing csv files after finishing this function.
KFoldCsvPath argument is the folder where those csv files will be saved.
Those csv files would be like ↓↓↓ 
   KFoldCsvPath
        |
        |-KFold_001_test.csv
        |-KFold_001_train.csv
        |-KFold_002_test.csv
        |-KFold_002_train.csv
        |
        |-....
<br> 
You can see each csv file includes stratified image names which are splited proportionally.
  </pre>
  </li>
  <li>
  <pre>Finally, call "moveKfoldFiles" function
This function needs 3 arguments "KFoldCsvFolder", "KFoldImgFolder" and "classList"
<br>
KFoldCsvFolder:
The same as KFoldCsvPath argument in step2.
<br>
classList:
The list including all your classes. ['classA','classB','classC'...]
You can get it by using ↓↓↓
classList = [name for name in os.listdir("The folder containing all your classes")]
<br>
KFoldImgFolder:
In the end, this function will copy all your images from the folder mentioned in step1 to KFoldImgFolder folder.
KFoldImgFolder is the name of the folder where all splitted images will be saved.
KFoldImgFolder would be like ↓↓↓ 
KFoldImgFolder
      |
      |----KFold001
      |        |
      |        |-----test
      |        |       |------classA
      |        |       |        |-img1.jpg
      |        |       |        |-img2.jpg
      |        |       |        |-...
      |        |       |
      |        |       |------classB
      |        |       |        |-img1.jpg
      |        |       |        |-img2.jpg
      |        |       |        |-...
      |        |
      |        |-----train
      |        |       |------classA
      |        |       |        |-img1.jpg
      |        |       |        |-img2.jpg
      |        |       |        |-...
      |        |       |
      |        |       |------classB
      |        |       |        |-img1.jpg
      |        |       |        |-img2.jpg
      |        |       |        |-...
      |        |
      |        |-.....
      |
      |
      |----KFold002
      |        |
      |        |-----test
      |        |       |------classA
      |        |       |        |-img1.jpg
      |        |       |        |-img2.jpg
      |        |       |        |-...
      |        |       |
      |        |       |------classB
      |        |       |        |-img1.jpg
      |        |       |        |-img2.jpg
      |        |       |        |-...
      |        |
      |        |-----train
      |        |       |------classA
      |        |       |        |-img1.jpg
      |        |       |        |-img2.jpg
      |        |       |        |-...
      |        |       |
      |        |       |------classB
      |        |       |        |-img1.jpg
      |        |       |        |-img2.jpg
      |        |       |        |-...
      |        |
      |        |-.....
      <br>
  </pre>
  </li>
</ol>

<h2>Notice<h2>
  <pre>StratifiedSplitCsv function will print "Training Data Len:" and Test Data Len:".
  "Test Data Len" would decrease continously.
  The reason might be rounding when doing stratified split.
  I use numpy.array_split to split data.</pre>


