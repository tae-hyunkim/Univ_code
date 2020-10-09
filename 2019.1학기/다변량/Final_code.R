setwd('C:/Users/hyoun/Desktop/regression')
rm(list=ls())
library(ISLR)
data = read.csv('대장암_new.csv')
head(data)
data_man = data[data$sex=='Man',][,-1]
str(data_man)
cor(data_man[,c(1,2,3,4,5,10,11)])
pairs(data_man[,c(1,2,3,4,5,10,11)])
head(data_man)
str(data_man)

wss=c()
for (k in 2:20){
  km=kmeans(data_man[,c(1,4)], center=k, nstart=10)
  wss=c(wss, km$tot.withinss)
}
plot(2:20, wss, type="b", xlab="Number of Clusters")
km=kmeans(data_man[,c(1,4)], center=5, nstart=10)
table(cluster)
data_man$cluster = km$cluster
head(data_man)

library(plotly) #install.packages('tidyselect')
plot_ly(data=data_man,y=~bmi,x=~age,color=~cluster)

data1 = data_man[data_man$cluster==1,][,-c(2,3,11,15)]
data2 = data_man[data_man$cluster==2,][,-c(2,3,11,15)]
data3 = data_man[data_man$cluster==3,][,-c(2,3,11,15)]
data4 = data_man[data_man$cluster==4,][,-c(2,3,11,15)]
data5 = data_man[data_man$cluster==5,][,-c(2,3,11,15)]
# 1번군집
summary(data1)
data1 = data1[,-9]
fit1 = glm(대장암여부~.,data1,family = 'binomial')
summary(fit1)

# 2번군집 #과거암이력 제거해야함
summary(data2)
fit2 = glm(대장암여부~.,data2,family = 'binomial')
summary(fit2)

# 3번군집
summary(data3)
fit3 = glm(대장암여부~.,data3,family = 'binomial')
summary(fit3)

# 4번군집
summary(data4)
data4 = data4[,-9]
fit4 = glm(대장암여부~.,data4,family = 'binomial')
summary(fit4)

# 5번군집
summary(data5)
fit5 = glm(대장암여부~.,data5,family = 'binomial')
summary(fit5)
####################################################
data_woman = data[data$sex!='Man',][,-1]
cor(data_woman[,c(1,2,3,4,5,10,11)])
pairs(data_woman[,c(1,2,3,5,10,11)])
head(data_woman)
summary(data_woman)

wss=c()
for (k in 2:30){
  km=kmeans(data_woman[,c(1,4)], center=k, nstart=10)
  wss=c(wss, km$tot.withinss)
}
plot(2:30, wss, type="b", xlab="Number of Clusters")

km=kmeans(data_woman[,c(1,4)], center=5, nstart=5)
table(km$cluster)
data_woman$cluster = km$cluster
library(plotly) #install.packages('tidyselect')
plot_ly(data=data_woman,y=~bmi,x=~age,color=~cluster)

data1 = data_woman[data_woman$cluster==1,][,-c(2,3,11,15)]
data2 = data_woman[data_woman$cluster==2,][,-c(2,3,11,15)]
data3 = data_woman[data_woman$cluster==3,][,-c(2,3,11,15)]
data4 = data_woman[data_woman$cluster==4,][,-c(2,3,11,15)]
data5 = data_woman[data_woman$cluster==5,][,-c(2,3,11,15)]

# 1번군집
summary(data1)
fit1 = glm(대장암여부~.,data1,family = 'binomial')
summary(fit1)

# 2번군집 #과거암이력 제거해야함
summary(data2)
fit2 = glm(대장암여부~.,data2,family = 'binomial')
summary(fit2)

# 3번군집
summary(data3)
fit3 = glm(대장암여부~.,data3,family = 'binomial')
summary(fit3)

# 4번군집
summary(data4)
fit4 = glm(대장암여부~.,data4,family = 'binomial')
summary(fit4)

# 5번군집
summary(data5)
data5 = data5[,-9]
fit5 = glm(대장암여부~.,data5,family = 'binomial')
summary(fit5)
