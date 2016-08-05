library(car)

# Codings filename
filename = "../python/1-Skill_open,Skill_closed--Goals,Emotion,Effect,Imagery,Time-/codings1.csv"

# List of the columns that refers to the filenames that are in the table
filename_columns <- c("Skill_closed", "Skill_open")

# select the bar colors (red, blue, gray1-100)
#bar_colors <- c("gray25","gray50","gray75","gray100")
bar_colors <- c("white","gray")

# select the codes that are interesting
select_codes = c( 
    # 1st code
    "imagery_"
)


# open the file
codings1 <- read.table(filename, header=TRUE, sep=",", na.strings="NA", dec=".", strip.white=TRUE)

# create a new column with the names of the filename columns
for (fc in filename_columns) {
    codings1$type[codings1[,fc] == 1] <- fc
}

sum_codings1 <- data.frame(matrix(vector(), 0, 3, dimnames=list(c(), c("filename", "type", "codename_1"))), stringsAsFactors=F)
for (fc in filename_columns) {
    temp <- data.frame(subset(codings1, codings1[,fc] == 1 ))
    temp$filename <- factor(temp$filename)
    temp <- as.data.frame(with(temp, table(filename, type, codename_1)))
    sum_codings1 <- rbind(sum_codings1,temp)
}

# for one code, just put things on the right column
sum_codings1$codes <- sum_codings1$codename_1


for (cod in select_codes) {
    sum_codings1 <- subset(sum_codings1, grepl(cod, sum_codings1$codes))
}

# refactor in order to have the correct levels
sum_codings1$codes <- factor(sum_codings1$codes)
sum_codings1$type <- factor(sum_codings1$type)

# eliminate duplicated columns that have 0s in them, this is related with the 
# pmin function above that could introduce exactly the same rows
sum_codings1 <- aggregate(
    list(Freq = sum_codings1$Freq), 
    by=list(filename=sum_codings1$filename, 
            type=sum_codings1$type, 
            codes=sum_codings1$codes), 
    FUN=sum)


# Apply the Anova, and disply means, sd and frequencies
AnovaModel.1 <- (lm(Freq ~ type, data=sum_codings1))
Anova(AnovaModel.1)
tapply(sum_codings1$Freq, list(type=sum_codings1$type), mean, na.rm=TRUE) # means
tapply(sum_codings1$Freq, list(type=sum_codings1$type), sd, na.rm=TRUE) # std. deviations
tapply(sum_codings1$Freq, list(type=sum_codings1$type), function(x) sum(!is.na(x))) # counts


# store the means in tabcodes, and create a dataframe 
tabcodes <- tapply(sum_codings1$Freq, list(codes=sum_codings1$codes, type=sum_codings1$type), mean, na.rm=TRUE)
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
tab_stderr <- tapply(sum_codings1$Freq, list(codes=sum_codings1$codes, type=sum_codings1$type), function(x) sd(x)/sqrt(length(x))) # st error
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
