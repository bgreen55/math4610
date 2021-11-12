/* Final Project */

/* Import data */

FILENAME REFFILE '/home/u59332818/AmesHousing.csv';

PROC IMPORT DATAFILE=REFFILE
	DBMS=CSV
	OUT=homesData
	replace;
	GETNAMES=YES;
run;


/************************************************
choose qualitative varaibles 
************************************************/

/* qualitative variables we are using */
/*  heating CentralAir  KitchenQuality */

/* make dummy variables for Heating */
data homesData; set homesData;
	if Heating="Floor" then floor=1; else floor=0;
	if Heating="GasA" then gasA=1; else gasA=0;
	if Heating="GasW" then gasW=1; else gasW=0;
	if Heating="Grav" then grav=1; else grav=0;
	if Heating="OthW" then othW=1; else othW=0;
	/* wall furnace heating is base */
run;

/* dummy varaibales for CentralAir */
data homesData; set homesData;
	if CentralAir="Y" then airCondition=1;
	if CentralAir="N" then airCondition=0;
run;

/* dummy variables for KitchenQuality */
data homesData; set homesData;
	if KitchenQual="Ex" then KitExcellent=1; else KitExcellent=0;
	if KitchenQual="Gd" then KitGood=1; else KitGood=0;
	if KitchenQual="TA" then KitAvg=1; else KitAvg=0;
	if KitchenQual="Fa" then KitFair=1; else KitFair=0;
	/* Kit Poor is 0 in all 4 */
run;

/* This removes the qualitative variables that we aren't using from data set */
data homesData (drop=HouseStyle GarageType BsmtExposure BsmtCond BsmtQual Foundation 
Exterior1st RoofMatl RoofStyle BldgType LotConfig LandContour LotShape Street); 
set homesData; 
run;


/* create interaction variable age, which is the age of the house */
data homesData; set homesData;
	age = yrSold - yearBuilt;
	ageRemodel = yrSold - yearRemodAdd;
	ID=order;
	if order=335 then SalePrice='.';
	if order=295 then SalePrice='.';
run;



/* run regression of model before any transformations */
proc reg data=homesData;
	model SalePrice = LotArea OverallQual OverallCond BsmtFinSF1 
	TotalBsmtSF LowQualFinSF GrLivArea BsmtFullBath
	BsmtHalfBath FullBath HalfBath BedroomAbvGr KitchenAbvGr TotRmsAbvGrd 
	Fireplaces GarageCars GarageArea WoodDeckSF OpenPorchSF floor gasA gasW grav
	othW airCondition KitExcellent KitGood KitAvg KitFair age ageRemodel;
	output out=out1 r=resid p=pred;
	title1 'SalePrice based on x variables';
run;



/* Histograms of the vairables */
proc univariate data=homesData noprint;
	histogram;
run;

/* the following variables are varaibles that should be transformed */
/* lotArea partially right skewed
year built is left skewed    
woodDeckSf right skewed
openPorchSf right skewed
salePrice right skewed    
age right skewed */




/* Scatterplots of the variables */
/* The plots are run three different times so plots are easier to see */
proc sgscatter data=homesData;
	plot SalePrice * (LotArea OverallQual OverallCond BsmtFinSF1 
	TotalBsmtSF LowQualFinSF GrLivArea BsmtFullBath BsmtHalfBath);
	title1 'Scatterplots of each X vs Y';
run;

proc sgscatter data=homesData;
	plot SalePrice * (FullBath HalfBath BedroomAbvGr KitchenAbvGr TotRmsAbvGrd 
	Fireplaces GarageCars GarageArea WoodDeckSF);
	title1 'Scatterplots of each X vs Y';
run;

proc sgscatter data=homesData;
	plot SalePrice * (OpenPorchSF floor gasA gasW grav
	othW airCondition KitExcellent);
	title1 'Scatterplots of each X vs Y';
run;

proc sgscatter data=homesData;
	plot SalePrice * (KitGood KitAvg KitFair age ageRemodel);
	title1 'Scatterplots of each X vs Y';
run;



/*******************************************************/
/*   TRANSFORM THE VARIABLES THAT NEED TRANSFORMING    */
/*******************************************************/


/* lotArea partially right skewed
year built is left skewed    
woodDeckSf right skewed
openPorchSf right skewed
salePrice right skewed    
age right skewed */

/* look at histograms of variables to see if more need transformation */


/********************************************/
/*   CHECK MULTICOLLINEARITY    */
/********************************************/







