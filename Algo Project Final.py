import tkinter as tk
from tkinter import * 
from tkinter import messagebox
  
  
root = tk.Tk()
root.geometry("700x500")
root.configure(background = "#85144B") 


#Header (DAA)
header = tk.Frame(root)
header.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)

def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0):
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)
canvas=Canvas(header,bg='#85144B', borderwidth = 0)
canvas.pack(fill=BOTH, expand=1)
text_var="DESIGN AND ANALYSIS OF ALGORITHMS"
text=canvas.create_text(0,-2000,text=text_var,font=('merriweather',16,'bold'),fill='#FF851B',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = x2-x1
height = y2-y1
canvas['width']=width
canvas['height']=height
fps=60 
shift()



#Final Project 
header2 = tk.Frame(root)
header2.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.2)
header2.config(bg = "#85144B")

header2label = tk.Label(header2,  text ='FINAL PROJECT', height = 3, width = 35, bg = "#85144B", borderwidth = 0)
header2label.place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 1)
header2label.config(font =("palantio 25 bold"), fg = "#FF851B")




#middle Container

middle = tk.Frame(root, bg='#85144B')
middle.place(relx = 0, rely = 0.4, relwidth = 1)

OPTIONS1 = [
"Longest Common Subsequence",
"Shortest Common SuperSequence",
"Levenshtien Distance",
"Longest Increasing Subsequence",
"Matrix Chain Multiplication",
"0-1 Knapsack",
"Partition Problem",
"Rod Cutting Problem",
"Coin Change Making Problem",
"Word Break Problem"
] 


variable1 = StringVar(middle)
variable1.set(OPTIONS1[0]) # default value

w1 = OptionMenu(middle, variable1, *OPTIONS1)
w1.config(bg = "#ffece5", font =("TISA 12 bold"), fg = "#3c2f2f")
w1.place()
w1.pack(pady = 10)




OPTIONS = [
"DataSet1",
"DataSet2",
"DataSet3",
"DataSet4",
"DataSet5",
"DataSet6",
"DataSet7",
"DataSet8",
"DataSet9",
"DataSet10"
] 


variable = StringVar(middle)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(middle, variable, *OPTIONS)
w.config(bg = "#ffece5", font =("TISA 12 bold"), fg = "#3c2f2f")
w.pack(pady = 2)

def ok():
    print ("\nvalue of Program: " + variable1.get())
    print ("\nValue of DataSet: " + variable.get())
    program=variable1.get()
    dataset=variable.get()
    if(program=="Longest Common Subsequence"):
        if(dataset=="DataSet1"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[0]
            Y=data[1]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of LCS is ", lcs(X, Y))

        elif(dataset=="DataSet2"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[2]
            Y=data[3]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of LCS is ", lcs(X, Y))

        elif(dataset=="DataSet3"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[4]
            Y=data[5]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of LCS is ", lcs(X, Y))

        elif(dataset=="DataSet4"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[6]
            Y=data[7]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of LCS is ", lcs(X, Y))

        elif(dataset=="DataSet5"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[8]
            Y=data[9]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of LCS is ", lcs(X, Y))

        elif(dataset=="DataSet6"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[10]
            Y=data[11]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of LCS is ", lcs(X, Y))

        elif(dataset=="DataSet7"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[12]
            Y=data[13]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of LCS is ", lcs(X, Y))

        elif(dataset=="DataSet8"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[14]
            Y=data[15]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of LCS is ", lcs(X, Y))

        elif(dataset=="DataSet9"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[16]
            Y=data[17]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of LCS is ", lcs(X, Y))

        elif(dataset=="DataSet10"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[18]
            Y=data[19]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of LCS is ", lcs(X, Y))
    
    elif(program=="Shortest Common SuperSequence"):
        if(dataset=="DataSet1"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[0]
            Y=data[1]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))


        elif(dataset=="DataSet2"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[2]
            Y=data[3]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))


        elif(dataset=="DataSet3"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[4]
            Y=data[5]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))


        elif(dataset=="DataSet4"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[6]
            Y=data[7]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))


        elif(dataset=="DataSet5"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[8]
            Y=data[9]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))


        elif(dataset=="DataSet6"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[10]
            Y=data[11]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))


        elif(dataset=="DataSet7"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[12]
            Y=data[13]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))


        elif(dataset=="DataSet8"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[14]
            Y=data[15]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))


        elif(dataset=="DataSet9"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[16]
            Y=data[17]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))


        elif(dataset=="DataSet10"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[18]
            Y=data[19]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))

    elif(program=="Levenshtien Distance"):
        if(dataset=="DataSet1"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[0]
            Y=data[1]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("The distamce is " + editDistDP(X,Y,len(X),len(Y)))


        elif(dataset=="DataSet2"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[2]
            Y=data[3]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("The distamce is " + editDistDP(X,Y,len(X),len(Y)))


        elif(dataset=="DataSet3"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[4]
            Y=data[5]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("The distamce is " + editDistDP(X,Y,len(X),len(Y)))


        elif(dataset=="DataSet4"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[6]
            Y=data[7]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("The distamce is " + editDistDP(X,Y,len(X),len(Y)))


        elif(dataset=="DataSet5"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[8]
            Y=data[9]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("The distamce is " + editDistDP(X,Y,len(X),len(Y)))


        elif(dataset=="DataSet6"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[10]
            Y=data[11]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("The distamce is " + editDistDP(X,Y,len(X),len(Y)))


        elif(dataset=="DataSet7"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[12]
            Y=data[13]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("The distamce is " + editDistDP(X,Y,len(X),len(Y)))


        elif(dataset=="DataSet8"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[14]
            Y=data[15]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("The distamce is " + editDistDP(X,Y,len(X),len(Y)))


        elif(dataset=="DataSet9"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[16]
            Y=data[17]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("The distamce is " + editDistDP(X,Y,len(X),len(Y)))


        elif(dataset=="DataSet10"):
            with open("InputABC.txt", "r") as file: 
                data = file.readlines()
            X=data[18]
            Y=data[19]
            print("Input dataset is: \n")
            print(X)
            print(Y)
            print("The distamce is " + editDistDP(X,Y,len(X),len(Y)))

    elif(program=="Longest Increasing Subsequence"):
        if(dataset=="DataSet1"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[0].split(',')
            print(arr)
            print("Length of lIS is", lis(arr))

        elif(dataset=="DataSet2"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[1].split(',')
            print(arr)
            print("Length of lIS is", lis(arr))

        elif(dataset=="DataSet3"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[2].split(',')
            print(arr)
            print("Length of lIS is", lis(arr))

        elif(dataset=="DataSet4"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[3].split(',')
            print(arr)
            print("Length of lIS is", lis(arr))

        elif(dataset=="DataSet5"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[4].split(',')
            print(arr)
            print("Length of lIS is", lis(arr))

        elif(dataset=="DataSet6"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[5].split(',')
            print(arr)
            print("Length of lIS is", lis(arr))

        elif(dataset=="DataSet7"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[6].split(',')
            print(arr)
            print("Length of lIS is", lis(arr))

        elif(dataset=="DataSet8"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[7].split(',')
            print(arr)
            print("Length of lIS is", lis(arr))

        elif(dataset=="DataSet9"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[8].split(',')
            print(arr)
            print("Length of lIS is", lis(arr))

        elif(dataset=="DataSet10"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[9].split(',')
            print(arr)
            print("Length of lIS is", lis(arr))

    
    elif(program=="Matrix Chain Multiplication"):
        if(dataset=="DataSet1"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[0].split(',')
            print(arr)
            size = len(arr) 
            print("Minimum number of multiplications is " + MatrixChainOrder(arr, size))

        elif(dataset=="DataSet2"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[1].split(',')
            print(arr)
            size = len(arr) 
            print("Minimum number of multiplications is " + MatrixChainOrder(arr, size))

        elif(dataset=="DataSet3"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[2].split(',')
            print(arr)
            size = len(arr) 
            print("Minimum number of multiplications is " + MatrixChainOrder(arr, size))

        elif(dataset=="DataSet4"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[3].split(',')
            print(arr)
            size = len(arr) 
            print("Minimum number of multiplications is " + MatrixChainOrder(arr, size))

        elif(dataset=="DataSet5"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[4].split(',')
            print(arr)
            size = len(arr) 
            print("Minimum number of multiplications is " + MatrixChainOrder(arr, size))

        elif(dataset=="DataSet6"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[5].split(',')
            print(arr)
            size = len(arr) 
            print("Minimum number of multiplications is " + MatrixChainOrder(arr, size))

        elif(dataset=="DataSet7"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[6].split(',')
            print(arr)
            size = len(arr) 
            print("Minimum number of multiplications is " + MatrixChainOrder(arr, size))

        elif(dataset=="DataSet8"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[7].split(',')
            print(arr)
            size = len(arr) 
            print("Minimum number of multiplications is " + MatrixChainOrder(arr, size))

        elif(dataset=="DataSet9"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[8].split(',')
            print(arr)
            size = len(arr) 
            print("Minimum number of multiplications is " + MatrixChainOrder(arr, size))

        elif(dataset=="DataSet10"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[9].split(',')
            print(arr)
            size = len(arr) 
            print("Minimum number of multiplications is " + MatrixChainOrder(arr, size))


    elif(program=="0-1 Knapsack"):
        if(dataset=="DataSet1"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            val=data[0].split(',')
            wt=data[1].split(',')
            W = 125
            n = len(val)
            print("Input dataset is: \n")
            print(val)
            print(wt)
            print(knapSack(W, wt, val, n))

        elif(dataset=="DataSet2"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            val=data[2].split(',')
            wt=data[3].split(',')
            W = 125
            n = len(val)
            print("Input dataset is: \n")
            print(val)
            print(wt)
            print(knapSack(W, wt, val, n))

        elif(dataset=="DataSet3"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            val=data[4].split(',')
            wt=data[5].split(',')
            W = 125
            n = len(val)
            print("Input dataset is: \n")
            print(val)
            print(wt)
            print(knapSack(W, wt, val, n))

        elif(dataset=="DataSet4"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            val=data[6].split(',')
            wt=data[7].split(',')
            W = 125
            n = len(val)
            print("Input dataset is: \n")
            print(val)
            print(wt)
            print(knapSack(W, wt, val, n))

        elif(dataset=="DataSet5"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            val=data[8].split(',')
            wt=data[9].split(',')
            W = 125
            n = len(val)
            print("Input dataset is: \n")
            print(val)
            print(wt)
            print(knapSack(W, wt, val, n))

        elif(dataset=="DataSet6"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            val=data[10].split(',')
            wt=data[11].split(',')
            W = 125
            n = len(val)
            print("Input dataset is: \n")
            print(val)
            print(wt)
            print(knapSack(W, wt, val, n))

        elif(dataset=="DataSet7"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            val=data[12].split(',')
            wt=data[13].split(',')
            W = 125
            n = len(val)
            print("Input dataset is: \n")
            print(val)
            print(wt)
            print(knapSack(W, wt, val, n))

        elif(dataset=="DataSet8"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            val=data[14].split(',')
            wt=data[15].split(',')
            W = 125
            n = len(val)
            print("Input dataset is: \n")
            print(val)
            print(wt)
            print(knapSack(W, wt, val, n))

        elif(dataset=="DataSet9"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            val=data[16].split(',')
            wt=data[17].split(',')
            W = 125
            n = len(val)
            print("Input dataset is: \n")
            print(val)
            print(wt)
            print(knapSack(W, wt, val, n))

        elif(dataset=="DataSet10"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            val=data[18].split(' ')
            wt=data[19].split(' ')
            W = 125
            n = len(val)
            print("Input dataset is: \n")
            print(val)
            print(wt)
            print(knapSack(W, wt, val, n))

    elif(program=="Partition Problem"):
        if(dataset=="DataSet1"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[0].split(',')
            print(arr)
            n = len(arr)
            if findPartition(arr, n) == True:
                print("Can be divided into two","subsets of equal sum")
            else:
                print("Can not be divided into ","two subsets of equal sum")

        elif(dataset=="DataSet2"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[1].split(',')
            print(arr)
            n = len(arr)
            if findPartition(arr, n) == True:
                print("Can be divided into two","subsets of equal sum")
            else:
                print("Can not be divided into ","two subsets of equal sum")

        elif(dataset=="DataSet3"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[2].split(',')
            print(arr)
            n = len(arr)
            if findPartition(arr, n) == True:
                print("Can be divided into two","subsets of equal sum")
            else:
                print("Can not be divided into ","two subsets of equal sum")


        elif(dataset=="DataSet4"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[3].split(',')
            print(arr)
            n = len(arr)
            if findPartition(arr, n) == True:
                print("Can be divided into two","subsets of equal sum")
            else:
                print("Can not be divided into ","two subsets of equal sum")

        elif(dataset=="DataSet5"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[4].split(',')
            print(arr)
            n = len(arr)
            if findPartition(arr, n) == True:
                print("Can be divided into two","subsets of equal sum")
            else:
                print("Can not be divided into ","two subsets of equal sum")

        elif(dataset=="DataSet6"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[5].split(',')
            print(arr)
            n = len(arr)
            if findPartition(arr, n) == True:
                print("Can be divided into two","subsets of equal sum")
            else:
                print("Can not be divided into ","two subsets of equal sum")

        elif(dataset=="DataSet7"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[6].split(',')
            print(arr)
            n = len(arr)
            if findPartition(arr, n) == True:
                print("Can be divided into two","subsets of equal sum")
            else:
                print("Can not be divided into ","two subsets of equal sum")

        elif(dataset=="DataSet8"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[7].split(',')
            print(arr)
            n = len(arr)
            if findPartition(arr, n) == True:
                print("Can be divided into two","subsets of equal sum")
            else:
                print("Can not be divided into ","two subsets of equal sum")

        elif(dataset=="DataSet9"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[8].split(',')
            print(arr)
            n = len(arr)
            if findPartition(arr, n) == True:
                print("Can be divided into two","subsets of equal sum")
            else:
                print("Can not be divided into ","two subsets of equal sum")

        elif(dataset=="DataSet10"):
            with open("InputDEGI.txt", "r") as file: 
                data = file.readlines() 

            arr = data[9].split(',')
            print(arr)
            n = len(arr)
            if findPartition(arr, n) == True:
                print("Can be divided into two","subsets of equal sum")
            else:
                print("Can not be divided into ","two subsets of equal sum")


    elif(program=="Rod Cutting Problem"):
        if(dataset=="DataSet1"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            arr=data[0].split(',')
            print(arr)
            size = len(arr) 
            print("Maximum Obtainable Value is: " + cutRod(arr, size))
    
        elif(dataset=="DataSet2"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            arr=data[1].split(',')
            print(arr)
            size = len(arr) 
            print("Maximum Obtainable Value is " + cutRod(arr, size))
    
        elif(dataset=="DataSet3"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            arr=data[2].split(',')
            print(arr)
            size = len(arr) 
            print("Maximum Obtainable Value is " + cutRod(arr, size))
    
        elif(dataset=="DataSet4"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            arr=data[3].split(',')
            print(arr)
            size = len(arr) 
            print("Maximum Obtainable Value is " + cutRod(arr, size))
    
        elif(dataset=="DataSet5"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            arr=data[4].split(',')
            print(arr)
            size = len(arr) 
            print("Maximum Obtainable Value is " + cutRod(arr, size))
    
        elif(dataset=="DataSet6"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            arr=data[16].split(',')
            print(arr)
            size = len(arr) 
            print("Maximum Obtainable Value is " + cutRod(arr, size))
    
        elif(dataset=="DataSet7"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            arr=data[6].split(',')
            print(arr)
            size = len(arr) 
            print("Maximum Obtainable Value is " + cutRod(arr, size))
    
        elif(dataset=="DataSet8"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            arr=data[12].split(',')
            print(arr)
            size = len(arr) 
            print("Maximum Obtainable Value is " + cutRod(arr, size))
    
        elif(dataset=="DataSet9"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()

            arr=data[8].split(',')
            print(arr)
            size = len(arr) 
            print("Maximum Obtainable Value is " + cutRod(arr, size))
    
        elif(dataset=="DataSet10"):
            with open("InputFH.txt", "r") as file: 
                data = file.readlines()
            arr=data[14].split(',')
            print(arr)
            size = len(arr) 
            print("Maximum Obtainable Value is " + cutRod(arr, size))

    elif(program=="Coin Change Making Problem"):
        if(dataset=="DataSet1"):
            with open("InputDEGI.txt", "r") as file:
                data = file.readlines()
            S = data[0].split(',')
            N = 125
            print(S)
            print(N)
            coins = findMinCoins(S, N)
            if coins != float('inf'):
                print("\nMinimum number of coins required to get desired change is", coins)

        elif(dataset=="DataSet2"):
            with open("InputDEGI.txt", "r") as file:
                data = file.readlines()
            S = data[1].split(',')
            N = 125
            print(S)
            print(N)
            coins = findMinCoins(S, N)
            if coins != float('inf'):
                print("\nMinimum number of coins required to get desired change is", coins)


        elif(dataset=="DataSet3"):
            with open("InputDEGI.txt", "r") as file:
                data = file.readlines()
            S = data[2].split(',')
            N = 125
            print(S)
            print(N)
            coins = findMinCoins(S, N)
            if coins != float('inf'):
                print("\nMinimum number of coins required to get desired change is", coins)


        elif(dataset=="DataSet4"):
            with open("InputDEGI.txt", "r") as file:
                data = file.readlines()
            S = data[3].split(',')
            N = 125
            print(S)
            print(N)
            coins = findMinCoins(S, N)
            if coins != float('inf'):
                print("\nMinimum number of coins required to get desired change is", coins)


        elif(dataset=="DataSet5"):
            with open("InputDEGI.txt", "r") as file:
                data = file.readlines()
            S = data[4].split(',')
            N = 125
            print(S)
            print(N)
            coins = findMinCoins(S, N)
            if coins != float('inf'):
                print("\nMinimum number of coins required to get desired change is", coins)


        elif(dataset=="DataSet6"):
            with open("InputDEGI.txt", "r") as file:
                data = file.readlines()
            S = data[5].split(',')
            N = 125
            print(S)
            print(N)
            coins = findMinCoins(S, N)
            if coins != float('inf'):
                print("\nMinimum number of coins required to get desired change is", coins)

        elif(dataset=="DataSet7"):
            with open("InputDEGI.txt", "r") as file:
                data = file.readlines()
            S = data[6].split(',')
            N = 125
            print(S)
            print(N)
            coins = findMinCoins(S, N)
            if coins != float('inf'):
                print("\nMinimum number of coins required to get desired change is", coins)


        elif(dataset=="DataSet8"):
            with open("InputDEGI.txt", "r") as file:
                data = file.readlines()
            S = data[7].split(',')
            N = 125
            print(S)
            print(N)
            coins = findMinCoins(S, N)
            if coins != float('inf'):
                print("\nMinimum number of coins required to get desired change is", coins)


        elif(dataset=="DataSet9"):
            with open("InputDEGI.txt", "r") as file:
                data = file.readlines()
            S = data[8].split(',')
            N = 125
            print(S)
            print(N)
            coins = findMinCoins(S, N)
            if coins != float('inf'):
                print("\nMinimum number of coins required to get desired change is", coins)

        elif(dataset=="DataSet10"):
            with open("InputDEGI.txt", "r") as file:
                data = file.readlines()
            S = data[9].split(',')
            N = 125
            print(S)
            print(N)
            coins = findMinCoins(S, N)
            if coins != float('inf'):
                print("\nMinimum number of coins required to get desired change is", coins)


    elif(program=="Word Break Problem"):
        if(dataset=="DataSet1"):
            dict = []
            print("Input data set is:\n")
            with open("InputJ.txt", "r") as f:
                for line in f:
                    dict.extend(line.split())
                    print(line)
            # input String
            str = "umaimasohail"

            if wordBreak(dict, str):
                wordBreak1(dict, str, "")
            else:
                print("\nString can't be segmented")

        elif(dataset=="DataSet2"):
            dict = []
            print("Input data set is:\n")
            with open("InputJ2.txt", "r") as f:
                for line in f:
                    dict.extend(line.split())
                    print(line)
            # input String
            str = "ajaykumar"

            if wordBreak(dict, str):
                wordBreak1(dict, str, "")
            else:
                print("\nString can't be segmented")

        if(dataset=="DataSet3"):
            dict = []
            print("Input data set is:\n")
            with open("InputJ3.txt", "r") as f:
                for line in f:
                    dict.extend(line.split())
                    print(line)
            # input String
            str = "umaimasohail"

            if wordBreak(dict, str):
                wordBreak1(dict, str, "")
            else:
                print("\nString can't be segmented")

        elif(dataset=="DataSet4"):
            dict = []
            print("Input data set is:\n")
            with open("InputJ4.txt", "r") as f:
                for line in f:
                    dict.extend(line.split())
                    print(line)
            # input String
            str = "umaimasohail"

            if wordBreak(dict, str):
                wordBreak1(dict, str, "")
            else:
                print("\nString can't be segmented")

        elif(dataset=="DataSet5"):
            dict = []
            print("Input data set is:\n")
            with open("InputJ5.txt", "r") as f:
                for line in f:
                    dict.extend(line.split())
                    print(line)
            # input String
            str = "ajaykumar"

            if wordBreak(dict, str):
                wordBreak1(dict, str, "")
            else:
                print("\nString can't be segmented")

        elif(dataset=="DataSet6"):
            dict = []
            print("Input data set is:\n")
            with open("InputJ6.txt", "r") as f:
                for line in f:
                    dict.extend(line.split())
                    print(line)
            # input String
            str = "umaimasohail"

            if wordBreak(dict, str):
                wordBreak1(dict, str, "")
            else:
                print("\nString can't be segmented")

        elif(dataset=="DataSet7"):
            dict = []
            print("Input data set is:\n")
            with open("InputJ7.txt", "r") as f:
                for line in f:
                    dict.extend(line.split())
                    print(line)
            # input String
            str = "ajaykumar"

            if wordBreak(dict, str):
                wordBreak1(dict, str, "")
            else:
                print("\nString can't be segmented")

        elif(dataset=="DataSet8"):
            dict = []
            print("Input data set for is:\n")
            with open("InputJ8.txt", "r") as f:
                for line in f:
                    dict.extend(line.split())
                    print(line)
            # input String
            str = "umaimasohail"
            if wordBreak(dict, str):
                wordBreak1(dict, str, "")
            else:
                print("\nString can't be segmented")

        elif(dataset=="DataSet9"):
            dict = []
            print("Input data set is:\n")
            with open("InputJ9.txt", "r") as f:
                for line in f:
                    dict.extend(line.split())
                    print(line)
            # input String
            str = "ajaykumar"

            if wordBreak(dict, str):
                wordBreak1(dict, str, "")
            else:
                print("\nString can't be segmented")

        elif(dataset=="DataSet10"):
            dict = []
            print("Input data set is:\n")
            with open("InputJ10.txt", "r") as f:
                for line in f:
                    dict.extend(line.split())
                    print(line)
            # input String
            str = "umaimasohail"

            if wordBreak(dict, str):
                wordBreak1(dict, str, "")
            else:
                print("\nString can't be segmented")
    messagebox.showerror("Congrats", "For Output, check Terminal")

button = Button(middle, text="OK", command=ok)
button.config(bg = "#ffece5", font =("TISA 12 bold"), fg = "#3c2f2f")
button.pack(pady = 3)


#Header
footer = tk.Frame(root, bg='#12232E')
footer.place(relx = 0, rely = 0.9, relwidth = 1, relheight = 0.5)

l3 = tk.Label(footer, text = "Presented By: \nAjay Kumar (18K-1136)\nUmaima Sohail (18K-1125)", bg = "#12232E", borderwidth = 0) 
l3.place(relx = 0.5, rely = 0.10, anchor = 'center', relwidth = 1)
l3.config(font =("TISA 8 bold"), fg = "white")

# Dynamic Programming implementation of LCS problem 
  
def lcs(X, Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n + 1) for i in range(m + 1)] 
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
# end of function lcs


def superSeq(X, Y, m, n):
    dp = [[0] * (n + 2) for i in range(m + 2)]
 
    # Fill table in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
 
            # Below steps follow above recurrence
            if (not i):
                dp[i][j] = j
            elif (not j):
                dp[i][j] = i
 
            elif (X[i - 1] == Y[j - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]
 
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],
                                   dp[i][j - 1])
 
    return dp[m][n]

def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],	 # Insert
                                            dp[i-1][j],	 # Remove
                                                dp[i-1][j-1])  # Replace

    return str(dp[m][n])

def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and  
    # initialize LIS values for all indexes 
    lis = [1]*n 
  
    # Compute optimized LIS values in bottom up manner 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if int(arr[i]) > int(arr[j]) and int(lis[i])< (int(lis[j]) + 1): 
                lis[i] = lis[j]+1
  
    # Initialize maximum to 0 to get  
    # the maximum of all LIS 
    maximum = 0
  
    # Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum , lis[i]-2) 
  
    return maximum 
# end of lis function

def MatrixChainOrder(p, n): 
    # For simplicity of the program,  
    # one extra row and one 
    # extra column are allocated in m[][].   
    # 0th row and 0th 
    # column of m[][] are not used 
    m = [[0 for x in range(n)] for x in range(n)] 
  
    # m[i, j] = Minimum number of scalar  
    # multiplications needed 
    # to compute the matrix A[i]A[i + 1]...A[j] =  
    # A[i..j] where 
    # dimension of A[i] is p[i-1] x p[i] 
  
    # cost is zero when multiplying one matrix. 
    for i in range(1, n): 
        m[i][i] = 0
  
    # L is chain length. 
    for L in range(2, n): 
        for i in range(1, n-L + 1): 
            j = i + L-1
            m[i][j] = sys.maxsize
            for k in range(i, j): 
  
                # q = cost / scalar multiplications 
                q = int(m[i][k]) + int(m[k + 1][j]) + int(p[i-1])*int(p[k])*int(p[j]) 
                if q < int(m[i][j]): 
                    m[i][j] = q 

    return str(m[1][n-1])


def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif int(wt[i-1]) <= w: 
                K[i][w] = max(int(val[i-1]) 
                          + int(K[i-1][w-int(wt[i-1])]),   
                              int(K[i-1][w])) 
            else: 
                K[i][w] = int(K[i-1][w]) 
  
    return K[n][W]


def findPartition(arr, n):
    sum = 0
    i, j = 0, 0
 
    # calculate sum of all elements
    for i in range(n):
        sum += int(arr[i])
 
    if sum % 2 != 0:
        return False
 
    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]
 
    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True
 
    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False
 
    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):
 
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
 
            if i >= int(arr[j - 1]):
                part[i][j] = (part[i][j] or
                              part[i - int(arr[j - 1])][j - 1])
 
    return part[sum // 2][n]

# A Dynamic Programming solution for Rod cutting problem 
INT_MIN = -32767
  
# Returns the best obtainable price for a rod of length n and 
# price[] as prices of different pieces 
def cutRod(price, n): 
    val = [0 for x in range(n + 1)] 
    val[0] = 0
  
    # Build the table val[] in bottom up manner and return 
    # the last entry from the table 
    for i in range(1, n + 1): 
        max_val = INT_MIN 
        for j in range(i): 
             max_val = max(max_val, int(price[j]) + int(val[i-j-1])) 
        val[i] = max_val 
  
    return str(val[n])

def findMinCoins(S, N):

    # T[i] stores minimum number of coins needed to get total of i
    T = [0] * (N + 1)

    for i in range(1, N + 1):

        # initialize minimum number of coins needed to infinity
        T[i] = float('inf')

        # do for each coin
        for c in range(len(S)):
            # check if index doesn't become negative by including
            # current coin c
            if i - int(S[c]) >= 0:
                res = T[i - int(S[c])]

                # if total can be reached by including current coin c,
                # update minimum number of coins needed T[i]
                if res != float('inf'):
                    T[i] = min(T[i], res + 1)

    # T[N] stores the minimum number of coins needed to get total of N
    return T[N]


def wordBreak(dict, str):

    # return true if we have reached the end of the String,
    if not str:
        return True

    for i in range(1, len(str) + 1):

        # consider all prefixes of current String
        prefix = str[:i]

        # return true if prefix is present in the dictionary and remaining
        # also forms space-separated sequence of one or more
        # dictionary words
        if prefix in dict and wordBreak(dict, str[i:]):
            return True

    # return false if the can't be segmented
    return False

# Function to segment given into a space-separated
# sequence of one or more dictionary words


def wordBreak1(dict, str, out):

    # if we have reached the end of the String,
    # print the output String
    if not str:
        print(out)
        return

    for i in range(1, len(str) + 1):
        # consider all prefixes of current String
        prefix = str[:i]

        # if the prefix is present in the dictionary, add prefix to the
        # output and recur for remaining String
        if prefix in dict:
            wordBreak1(dict, str[i:], out + " " + prefix)

tk.mainloop() 