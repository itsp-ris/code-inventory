# Author: Priscilla Tham Ai Ching
# Student ID: 28390121
# Date: 26/04/2020

library(ROCR)
library(tree)
library(e1071)
library(ggplot2)
library(rpart)
library(caret)
library(adabag)
library(randomForest)
library(neuralnet)
library(car)

getConfusionMatrix = 
  function(actual.class, predicted.class) {
    table(actual=actual.class, 
          predicted=predicted.class)
  }

doPrediction = 
  function(trainedmodel, newdata, type) {
    return(predict(
      trainedmodel, newdata, type=type))
}

WAUS = read.csv("WAUS2020.csv")
L = as.data.frame(c(1:49))
set.seed(28390121)
L = L[sample(nrow(L), 10, replace=FALSE), ]
WAUS = WAUS[(WAUS$Location %in% L), ]
WAUS = WAUS[
  sample(nrow(WAUS), 2000, replace=FALSE), ]

# remove rows containing NA
WAUS = na.omit(WAUS)
#####

# convert these variables to factor type
factor.var = c("Day", "Month", "Year", "Location", 
                   "WindGustDir", "WindDir9am", 
                   "WindDir3pm", "RainToday", 
                   "RainTomorrow")
WAUS[, factor.var] = lapply(
  WAUS[, factor.var], factor)
# find mode for factor type variables
factor.var.summary = lapply(
  WAUS[, factor.var], summary)
lapply(factor.var.summary, which.max)

real.var = names(WAUS)[
  !(names(WAUS) %in% factor.var)]
# get the description for integer and numerical 
# variables; including mean, min, 1st quartile, 
# median, 3rd quartile and max
summary(WAUS[real.var])
# calculate the standard deviation for integer and 
# numerical variables
round(apply(WAUS[, real.var], 2, sd), 2)

# get proportion of rainy days to fine days
nrow(WAUS[WAUS$RainToday == "Yes",])
nrow(WAUS[WAUS$RainToday != "Yes",])
#####

set.seed(28390121) #Student ID as random seed
train.row = sample(1:nrow(WAUS), 0.7*nrow(WAUS))
WAUS.train = WAUS[train.row,]
WAUS.test = WAUS[-train.row,]

### fit tree model
WAUS.fit = tree(RainTomorrow~., data=WAUS.train)
# get important variables
summary(WAUS.fit)[["used"]]
# test accuracy
WAUS.predict = doPrediction(
  WAUS.fit, WAUS.test, "class")
getConfusionMatrix(
  WAUS.test$RainTomorrow, WAUS.predict)
# standardize
WAUS.predict = doPrediction(
  WAUS.fit, WAUS.test, "vector")
WAUS.predicted = prediction(
  WAUS.predict[,2], WAUS.test$RainTomorrow)
WAUS.performance = performance(
  WAUS.predicted, "tpr", "fpr")
# calculate auc
performance(WAUS.predicted, measure="auc")@y.values
###

### fit naive bayes model
WAUS.bayes = naiveBayes(
  RainTomorrow~., data=WAUS.train)
# test accuracy
WAUS.bayes.predict = doPrediction(
  WAUS.bayes, WAUS.test, "class")
getConfusionMatrix(
  WAUS.test$RainTomorrow, WAUS.bayes.predict)
# standardize
WAUS.bayes.predict = doPrediction(
  WAUS.bayes, WAUS.test, "raw")
WAUS.bayes.predicted = prediction(
  WAUS.bayes.predict[,2], WAUS.test$RainTomorrow)
WAUS.bayes.performance = performance(
  WAUS.bayes.predicted, "tpr", "fpr")
# calculate auc
performance(
  WAUS.bayes.predicted, measure="auc")@y.values
###

### bagging
WAUS.bag = bagging(
  RainTomorrow~., data=WAUS.train)
# get important variables
WAUS.bag$importance
# test accuracy
WAUS.bag.predict = predict.bagging(
  WAUS.bag, WAUS.test)
WAUS.bag.predict$confusion
# standardize
WAUS.bag.predicted = prediction(
  WAUS.bag.predict$prob[,2], WAUS.test$RainTomorrow)
WAUS.bag.performance = performance(
  WAUS.bag.predicted, "tpr", "fpr")
# calculate auc
performance(
  WAUS.bag.predicted, measure="auc")@y.values
# plot variables' importance
importanceplot(WAUS.bag, horiz=TRUE, cex.names=.6)
###

### boosting
WAUS.boost = boosting(
  RainTomorrow~., data=WAUS.train)
# get important variables
WAUS.boost$importance
# test accuracy
WAUS.boost.predict = predict.boosting(
  WAUS.boost, WAUS.test)
WAUS.boost.predict$confusion
# standardize
WAUS.boost.predicted = prediction(
  WAUS.boost.predict$prob[,2], 
  WAUS.test$RainTomorrow)
WAUS.boost.performance = performance(
  WAUS.boost.predicted, "tpr", "fpr")
# calculate auc
performance(
  WAUS.boost.predicted, measure="auc")@y.values
# plot variables' importance
importanceplot(WAUS.boost, horiz=TRUE, cex.names=.6)
###

### random forest
WAUS.rf = randomForest(
  RainTomorrow~., data=WAUS.train)
# get important variables
WAUS.rf$importance
# test accuracy
WAUS.rf.predict = doPrediction(
  WAUS.rf, WAUS.test, "class")
getConfusionMatrix(
  WAUS.test$RainTomorrow, WAUS.rf.predict)
# standardize
WAUS.rf.predict = doPrediction(
  WAUS.rf, WAUS.test, "prob")
WAUS.rf.predicted = prediction(
  WAUS.rf.predict[,2], WAUS.test$RainTomorrow)
WAUS.rf.performance = performance(
  WAUS.rf.predicted, "tpr", "fpr")
# calculate auc
performance(
  WAUS.rf.predicted, measure="auc")@y.values
varImpPlot(WAUS.rf,
           main="Variable relative importance")
###

##### plot ROC Curve
ggplot() + 
  geom_line(
    aes(x=WAUS.performance@x.values[[1]], 
        y=WAUS.performance@y.values[[1]], 
        colour="Decision Tree")) + 
  geom_line(
    aes(x=WAUS.bayes.performance@x.values[[1]], 
        y=WAUS.bayes.performance@y.values[[1]], 
        colour="Naive Bayes")) + 
  geom_line(
    aes(x=WAUS.bag.performance@x.values[[1]], 
        y=WAUS.bag.performance@y.values[[1]], 
        colour="Bagging")) + 
  geom_line(
    aes(x=WAUS.boost.performance@x.values[[1]], 
        y=WAUS.boost.performance@y.values[[1]], 
        colour="Boosting")) + 
  geom_line(
    aes(x=WAUS.rf.performance@x.values[[1]], 
        y=WAUS.rf.performance@y.values[[1]], 
        colour="Random Forest")) + 
  labs(x="False Positive Rate", 
       y="True Positive Rate", 
       title="ROC Curve of Decision Tree, 
       Naive Bayes, Bagging, Boosting and 
       Random Forest Technique")

#####

### decision tree improvement
test.WAUS.fit = cv.tree(
  WAUS.fit, FUN=prune.misclass)
# get best tree size
best = test.WAUS.fit[["size"]][
  length(test.WAUS.fit[["size"]])/2]
# prune to best size
prune.WAUS.fit = prune.misclass(WAUS.fit, best=best)
# get important variables
summary(prune.WAUS.fit)[["used"]]
# test accuracy
prune.WAUS.predict = doPrediction(
  prune.WAUS.fit, WAUS.test, "class")
getConfusionMatrix(
  WAUS.test$RainTomorrow, prune.WAUS.predict)
###

### bagging improvement
set.seed(28390121)
control = trainControl(method="cv", number=10)
test.WAUS.bag = train(
  RainTomorrow~. -RainToday, data=WAUS.train,
  method="AdaBag", trControl=control)
# get variables' importance
test.WAUS.bag$finalModel$importance
# test accuracy
imprv.WAUS.bag.predict = doPrediction(
  test.WAUS.bag, WAUS.test, "raw")
getConfusionMatrix(
  WAUS.test$RainTomorrow, imprv.WAUS.bag.predict)
###

### boosting improvement
test.WAUS.boost = train(
  RainTomorrow~. -RainToday, data=WAUS.train,
  method="adaboost", trControl=control)
# get variables' importance
test.WAUS.boost$finalModel$importance
# test accuracy
imprv.WAUS.boost.predict = doPrediction(
  test.WAUS.boost, WAUS.test, "raw")
getConfusionMatrix(
  WAUS.test$RainTomorrow, imprv.WAUS.boost.predict)
###

### random forest improvement
test.WAUS.rf = train(
  RainTomorrow~., data=WAUS.train, 
  method="rf", trControl=control)
imprv.WAUS.rf.predict = doPrediction(
  test.WAUS.rf, WAUS.test, "raw")
getConfusionMatrix(
  WAUS.test$RainTomorrow, imprv.WAUS.rf.predict)
###

#####
# preprocess dataset
# remove categorical predictor 
# (independent) variables
new.columns = c(real.var, "RainTomorrow")
new.WAUS.train = WAUS.train[, new.columns]
new.WAUS.test = WAUS.test[, new.columns]
# convert categorical response variable to 
# numerical
new.WAUS.train$RainTomorrow = recode(
  new.WAUS.train$RainTomorrow, "'Yes'='1';'No'='2'")
new.WAUS.test$RainTomorrow = recode(
  new.WAUS.test$RainTomorrow, "'Yes'='1';'No'='2'")

new.WAUS.train$RainTomorrow = as.numeric(
  new.WAUS.train$RainTomorrow)
new.WAUS.test$RainTomorrow = as.numeric(
  new.WAUS.test$RainTomorrow)

# train neural network
WAUS.nn = neuralnet(
  RainTomorrow==1~., data=new.WAUS.train, 
  hidden=c(3, 2), linear.output=FALSE)
# test accuracy
WAUS.nn.predict = compute(
  WAUS.nn, new.WAUS.test[
    names(new.WAUS.test) != "RainTomorrow"])
prob = WAUS.nn.predict$net.result
pred = ifelse(prob>0.5, 1, 2)
getConfusionMatrix(
  new.WAUS.test$RainTomorrow, pred)
#####

