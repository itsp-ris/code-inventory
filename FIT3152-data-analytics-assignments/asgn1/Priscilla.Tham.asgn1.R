# Author: Priscilla Tham Ai Ching
# Student ID: 28390121
# Date: 26/04/2020

library("ggplot2")
library("ggnet")
library("network")
library("sna")

# adding connections from one vector to another
# in adjacent matrix
makeAdjMat <- function(adj_Mat, by_data, v_data) {
  count = 0
  for (i in 2:length(by_data)) {
    if (by_data[i-1] !=
        by_data[i]) {
      count = 0
      
    } else {
      head = which(
        users==v_data[i-1])
      tail = which(
        users==v_data[i])
      adj_Mat[head, tail] = 1
      adj_Mat[tail, head] = 1
      count = count + 1
      
      if (count > 1) {
        # adding edges to all the other vectors
        # in the same thread
        for (j in (i - count):(i-2)) {
          head = which(
            users==v_data[j])
          tail = which(
            users==v_data[i])
          adj_Mat[head, tail] = 1
          adj_Mat[tail, head] = 1
        }
      }
    }
  }
  return(adj_Mat)
}


# count the number of occurrences of names
# and convert it to a data frame
getFreq <- function(names, renames) {
  return(as.data.frame(table(names, dnn=renames)))
}


# perform the function fn on rows of names
# then group them by the variable by
groupBy <- function(names, by, data, fn) {
  return(aggregate(names, by=by, data=data, FUN=fn))
}


# stack the names by the variable by
meltDf <- function(by, names) {
  return(cbind(row.names=NULL, by, stack(names)))
}


# rename columns in data frames
rename <- function(data, columns, names) {
  colnames(data)[columns] = names
  return(data)
}


# find the maximum in name and return its position
findMax <- function(name) {
  return(which.max(name))
}


set.seed(28390121) #XXXXXXXX = your student ID
forum_data = read.csv(file="webforum.csv", 
                      header=TRUE)
forum_data = forum_data[
  sample(nrow(forum_data), 20000), 
  ] # 20000 rows

# remove non-text post and anonymous user
forum_data = forum_data[
  forum_data$AuthorID!=-1 & forum_data$WC!=0, ]

# Question A
# count occurrences of each author ID
user_post_count = getFreq(forum_data$AuthorID, 
                     c("AuthorID"))
most_active_user = user_post_count$AuthorID[
  findMax(user_post_count$Freq)
]

# count occurrences of each thread ID
thread_post_count = getFreq(forum_data$ThreadID, 
                            c("ThreadID"))
most_active_thread = thread_post_count$ThreadID[
  findMax(thread_post_count$Freq)
]

# count occurrences of each author ID's 
# each thread ID
each_user_thread_post_count = getFreq(
  list(forum_data$AuthorID, forum_data$ThreadID), 
  c("AuthorID", "ThreadID"))

# threads of author ID = most active user author ID
most_active_user_threads = 
  each_user_thread_post_count[
    which(each_user_thread_post_count$AuthorID==
            most_active_user), ]
most_active_user_most_active_thread = 
  most_active_user_threads$ThreadID[
    findMax(most_active_user_threads$Freq)
]

cor(forum_data$AuthorID, forum_data$ThreadID)

### hypothesis test on H0: the probability of most 
# active thread being the most active user's most 
# active thread <= 60%
# H1: the probability of most active thread being 
# the most active user's most active thread > 60%
other_users_threads = 
  each_user_thread_post_count[
    which(each_user_thread_post_count$AuthorID!=
            most_active_user), ]
mean = mean(most_active_user_threads$Freq) - 
  mean(other_users_threads$Freq)
approx_z_score = mean/sqrt(
  (var(most_active_user_threads$Freq)/
     length(most_active_user_threads$Freq)) + 
    (var(other_users_threads$Freq)/
       length(other_users_threads$Freq)))
p_value = 2*pnorm(-abs(approx_z_score))
###

# adding the column Year to data
forum_data["Year"] = format(
  as.Date(forum_data$Date, format="%Y-%m-%d"), "%Y")

# count the occurrences of each year
yearly_post_count = getFreq(
  forum_data$Year, c("Year"))
ggplot(data=yearly_post_count, aes(
  x=Year, y=Freq, group=1)) + 
  geom_line() + 
  geom_point() + 
  ggtitle("Post Frequency of Each Year")

LIWC = with(forum_data, 
            cbind(Analytic, Clout, Authentic, Tone, 
                  ppron, i, we, you, shehe, they, 
                  affect, posemo, negemo))

yearly_LIWC = groupBy(
  LIWC, list(forum_data$Year), forum_data, "mean")

round(cor(forum_data[, c(17)], 
          forum_data[, 18:19]), digits=4)

### hypothesis test on H0: the probability of  
# positive sentiment expressed <= 80% 
# H1: the probability of positive sentiment
# expressed is > 80%
mean = mean(yearly_LIWC$posemo) - 
  mean(yearly_LIWC$affect)
approx_z_score = mean/sqrt(
  (var(yearly_LIWC$posemo)/
     length(yearly_LIWC$posemo)) + 
    (var(yearly_LIWC$affect)/
       length(yearly_LIWC$affect)))
p_value = 2*pnorm(-abs(approx_z_score))
###

yearly_sentiment_LIWC = meltDf(
  yearly_LIWC[1], yearly_LIWC[12:14])
yearly_sentiment_LIWC = rename(
  yearly_sentiment_LIWC, 1:3, c("Year", "LIWC", 
                                "Group"))
ggplot(data=yearly_sentiment_LIWC, aes(
  x=Year, y=log(LIWC), group=Group, color=Group)) + 
  geom_line() + 
  geom_point() + 
  ggtitle("Linguistic Inquiry and Word Count (LIWC) 
          Summary of Each Year in Affect, Positive 
          and Negative Emotions")

yearly_voice_LIWC = meltDf(
  yearly_LIWC[1], yearly_LIWC[2:5])
yearly_voice_LIWC = rename(
  yearly_voice_LIWC, 1:3, c("Year", "LIWC", 
                            "Group"))
ggplot(data=yearly_voice_LIWC, aes(
  x=Year, y=log(LIWC), group=Group, color=Group)) + 
  geom_line() + 
  geom_point() + 
  ggtitle("Linguistic Inquiry and Word Count (LIWC) 
          Summary of Each Year in Analytic, 
          Authenticity, Clout and Tone")

yearly_pronouns_LIWC = meltDf(
  yearly_LIWC[1], yearly_LIWC[6:11])
yearly_pronouns_LIWC = rename(
  yearly_pronouns_LIWC, 1:3, c("Year", "LIWC", 
                                "Group"))
ggplot(data=yearly_pronouns_LIWC, aes(
  x=Year, y=log(LIWC), group=Group, color=Group)) + 
  geom_line() + 
  geom_point() + 
  ggtitle("Linguistic Inquiry and Word Count (LIWC) 
          Summary of Pronouns in Each Year")

keywords = with(forum_data, 
                cbind(anx, anger, social, family, 
                      friend, leisure, money, 
                      relig, swear, QMark))

cor(forum_data$social, forum_data$Clout)

### hypothesis test on H0: the probability of a 
# post content referring to social processes
# has higher Clout values <= 60%
# H1: the probability of post content referring to 
# social processes has higher Clout values > 60%
mean = mean(forum_data$social) - 
  mean(forum_data$Clout)
approx_z_score = mean/sqrt(
  (var(forum_data$social)/
     length(forum_data$social)) + 
    (var(forum_data$Clout)/
       length(forum_data$Clout)))
p_value = 2*pnorm(-abs(approx_z_score))
###

cor(forum_data$anger, forum_data$negemo)

### hypothesis test on H0: the probability of 
# anger referred words relating to negative 
# emotions is <= 60%
# H1: the probability of anger referred words
# relating to negative emotions is > 60%
mean = mean(forum_data$anger) - 
  mean(forum_data$negemo)
approx_z_score = mean/sqrt(
  (var(forum_data$anger)/
     length(forum_data$anger)) + 
    (var(forum_data$negemo)/
       length(forum_data$negemo)))
p_value = 2*pnorm(-abs(approx_z_score))
###

yearly_keywords = groupBy(
  keywords, list(forum_data$Year), 
  data=forum_data, "mean")
yearly_keywords = meltDf(
  yearly_keywords[1], yearly_keywords[-1])
yearly_keywords = rename(
  yearly_keywords, 1:3, c("Year", "Proportion", 
                          "Group"))
ggplot(data=yearly_keywords, aes(
  x=Year, y=log(Proportion), 
  group=Group, color=Group)) + 
  geom_line() + 
  geom_point() + 
  ggtitle("Proportion of Keywords in Each Year")

# adding the column Polarity to data
forum_data["Polarity"] = forum_data$posemo - 
  forum_data$negemo

user_yearly_LIWC = with(forum_data, groupBy(
  cbind(LIWC, Polarity), list(Year, AuthorID), 
  forum_data, "mean"))
user_yearly_LIWC = rename(
  user_yearly_LIWC, 1:2, c("Year", "AuthorID"))
qplot(data=user_yearly_LIWC, facets=~Year, 
      x=log(Analytic), y=log(Authentic), 
      size=log(Clout), alpha=log(Tone), 
      color=factor(sign(Polarity))) +
  ggtitle("User Distribution in Analytic, 
          Authenticity, Clout, Tone and Polarity in 
          Each Year")

#####

#Question B
# count the occurrences of each thread in each year
yearly_thread_post_count = getFreq(
  list(forum_data$ThreadID, forum_data$Year), 
  c("ThreadID", "Year"))
yearly_thread_post_count = yearly_thread_post_count[
  yearly_thread_post_count$Freq!=0,]

# count the occurrences of each thread in 
# yearly_thread_post_count
id_occurences = getFreq(
  yearly_thread_post_count$ThreadID, c("ThreadID"))

set.seed(28390121)
# sample 9 nine threads from 
# yearly_thread_post_count that occur in more than
# one year
sample_ids = sample((id_occurences[
  id_occurences$Freq>1,])$ThreadID, 9)

thread_yearly_LIWC = with(forum_data, groupBy(
  cbind(LIWC, Polarity), list(Year, ThreadID), 
  forum_data, "mean"))
thread_yearly_LIWC = rename(
  thread_yearly_LIWC, 1:2, c("Year", "ThreadID"))

# get the nine threads' sentiment LIWC in each year
thread_yearly_sentiment_LIWC = thread_yearly_LIWC[
  thread_yearly_LIWC$ThreadID %in% sample_ids, ]
ggplot(data=thread_yearly_sentiment_LIWC, aes(
  x=Year, y=log(affect), group=1)) + 
  geom_line() + 
  geom_point(aes(color=factor(sign(Polarity)), 
                 size=Polarity)) +
  facet_wrap(~ThreadID) + 
  ggtitle("Linguistic Inquiry and Word Count (LIWC) 
          Summary of Random Threads in Each Year in 
          Affect and Polarity")

thread_yearly_voice_LIWC = meltDf(
  thread_yearly_LIWC[1:2], thread_yearly_LIWC[3:6])
thread_yearly_voice_LIWC = rename(
  thread_yearly_voice_LIWC, 3:4, c("LIWC", "Group"))

# get the nine threads' voice LIWC in each year
thread_yearly_voice_LIWC = thread_yearly_voice_LIWC[
  thread_yearly_voice_LIWC$ThreadID %in% 
    sample_ids, ]
ggplot(data=thread_yearly_voice_LIWC, aes(
  x=Year, y=log(LIWC), group=Group, color=Group)) + 
  geom_line() + 
  geom_point() +
  facet_wrap(~ThreadID) + 
  ggtitle("Linguistic Inquiry and Word Count (LIWC) 
          Summary of Random Threads in Each Year in 
          Analytic, Authenticity, Clout and Tone")

thread_yearly_keywords = with(forum_data, groupBy(
  keywords, list(Year, ThreadID), 
  data=forum_data, "mean"))
thread_yearly_keywords = meltDf(
  thread_yearly_keywords[1:2], 
  thread_yearly_keywords[
    3:ncol(thread_yearly_keywords)])
thread_yearly_keywords = rename(
  thread_yearly_keywords, 1:4, 
  c("Year", "ThreadID", "Proportion", "Group"))

# get the nine threads' proportion of keywords in 
# each year
thread_yearly_keywords = 
  thread_yearly_keywords[
    thread_yearly_keywords$ThreadID %in% 
      sample_ids, ]
ggplot(data=thread_yearly_keywords, aes(
  x=Year, y=log(Proportion), 
  group=Group, color=Group)) + 
  geom_line() + 
  geom_point() +
  facet_wrap(~ThreadID) + 
  ggtitle("Proportion of Keywords in Random Threads 
          in Each Year")

thread_daily_LIWC = with(forum_data, groupBy(
  cbind(LIWC, Polarity), 
  list(Year, ThreadID, Date), forum_data, "mean"))
thread_daily_LIWC = rename(
  thread_daily_LIWC, 1:3, 
  c("Year", "ThreadID", "Date"))

# get the nine threads' LIWC in each day of 
# each year
thread_daily_LIWC = thread_daily_LIWC[
  thread_daily_LIWC$ThreadID %in% sample_ids, ]
qplot(data=thread_daily_LIWC, facets=ThreadID~Year, 
      x=log(Analytic), y=log(Authentic), 
      size=log(Clout), alpha=log(Tone), 
      color=factor(sign(Polarity))) + 
  ggtitle("Post Distribution in Analytic, 
          Authenticity, Clout, Tone and Polarity of 
          Random Threads in Each Year")

#####

#Question C
# count the occurrences of each author ID in 
# each thread ID in each year
yearly_thread_users = with(forum_data, getFreq(
  list(Year, ThreadID, AuthorID),
  c("Year", "ThreadID", "AuthorID")))
yearly_thread_users = yearly_thread_users[
  yearly_thread_users$Freq>1, ]

set.seed(28390121)
# sample 3 threads from yearly_thread_users
sample_threads = sample(
  yearly_thread_users[duplicated(
      yearly_thread_users$ThreadID), ]$ThreadID, 3)

# get the 3 threads' users in each year
yearly_thread_users = yearly_thread_users[
  yearly_thread_users$ThreadID %in%
    sample_threads, ]
# order them by thread ID so edges are added to
# users in the same thread only
yearly_thread_users = yearly_thread_users[
  order(yearly_thread_users$ThreadID), ]

# get the thread and users in 2007
thread_users_2007 = yearly_thread_users[
  yearly_thread_users$Year=="2007", ]
# get the unique users in thread_users_2007
# and order them so the author ID are arranged in 
# the same order in the adjacent matrix. then 
# the position of each author ID corresponds
# to its position in the adjacent matrix
users = unique((thread_users_2007[
  order(thread_users_2007$AuthorID), ])$AuthorID)
total_users = length(users)
adj_Mat = matrix(0L, nrow=total_users,
                 ncol=total_users)
adj_Mat = makeAdjMat(
  adj_Mat,
  thread_users_2007$ThreadID,
  thread_users_2007$AuthorID)

net_2007 = network(adj_Mat, matrix.type="adjacency")
ggnet2(net_2007, size="degree", label=users) + 
  ggtitle("Social Network of Year 2007")

# get the thread and users in 2008
thread_users_2008 = yearly_thread_users[
  yearly_thread_users$Year=="2008", ]
# get the unique users in thread_users_2008
# and order them so the author ID are arranged in 
# the same order in the adjacent matrix. then 
# the position of each author ID corresponds
# to its position in the adjacent matrix
users = unique((thread_users_2008[
  order(thread_users_2008$AuthorID), ])$AuthorID)
total_users = length(users)
adj_Mat = matrix(0L, nrow=total_users,
                 ncol=total_users)
adj_Mat = makeAdjMat(
  adj_Mat, 
  thread_users_2008$ThreadID, 
  thread_users_2008$AuthorID)

net_2008 = network(adj_Mat, matrix.type="adjacency")
ggnet2(net_2008, size="degree", label=users) + 
  ggtitle("Social Network of Year 2008")

#####