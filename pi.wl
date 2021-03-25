Initializing variables (change iter to change iteration amount)
n=0;
pi=0;
iter=10;
____________________________________________________
The
For[k=0,k<=iter,k++,n+=Divide[(6k)!(545140134k+13591409),(3k)!((k!)^3)(-262537412640768000)^k];Print[k,"/",iter," done\033[2F"]]
____________________________________________________
Writing result to file
WriteString["output.txt",InputForm[Divide[1,Divide[n,426880Sqrt[10005]]]]]