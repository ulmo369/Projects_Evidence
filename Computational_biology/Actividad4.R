setwd("C:/Users/LENOVO/Documents/UNIVERSIDAD/SEGUNDO/biología computacional/Actividad 4")

BiocManager::install("GO.db")
BiocManager::install("annotate")
BiocManager::install("org.Hs.eg.db")
BiocManager::install("hugene20stprobeset.db")
BiocManager::install("hugene20sttranscriptcluster.db")
BiocManager::install("affy")
BiocManager::install("gplots")

library(GO.db)
library(annotate)
library(org.Hs.eg.db)
library(hugene20stprobeset.db)
library(hugene20sttranscriptcluster.db)
annDB ="hugene20sttranscriptcluster.db"
NoTranscripts = 53618
library(affy)
library(gplots)
library(limma)

CoCaData =read.csv(file="Actividad4.csv", header=TRUE)
dim(CoCaData)
CoCaData[1:10,1:5]

probenames<-as.character(CoCaData$ID_REF)
entID<-getEG(probenames,annDB)
sym<-getSYMBOL(probenames,annDB)
geneExpData<-data.frame(sym, CoCaData)
indx.NAs =!is.na(geneExpData$sym)
geneExpData = geneExpData[indx.NAs,]
dim(geneExpData)
geneExpData[1:11,1:5]

datosColon =as.matrix(geneExpData[,3:86])
rownames(datosColon) = geneExpData$sym
datosColon[1:5,1:5]

etiquetas =read.csv(file="DetalleMuestrasCoca.csv", header=TRUE)
colnames(datosColon) =as.character(etiquetas$Etiqueta)
indx=c(which(substring(etiquetas$Etiqueta,1,6) =="Normal"),
       which(substring(etiquetas$Etiqueta,1,6) =="TumorP"),
       which(substring(etiquetas$Etiqueta,1,3) =="T2D"),
       which(substring(etiquetas$Etiqueta,1,8) =="TumorT2D"))
datosColon = datosColon[,indx]

datosColon[1:5,1:5]
colnames(datosColon)

colores =c(rep("lightgray", 19),rep("steelblue",19),
           rep("orange",23),rep("indianred",23))
plotDensity(datosColon,col=colores, main ="DatosNormalizados",
            xlab ="ExpressionLevels")
par(mar=c(7,4,4,4))
boxplot(datosColon,col=colores, main ="DatosNormalizados",
        las =2, ylab ="Expression", cex.axis=.8, pch=".")

#Identificando los genes diferencial mente expresados
#-----------------------------------------------------------
#initializevariables
pv = 2
M = 0.3

#designmatrix
smpls = 84
gps = 4

design =matrix(rep(0,gps*smpls),nrow=smpls)
colnames(design) =c("Normal","CoCa","T2D","CoCaT2D")
design[1:19, 1]=1
design[20:38,2]=1
design[39:61,3]=1
design[62:84,4]=1

#contrastmatrix
cont.matrix= makeContrasts("CoCa-Normal","CoCaT2D-T2D","CoCaT2D-CoCa","T2D-Normal",levels=design)

#linearmodelfit
fit = lmFit(datosColon,design)
fitC =contrasts.fit(fit, cont.matrix)
fitCB = eBayes(fitC)

#resultados
#resultados

TT = topTable(fitCB,coef="CoCaT2D-T2D", adjust ="fdr",sort.by="logFC",
              number=NoTranscripts, genelist=fit$genes)
genesDifExp = TT[(-log10(TT$P.Value)>pv&abs(TT$logFC)>M),]
dim(genesDifExp)
Up.regulated =sum(genesDifExp$logFC>M)
Dw.regulated =sum(genesDifExp$logFC<=M)
head(genesDifExp)
#------------------------------------------------
#Esta parte del código es para poder generar un documento y buscar en DAVID
install.packages("openxlsx")
library(openxlsx)
lista1 <- genesDifExp[, c("ID")]
View(lista1)
write.xlsx(lista1, file = "lista1.xlsx")
#------------------------------------------------

TT = topTable(fitCB,coef="CoCaT2D-CoCa", adjust ="fdr",sort.by="logFC",
              number=NoTranscripts, genelist=fit$genes)
genesDifExp = TT[(-log10(TT$P.Value)>pv&abs(TT$logFC)>M),]
dim(genesDifExp)
Up.regulated =sum(genesDifExp$logFC>M)
Dw.regulated =sum(genesDifExp$logFC<=M)
head(genesDifExp)
#------------------------------------------------
#Esta parte del código es para poder generar un documento y buscar en DAVID
lista2 <- genesDifExp[, c("ID")]
View(lista2)
write.xlsx(lista2, file = "listaCoCaT2D-Normal.xlsx")
#------------------------------------------------


#volcanoplot(fitCB,col="black",coef=1)
volcanoplot(fitCB,coef="CoCa-Normal", main ="Contraste CoCa vs Normal")
volcanoplot(fitCB,coef="CoCaT2D-CoCa",col="red", main ="Contraste CoCaT2D vs CoCa")
volcanoplot(fitCB,coef="CoCaT2D-T2D",col="blue", main ="Contraste CoCaT2D vs T2D")

genelabels = genesDifExp$ID
datos.cluster = datosColon[as.numeric(rownames(genesDifExp)),1:38]
par(oma =c(3,1,3,4),mar=c(14,5,2,2)+0.1)
ind.hmap = heatmap.2(datos.cluster,col=greenred(75),scale="row",
                     key=TRUE, symkey=FALSE,density.info="none",trace="none",
                     cexRow=.55, cexCol=.7, main ="CoCavsNormal", labRow =
                       genelabels, ColSideColors=colores[1:38])


# First look at the results in B&W to determine the axes limits 
# to avoid misplacing the labels every time I overwrite colors

volcanoplot(fitCB, coef=i)


# These are vectors of as many entries as nC update the values
# according to the limits you observe in the black and white plots
# x0 and x1 are the limits of the x-axis "log fold-change" or M
# y0 and y1 are the limits of the y-axis log-odds "B" statistic

y0= -10
y1= 30
x0= -5
x1= 3

# Next, I set the values of the B statistic (B) and the log fold-change
# which I call M here. There is also another variable "contrasts"
# This is the vector of labels for each contrast "this vs that"
# ind1 --4 are the indices for the four colors (green, red, magenta and orange)

M=1
B=0

volcanoplot(fitCB, coef=1, col="blue", ylim=c(y0,y1), xlim=c(x0,x1), main="Exp. Dif. de ", cex.lab=1.3, ylab="B")
par(new=T)
abline(v=-M, col="brown", ylab="", xlab="")
par(new=T)
abline(v=M, col="brown", ylab="", xlab="")
par(new=T)
abline(h=B, col="black", ylab="", xlab="")
par(new=T)
ind1 = abs(fitCB$coef)>M
ind2 = fitCB$lods >B
ind3 = (fitCB$coef>M & fitCB$lods>B)
ind4 = (fitCB$coef< -M & fitCB$lods>B)
x = as.matrix(fitCB$coef[ind1])
y = as.matrix(fitCB$lods[ind1])
plot(x, y, col="magenta",ylim=c(y0,y1), xlim=c(x0,x1),main="", pch = "*",xlab="", ylab="",cex.lab=1.2)
x = as.matrix(fitCB$coef[ind2])
y = as.matrix(fitCB$lods[ind2])
par(new=T)
plot(x, y, col="orange",  ylim=c(y0,y1), xlim=c(x0,x1), main="", pch = 20,xlab="", ylab="",cex.lab=1.2)
x = as.matrix(fitCB$coef[ind3])
y = as.matrix(fitCB$lods[ind3])
par(new=T)
plot(x, y, col="red",  ylim=c(y0,y1), xlim=c(x0,x1), main="", pch = 20,xlab="", ylab="",cex.lab=1.2)
x = as.matrix(fitCB$coef[ind4])
y = as.matrix(fitCB$lods[ind4])
par(new=T)
plot(x, y, col="darkgreen", ylim=c(y0,y1), xlim=c(x0,x1), main="", pch = 20,xlab="", ylab="",cex.lab=1.2)
2
