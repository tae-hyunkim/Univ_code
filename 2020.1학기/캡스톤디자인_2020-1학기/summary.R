setwd('C:\\Users\\USER\\Desktop\\캡스톤디자인\\팀프로젝트')

data <- read.csv('smoke2.csv', encoding = 'CP949')

head(data)

data2 <- data[1:ncol(data)]
head(data2)

library('psych')
alpha(data2[,c('Long_term_1','Long_term_2','Long_term_3','Long_term_4')], na.rm=TRUE)
alpha(data2[,c('Short_term_1','Short_term_2','Short_term_3','Short_term_4')], na.rm=TRUE)
alpha(data2[,c('Marketing_Practice_1','Marketing_Practice_2','Marketing_Practice_3','Marketing_Practice_4')], na.rm=TRUE)
alpha(data2[,c('second_hand_1','second_hand_2','second_hand_3','second_hand_4')], na.rm=TRUE)
alpha(data2[,c('negative_role_1','negative_role_2','negative_role_3','negative_role_4')], na.rm=TRUE)
library(GPArotation)

cor(data2[6:25])
head(data2[6:25])
oif <- princomp(data2[6:25], cor = TRUE)
summary(oif)
summary(oif)$sdev

plot(oif, type='lines', ylim=c(0,5), main = 'Screeplot for PCA(Principal Component Analysis)')
abline(h=1)

oif.no<-principal(data2[6:25], nfactors = 5, rotate = 'norotate')
oif.no
oif.vm<-principal(data2[6:25], nfactors = 5, rotate = 'varimax')
oif.vm

library(dplyr)

data %>% group_by(alltime_tabacco) %>% summarise(mean(negative_role_model))
mean(data$negative_role_model)

class(data$long_term)
colnames(data2)
data3 = data2[c(2,3,4,5,6,10,14,18,22)]
data4 = data2[c(2,3,4,5,7,11,15,19,23)]
data5 = data2[c(2,3,4,5,8,12,16,20,24)]
data6 = data2[c(2,3,4,5,9,13,17,21,25)]
library(reshape)
#install.packages('agricolae')
library(agricolae)
library(car)
mel1 = melt(data3,id.vars=c('sex','smoking_count','family_count','parent_smoking'))
mel2 = melt(data4,id.vars=c('sex','smoking_count','family_count','parent_smoking'))
mel3 = melt(data5,id.vars=c('sex','smoking_count','family_count','parent_smoking'))
mel4 = melt(data6,id.vars=c('sex','smoking_count','family_count','parent_smoking'))

# data Class 확인 
sapply(mel1,class)
head(mel1)

# 금연에 대하여 생각하게 하는 정도의 차이 

# 정규성
shapiro.test(mel1$value)
# outlier 근데 왜 안되는지 모르겠음 
outlierTest(mel1$value)
# 등분산성 검사 
leveneTest(value~variable, data=mel1) # 등분산 만족 X 

oneway.test(value~variable, data=mel1) # 차이가 존재함을 증명함. 
aov1 = aov(value~variable, data=mel1)
summary(aov1)
install.packages('onewaytests')
library(onewaytests)
aov1 = welch.test(value~variable, data=mel1)

# TukeyHSD 활용 어떤 변수가 영향을 주는지 확인 
TukeyHSD(aov1) # Negative Role Model의 경우가 다른 모든 경우에 비해 금연에 대해 생각하게 만드는 효과가 있음.
plot(TukeyHSD(aov1), col='red')

library(userfriendlyscience)

posthocTGH(mel1$variable, y =mel1$value, method = 'games-howell')
# duncantest활용 군집으로 묶는다면 어떻게 묶이는가? 
out1 = duncan.test(aov1,'variable')
plot(out1, variation='IQR')

duncan.test(aov1,'variable',alpha=0.05,console = T)
# 총 4개의 군집으로 구분이 되며 가장 성능이 좋은 것은 Negative Role Model, 이후 Long_term, Marketing Practice가 성능이 우수함 
# Short term과 Sencond hand는 다른 것에 비해 성능 낮아짐. 

# 내 삶과 관련이 있다고 생각하는 정도의 차이 

# 정규성
shapiro.test(mel2$value)
# outlier 근데 왜 안되는지 모르겠음 
outlierTest(mel2$value)
# 등분산성 검사 
leveneTest(value~variable, data=mel2) # 등분산 만족 

aov2 = aov(value~variable, data=mel2)
summary(aov2) # 차이 존재함 

# TukeyHSD 활용 어떤 변수가 영향을 주는지 확인 
TukeyHSD(aov2)
# 간접흡연과 LongTerm 효과 비교시 간접흡연이 더 내 삶과 관련이 있다 생각함. 
# Negative Role Model과 간접흡연을 제외한 주제는 내 삶과 관련이 있다 생각하는 정도의 차이가 존재함 
# Neative role Model과 간접흡연의 차이가 유의하 지않음
plot(TukeyHSD(aov2), col='red')

# duncantest활용 군집으로 묶는다면 어떻게 묶이는가? 
out2 = duncan.test(aov2,'variable')
plot(out2, variation='IQR')

duncan.test(aov2,'variable',alpha=0.05,console = T)
# 가장 효과적인 방법의 순서로 나열하면 Negative, second, Marketing shorterm longterm

# 유용한 정보를 제공하는지 느끼는 차이 

# 정규성
shapiro.test(mel3$value)
# outlier 근데 왜 안되는지 모르겠음 
outlierTest(mel3$value)
# 등분산성 검사 
leveneTest(value~variable, data=mel3) # 등분산 만족 X 

oneway.test(value~variable, data = mel3)

aov1 = welch.test(value~variable, data=mel3)
posthocTGH(mel3$variable, y =mel3$value, method = 'games-howell')
# 그룹간 차이가 존재한다는 사실을 알 수 있음. 
aov3 = aov(value~variable, data=mel3)
summary(aov3)

# TukeyHSD 활용 어떤 변수가 영향을 주는지 확인 
TukeyHSD(aov3)
# Negative Role Model이 유용한 정보를 제공한다고 생각하는 정도가 가장 뛰어나고 나머지는 차이가 존재 X 
plot(TukeyHSD(aov3), col='red')

# duncantest활용 군집으로 묶는다면 어떻게 묶이는가? 
out3 = duncan.test(aov3,'variable')
plot(out3, variation='IQR')

duncan.test(aov3,'variable',alpha=0.05,console = T)
# duncan test결과 군집은 2개로 나뉘어지며 Negative roel model이 가장 효과가 좋다. 

# 주위 사람에게 금연을 권하고 싶은 정도의 차이 

# 정규성
shapiro.test(mel4$value)
# outlier 근데 왜 안되는지 모르겠음 
# outlierTest(mel4$value)
# 등분산성 검사 
leveneTest(value~variable, data=mel4) # 등분산 만족 X 

aov4 = aov(value~variable, data=mel4)
summary(aov4)
oneway.test(value~variable,data=mel4)
# 집단간 차이가 존재한다는 것을 알 수 있음. 
# TukeyHSD 활용 어떤 변수가 영향을 주는지 확인 
TukeyHSD(aov4)
# Negative Role Model이 주위 사람에게 금연을 권하고 싶은 정도의 차이가 유의하게 나타나며 높은 수치를 기록함.
plot(TukeyHSD(aov4), col='red')

# duncantest활용 군집으로 묶는다면 어떻게 묶이는가? 
out4 = duncan.test(aov4,'variable')
plot(out4, variation='IQR')

duncan.test(aov4,'variable',alpha=0.05,console = T)
# 군집은 4개로 나뉘어 지며 Negative Role Model이 가장 주위사람에게 권하고 싶어함 이후는 Marketing Practice

# 담배 경험과 광고 변수 
table(mel1[2]) # 5갑 미만에 대한 데이터를 최소 150개 이상 모아야함 설문지 변수가 5개이므로 5로 나누어봐야하기 때문.. 

# 금연 생각 정도의 차이

aov1_1 = aov(value~variable + smoking_count, data = mel1)
aov1_2 = aov(value~variable * smoking_count, data = mel1)

summary(aov1_1)
summary(aov1_2)

anova(aov1_1, aov1_2)
# 담배 경험과 금연생각에 상호작용이 존재한다. 

TukeyHSD(aov1_1, which = 'variable')
TukeyHSD(aov1_1, which = 'smoking_count')

TukeyHSD(aov1_2, which = 'variable')
TukeyHSD(aov1_2, which = 'smoking_count')

# 내 삶과 관련이 있다고 생각하는 정도의 차이 
aov2_1 = aov(value~variable + smoking_count, data = mel2)
aov2_2 = aov(value~variable * smoking_count, data = mel2)

summary(aov2_1)
summary(aov2_2)
# 담배 경험과 내 삶과 관련된다고 생각하는 정도에 상호작용이 존재한다. 

TukeyHSD(aov2_1, which = 'variable')
TukeyHSD(aov2_1, which = 'smoking_count')

TukeyHSD(aov2_2, which = 'variable')
TukeyHSD(aov2_2, which = 'smoking_count')

anova(aov2_1, aov2_2)
# 유용한 정보를 제공하는지 느끼는 차이 

aov3_1 = aov(value~variable + smoking_count, data = mel3)
aov3_2 = aov(value~variable * smoking_count, data = mel3)

summary(aov3_1)
summary(aov3_2)
# 유용한 정보 제공한다 생각하는 상호 작용 존재 

TukeyHSD(aov3_1, which = 'variable')
TukeyHSD(aov3_1, which = 'smoking_count')

TukeyHSD(aov3_2, which = 'variable')
TukeyHSD(aov3_2, which = 'smoking_count')

anova(aov2_1, aov2_2)
# 상호작용 고려가 더 좋다 

# 주위 사람에게 금연을 권하고 싶은 정도의 차이 

aov4_1 = aov(value~variable + smoking_count, data = mel4)
aov4_2 = aov(value~variable * smoking_count, data = mel4)

summary(aov4_1)
summary(aov4_2)
# 주위사람에게 금연을 권장하고 하는 생각의 정도의 차이에 흡연 경험정도와 주제간 상호작용이 존재한다 

TukeyHSD(aov4_1, which = 'variable')
TukeyHSD(aov4_1, which = 'smoking_count')

TukeyHSD(aov4_2, which = 'variable')
TukeyHSD(aov4_2, which = 'smoking_count')

anova(aov4_1, aov4_2)
# 상호작용을 고려한 모델이 더 좋다. 

head(mel1)

mel1$new_fac = as.factor(paste(mel1$smoking_count, mel1$variable))
mel2$new_fac = as.factor(paste(mel2$smoking_count, mel2$variable))
mel3$new_fac = as.factor(paste(mel3$smoking_count, mel3$variable))
mel4$new_fac = as.factor(paste(mel4$smoking_count, mel4$variable))

# 등분산성 검사 
leveneTest(value~new_fac, data=mel1) # 등분산 만족 X 

oneway.test(value~new_fac, data=mel1) # 차이가 존재함을 증명함. 
aov1 = aov(value~new_fac, data=mel1)
summary(aov1)
welch.test(value~new_fac, data=mel1)
posthocTGH(mel1$new_fac, y =mel1$value, method = 'games-howell')

# TukeyHSD 활용 어떤 변수가 영향을 주는지 확인 
TukeyHSD(aov1) # Negative Role Model의 경우가 다른 모든 경우에 비해 금연에 대해 생각하게 만드는 효과가 있음.
plot(TukeyHSD(aov1), col='red')

# duncantest활용 군집으로 묶는다면 어떻게 묶이는가? 
out1 = duncan.test(aov1,'new_fac')
plot(out1, variation='IQR')

duncan.test(aov1,'new_fac',alpha=0.05,console = T)
# 총 4개의 군집으로 구분이 되며 가장 성능이 좋은 것은 Negative Role Model, 이후 Long_term, Marketing Practice가 성능이 우수함 
# Short term과 Sencond hand는 다른 것에 비해 성능 낮아짐. 

# 내 삶과 관련이 있다고 생각하는 정도의 차이 

# 등분산성 검사 
leveneTest(value~new_fac, data=mel2) # 등분산 만족 

aov2 = aov(value~new_fac, data=mel2)
summary(aov2) # 차이 존재함 

# TukeyHSD 활용 어떤 변수가 영향을 주는지 확인 
TukeyHSD(aov2)
# 간접흡연과 LongTerm 효과 비교시 간접흡연이 더 내 삶과 관련이 있다 생각함. 
# Negative Role Model과 간접흡연을 제외한 주제는 내 삶과 관련이 있다 생각하는 정도의 차이가 존재함 
# Neative role Model과 간접흡연의 차이가 유의하 지않음
plot(TukeyHSD(aov2), col='red')

# duncantest활용 군집으로 묶는다면 어떻게 묶이는가? 
out2 = duncan.test(aov2,'new_fac')
plot(out2, variation='IQR')

duncan.test(aov2,'new_fac',alpha=0.05,console = T)
# 가장 효과적인 방법의 순서로 나열하면 Negative, second, Marketing shorterm longterm

# 유용한 정보를 제공하는지 느끼는 차이 

# 등분산성 검사 
leveneTest(value~new_fac, data=mel3) # 등분산 만족 X 

oneway.test(value~new_fac, data = mel3)
# 그룹간 차이가 존재한다는 사실을 알 수 있음. 
aov3 = aov(value~new_fac, data=mel3)
summary(aov3)

welch.test(value~new_fac, data=mel3)
posthocTGH(mel3$new_fac, y =mel3$value, method = 'games-howell')
# TukeyHSD 활용 어떤 변수가 영향을 주는지 확인 
TukeyHSD(aov3)
# Negative Role Model이 유용한 정보를 제공한다고 생각하는 정도가 가장 뛰어나고 나머지는 차이가 존재 X 
plot(TukeyHSD(aov3), col='red')

# duncantest활용 군집으로 묶는다면 어떻게 묶이는가? 
out3 = duncan.test(aov3,'new_fac')
plot(out3, variation='IQR')

duncan.test(aov3,'new_fac',alpha=0.05,console = T)
# duncan test결과 군집은 2개로 나뉘어지며 Negative roel model이 가장 효과가 좋다. 

# 주위 사람에게 금연을 권하고 싶은 정도의 차이 

# 등분산성 검사 
leveneTest(value~new_fac, data=mel4) # 등분산 만족 X 

aov4 = aov(value~new_fac, data=mel4)
summary(aov4)
oneway.test(value~new_fac,data=mel4)
# 집단간 차이가 존재한다는 것을 알 수 있음. 
# TukeyHSD 활용 어떤 변수가 영향을 주는지 확인 
TukeyHSD(aov4)
# Negative Role Model이 주위 사람에게 금연을 권하고 싶은 정도의 차이가 유의하게 나타나며 높은 수치를 기록함.
plot(TukeyHSD(aov4), col='red')

# duncantest활용 군집으로 묶는다면 어떻게 묶이는가? 
out4 = duncan.test(aov4,'new_fac')
plot(out4, variation='IQR')

duncan.test(aov4,'new_fac',alpha=0.05,console = T)
# 군집은 4개로 나뉘어 지며 Negative Role Model이 가장 주위사람에게 권하고 싶어함 이후는 Marketing Practice
