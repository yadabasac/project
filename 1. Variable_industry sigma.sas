/*libname tmp1 '/home/u63644257/Data';*/
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
if oibdp ="." then delete;
if xint ="." then xint=0;
if txt ="." then txt=0;
if dvc ="." then dvc=0;
if che ="." then delete;
if at="." then delete;
if (at-che)=0 then delete;
gvkey2=gvkey*1;
nyear = year(datadate);run;

data a2; set a1;
drop consol indfmt datafmt popsrc curcd costat;run;

data a3; set a2;
cashflow=(oibdp-xint-txt-dvc)/(at-che);
sic2 =int(sic/100);run;


/************************/
/*1987*/
/************************/

data a4; set a3;
if (1987-20) <= nyear<= (1987-1);run;

proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1987;run;

data tmp1.sigma1987; set a6; run;

/************************/
/*1988*/
/************************/

data a4; set a3;
if (1988-20) <= nyear<= (1988-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1988;run;

data tmp1.sigma1988; set a6; 
proc means; run;

/************************/
/*1989*/
/************************/

data a4; set a3;
if (1989-20) <= nyear<= (1989-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1989;run;

data tmp1.sigma1989; set a6; proc means; run;

/************************/
/*1990*/
/************************/

data a4; set a3;
if (1990-20) <= nyear<= (1990-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1990;run;

data tmp1.sigma1990; set a6; proc means; run;

/************************/
/*1991*/
/************************/

data a4; set a3;
if (1991-20) <= nyear<= (1991-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1991;run;

data tmp1.sigma1991; set a6; proc means; run;

/************************/
/*1992*/
/************************/

data a4; set a3;
if (1992-20) <= nyear<= (1992-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1992;run;

data tmp1.sigma1992; set a6; proc means; run;

/************************/
/*1993*/
/************************/

data a4; set a3;
if (1993-20) <= nyear<= (1993-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1993;run;

data tmp1.sigma1993; set a6; proc means; run;

/************************/
/*1994*/
/************************/

data a4; set a3;
if (1994-20) <= nyear<= (1994-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1994;run;

data tmp1.sigma1994; set a6; proc means; run;

/************************/
/*1995*/
/************************/

data a4; set a3;
if (1995-20) <= nyear<= (1995-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1995;run;

data tmp1.sigma1995; set a6; proc means; run;

/************************/
/*1996*/
/************************/

data a4; set a3;
if (1996-20) <= nyear<= (1996-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1996;run;

data tmp1.sigma1996; set a6; proc means; run;

/************************/
/*1997*/
/************************/

data a4; set a3;
if (1997-20) <= nyear<= (1997-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1997;run;

data tmp1.sigma1997; set a6; proc means; run;

/************************/
/*1998*/
/************************/

data a4; set a3;
if (1998-20) <= nyear<= (1998-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1998;run;

data tmp1.sigma1998; set a6; proc means; run;

/************************/
/*1999*/
/************************/

data a4; set a3;
if (1999-20) <= nyear<= (1999-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 1999;run;

data tmp1.sigma1999; set a6; proc means; run;

/************************/
/*2000*/
/************************/

data a4; set a3;
if (2000-20) <= nyear<= (2000-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2000;run;

data tmp1.sigma2000; set a6; proc means; run;

/************************/
/*2001*/
/************************/

data a4; set a3;
if (2001-20) <= nyear<= (2001-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2001;run;

data tmp1.sigma2001; set a6; proc means; run;

/************************/
/*2002*/
/************************/

data a4; set a3;
if (2002-20) <= nyear<= (2002-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2002;run;

data tmp1.sigma2002; set a6; proc means; run;

/************************/
/*2003*/
/************************/

data a4; set a3;
if (2003-20) <= nyear<= (2003-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2003;run;

data tmp1.sigma2003; set a6; proc means; run;

/************************/
/*2004*/
/************************/

data a4; set a3;
if (2004-20) <= nyear<= (2004-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2004;run;

data tmp1.sigma2004; set a6; proc means; run;

/************************/
/*2005*/
/************************/

data a4; set a3;
if (2005-20) <= nyear<= (2005-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2005;run;

data tmp1.sigma2005; set a6; proc means; run;

/************************/
/*2006*/
/************************/

data a4; set a3;
if (2006-20) <= nyear<= (2006-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2006;run;

data tmp1.sigma2006; set a6; proc means; run;

/************************/
/*2007*/
/************************/

data a4; set a3;
if (2007-20) <= nyear<= (2007-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2007;run;

data tmp1.sigma2007; set a6; proc means; run;

/************************/
/*2008*/
/************************/

data a4; set a3;
if (2008-20) <= nyear<= (2008-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2008;run;

data tmp1.sigma2008; set a6; proc means; run;

/************************/
/*2009*/
/************************/

data a4; set a3;
if (2009-20) <= nyear<= (2009-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2009;run;

data tmp1.sigma2009; set a6; proc means;  run;

/************************/
/*2010*/
/************************/

data a4; set a3;
if (2010-20) <= nyear<= (2010-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2010;run;

data tmp1.sigma2010; set a6; proc means; run;

/************************/
/*2011*/
/************************/

data a4; set a3;
if (2011-20) <= nyear<= (2011-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2011;run;

data tmp1.sigma2011; set a6; proc means; run;

/************************/
/*2012*/
/************************/

data a4; set a3;
if (2012-20) <= nyear<= (2012-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2012;run;

data tmp1.sigma2012; set a6; proc means;  run;

/************************/
/*2013*/
/************************/

data a4; set a3;
if (2013-20) <= nyear<= (2013-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2013;run;

data tmp1.sigma2013; set a6; proc means; run;

/************************/
/*2014*/
/************************/

data a4; set a3;
if (2014-20) <= nyear<= (2014-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2014;run;

data tmp1.sigma2014; set a6; proc means; run;

/************************/
/*2015*/
/************************/

data a4; set a3;
if (2015-20) <= nyear<= (2015-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2015;run;

data tmp1.sigma2015; set a6; proc means; run;

/************************/
/*2016*/
/************************/

data a4; set a3;
if (2016-20) <= nyear<= (2016-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2016;run;

data tmp1.sigma2016; set a6; proc means; run;

/************************/
/*2017*/
/************************/

data a4; set a3;
if (2017-20) <= nyear<= (2017-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2017;run;

data tmp1.sigma2017; set a6; proc means; run;

/************************/
/*2018*/
/************************/

data a4; set a3;
if (2018-20) <= nyear<= (2018-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2018;run;

data tmp1.sigma2018; set a6; proc means; run;

/************************/
/*2019*/
/************************/

data a4; set a3;
if (2019-20) <= nyear<= (2019-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2019;run;

data tmp1.sigma2019; set a6; proc means; run;

/************************/
/*2020*/
/************************/

data a4; set a3;
if (2020-20) <= nyear<= (2020-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2020;run;

data tmp1.sigma2020; set a6; proc means; run;

/************************/
/*2021*/
/************************/

data a4; set a3;
if (2021-20) <= nyear<= (2021-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2021;run;

data tmp1.sigma2021; set a6; proc means; run;

/************************/
/*2022*/
/************************/

data a4; set a3;
if (2022-20) <= nyear<= (2022-1);run;
proc sort data=a4; by sic2;run;

proc means noprint; var cashflow; by sic2; 
output out=cash std=sigmacash; by sic2;

data a5; set cash;
drop _type_ _FREQ_;run;

data a6; set a5;
nyear = 2022;run;

data tmp1.sigma2022; set a6; proc means; run;

/************************/
/*Merge industry sigma for all years*/
/************************/

data a7; set tmp1.sigma1987 tmp1.sigma1988 tmp1.sigma1989
tmp1.sigma1990 tmp1.sigma1991 tmp1.sigma1992 tmp1.sigma1993 tmp1.sigma1994
tmp1.sigma1995 tmp1.sigma1996 tmp1.sigma1997 tmp1.sigma1998 tmp1.sigma1999
tmp1.sigma2000 tmp1.sigma2001 tmp1.sigma2002 tmp1.sigma2003 tmp1.sigma2004
tmp1.sigma2005 tmp1.sigma2006 tmp1.sigma2007 tmp1.sigma2008 tmp1.sigma2009
tmp1.sigma2010 tmp1.sigma2011 tmp1.sigma2012 tmp1.sigma2013 tmp1.sigma2014
tmp1.sigma2015 tmp1.sigma2016 tmp1.sigma2017 tmp1.sigma2018 tmp1.sigma2019
tmp1.sigma2020 tmp1.sigma2021 tmp1.sigma2022;run;

data a8; set a7;
if not missing(sigmacash); run;

data tmp1.m_sigma1987_2022; set a8;
proc means; run; 

/************************/
/*Merge with original data to get gvkey2*/
/************************/

data a9; set tmp1.m_sigma1987_2022;run;
proc sort nodupkey; by sic2 nyear; run;

data a10; set a3;
if nyear >= 1987;
keep gvkey2 nyear sic2 ;
proc sort; by sic2 nyear; run;

data a11; merge a10 a9;
by sic2 nyear; 
proc means; run;

data a12; set a11;
if not missing(gvkey2);
if not missing(nyear);
if not missing(sic2);
if not missing(sigmacash); 
proc means;run;

data tmp1.m_ind_sig; set a12;run;
