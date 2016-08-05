# Codings filename
#filename = "/home/tico/git/rqda-to-gephi/2 - Skill_open,Skill_closed -  - Goals,Emotion,Effect,Imagery,Time - /codings2_doubled.csv"
filename = "../python/2-Skill_open,Skill_closed--Goals,Emotion,Effect,Imagery,Time-/codings2.csv"

# List of the columns that refers to the filenames that are in the table
#filename_columns <- c("Skill_closed", "Skill_open","Skill_closed2", "Skill_open2")
filename_columns <- c("Skill_closed", "Skill_open")


# select the bar colors (red, blue, gray1-100)
#bar_colors <- c("gray25","gray50","gray75","gray100")
bar_colors <- c("white","gray")


# select the codes that are interesting
select_codes = c( 
    # 1st code
    "imagery_concrete|imagery_abstract", 
    # 2nd code
    "time_competition_before_action|time_competition_in_action|time_before_competition"
)


# open the file
codings2 <- read.table(filename, header=TRUE, sep=",", na.strings="NA", dec=".", strip.white=TRUE)

# create a new column with the names of the filename columns
for (fc in filename_columns) {
    codings2$type[codings2[,fc] == 1] <- fc
}

sum_codings2 <- data.frame(matrix(vector(), 0, 4, dimnames=list(c(), c("filename", "type", "codename_1", "codename_2"))), stringsAsFactors=F)
for (fc in filename_columns) {
    temp <- data.frame(subset(codings2, codings2[,fc] == 1 ))
    temp$filename <- factor(temp$filename)
    temp <- as.data.frame(with(temp, table(filename, type, codename_1, codename_2)))
    sum_codings2 <- rbind(sum_codings2,temp)
}

# add codes column (assumes that the codes include the category names separated by _. For example, emotion_codename,
# where emotion is a category and codename the code name). This just allow to present the data in alphabetical order
# in the graphs
sum_codings2$codes <- pmin( 
    paste(sum_codings2$codename_1,sum_codings2$codename_2,sep="-"), 
    paste(sum_codings2$codename_2,sum_codings2$codename_1,sep="-"))

subset(sum_codings2, grepl("imagery_concrete|imagery_abstract", sum_codings2$codes))
"imagery_concrete|imagery_abstract"
for (cod in select_codes) {
    sum_codings2 <- subset(sum_codings2, grepl(cod, sum_codings2$codes))
}


# refactor in order to have the correct levels
sum_codings2$codes <- factor(sum_codings2$codes)
sum_codings2$type <- factor(sum_codings2$type)

# eliminate duplicated columns that have 0s in them, this is related with the 
# pmin function above that could introduce exactly the same rows
sum_codings2 <- aggregate(
    list(Freq = sum_codings2$Freq), 
    by=list(filename=sum_codings2$filename, 
            type=sum_codings2$type, 
            codes=sum_codings2$codes), 
    FUN=sum)

# Apply the Anova, and disply means, sd and frequencies
AnovaModel.1 <- (lm(Freq ~ codes*type, data=sum_codings2))
Anova(AnovaModel.1)
tapply(sum_codings2$Freq, list(codes=sum_codings2$codes, type=sum_codings2$type), mean, na.rm=TRUE) # means
tapply(sum_codings2$Freq, list(codes=sum_codings2$codes, type=sum_codings2$type), sd, na.rm=TRUE) # std. deviations
tapply(sum_codings2$Freq, list(codes=sum_codings2$codes, type=sum_codings2$type), function(x) sum(!is.na(x))) # counts

# Repeated Measures Anova
aov.out = aov(Freq ~ type * codes + Error(filename/codes), data=sum_codings2)
summary(aov.out)

# store the means in tabcodes, and create a dataframe 
tabcodes <- tapply(sum_codings2$Freq, list(codes=sum_codings2$codes, type=sum_codings2$type), mean, na.rm=TRUE)
datacodes <- data.frame(tabcodes)


sort_by = filename_columns[1]
# get the order of the frequencies from less to more of the closed type
desc_order <- order(datacodes[,sort_by], decreasing=TRUE)
# sort the data codes framewor
datacodes_order <- datacodes[desc_order,]
# remove the ones with no ocurrences
datacodes <- subset(datacodes_order, datacodes_order[,sort_by] > 0)
# transpose the data
dcodes<-t(as.matrix(datacodes[,1:ncol(datacodes)]))

# Calculate the st error manually
tab_stderr <- tapply(sum_codings2$Freq, list(codes=sum_codings2$codes, type=sum_codings2$type), function(x) sd(x)/sqrt(length(x))) # st error
# Create the data frame
data_stderr <- data.frame(tab_stderr)
# Follow the order of the averates
data_stderr <- data_stderr[desc_order, ]
# Removes those rows that have no frequencies
data_stderr <- subset(data_stderr, datacodes_order[,sort_by] > 0)
# Transpose the data
dstderr<-t(as.matrix(data_stderr[,1:ncol(data_stderr)]))


plot.new()
width <- max(strwidth(colnames(dcodes), units = "inches", cex=4.5))
par(mar = c(4, width, 2, 2) + 0.2, cex.axis=0.8) #add room for the rotated labels
y<-barplot(dcodes, beside=TRUE,
        legend.text=rownames(dcodes), horiz=TRUE,
        args.legend=list(bty="n",horiz=FALSE),
        col=bar_colors,
        border="black",
        xlim=c(0,ceiling(max(dcodes+dstderr))),
        xlab="",
        main="",las=2)

box(bty="l")
arrows(x0=dcodes-dstderr,
       y0=y,
       x1=dcodes+dstderr,
       y1=y,
       angle=90,
       code=3,
       length=0.04,
       lwd=1)


