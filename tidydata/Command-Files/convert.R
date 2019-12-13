library(foreign)
mydata = read.spss("pew.sav",to.data.frame=TRUE)
write.table(mydata,"pew_conv.txt",sep = ";;")