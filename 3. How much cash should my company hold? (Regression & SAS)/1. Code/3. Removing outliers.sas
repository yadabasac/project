
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

/* ******************** */
/*Removing Outliers*/
/* ******************** */

data a1; set tmp1.m_cashestimation_merge;
if not missing(che2);
if not missing(size);
if not missing(nwc);
if not missing(capx2);
if not missing(sic2);
if not missing(sigmacash);
if not missing(xrd2);
if not missing(dvc2);
if not missing(salesgrowth);
if not missing(cashop);
if not missing(firmage);
if not missing(tax_b);
if not missing(dma);
proc sort; by nyear; run;
proc means; run;

/*proc univariate; run;*/

proc means data=a1 p1 p99;
var che2 size nwc capx2 sigmacash xrd2 salesgrowth cashop firmage tax_b;
by nyear;
output out=winbreak1 p1=che2p1 sizep1 nwcp1 capx2p1 sigmacashp1 xrd2p1 salesgrowthp1 cashopp1 firmagep1 tax_bp1
p99=che2p99 sizep99 nwcp99 capx2p99 sigmacashp99 xrd2p99 salesgrowthp99 cashopp99 firmagep99 tax_bp99;
run;

data a2; set winbreak1;
proc sort; by nyear; run;


data a3;
merge a1 a2;
by nyear;run;

data a4; set a3;run;

data a5; set a4;
if che2<che2p1 then che2 = che2p1;
if che2>che2p99 then che2 = che2p99;
if size<sizep1 then size = sizep1;
if size>sizep99 then size = sizep99;
if nwc<nwcp1 then nwc = nwcp1;
if nwc>nwcp99 then nwc = nwcp99;
if capx2<capx2p1 then capx2 = capx2p1;
if capx2>capx2p99 then capx2 = capx2p99;
if sigmacash<sigmacashp1 then sigmacash = sigmacashp1;
if sigmacash>sigmacashp99 then sigmacash = sigmacashp99;
if xrd2<xrd2p1 then xrd2 = xrd2p1;
if xrd2>xrd2p99 then xrd2 = xrd2p99;
if salesgrowth<salesgrowthp1 then salesgrowth = salesgrowthp1;
if salesgrowth>salesgrowthp99 then salesgrowth = salesgrowthp99;
if cashop<cashopp1 then cashop = cashopp1;
if cashop>cashopp99 then cashop = cashopp99;
if firmage<firmagep1 then firmage = firmagep1;
if firmage>firmagep99 then firmage = firmagep99;
if tax_b<tax_bp1 then tax_b = tax_bp1;
if tax_b>tax_bp99 then tax_b = tax_bp99;

drop _type_ _freq_ salesgrowthp1 che2p1 sizep1 cashopp1 nwcp1 capx2p1 sigmacashp1 xrd2p1 firmagep1 tax_bp1
salesgrowthp99 che2p99 sizep99 cashopp99 nwcp99 capx2p99 sigmacashp99 xrd2p99 firmagep99 tax_bp99;run;

data a6; set a5;
proc means; run;

data a7; set a6;
if nyear=1988 then y1988=1; else y1988=0;
if nyear=1989 then y1989=1; else y1989=0;
if nyear=1990 then y1990=1; else y1990=0;
if nyear=1991 then y1991=1; else y1991=0;
if nyear=1992 then y1992=1; else y1992=0;
if nyear=1993 then y1993=1; else y1993=0;
if nyear=1994 then y1994=1; else y1994=0;
if nyear=1995 then y1995=1; else y1995=0;
if nyear=1996 then y1996=1; else y1996=0;
if nyear=1997 then y1997=1; else y1997=0;
if nyear=1998 then y1998=1; else y1998=0;
if nyear=1999 then y1999=1; else y1999=0;
if nyear=2000 then y2000=1; else y2000=0;
if nyear=2001 then y2001=1; else y2001=0;
if nyear=2002 then y2002=1; else y2002=0;
if nyear=2003 then y2003=1; else y2003=0;
if nyear=2004 then y2004=1; else y2004=0;
if nyear=2005 then y2005=1; else y2005=0;
if nyear=2006 then y2006=1; else y2006=0;
if nyear=2007 then y2007=1; else y2007=0;
if nyear=2008 then y2008=1; else y2008=0;
if nyear=2009 then y2009=1; else y2009=0;
if nyear=2010 then y2010=1; else y2010=0;
if nyear=2011 then y2011=1; else y2011=0;
if nyear=2012 then y2012=1; else y2012=0;
if nyear=2013 then y2013=1; else y2013=0;
if nyear=2014 then y2014=1; else y2014=0;
if nyear=2015 then y2015=1; else y2015=0;
if nyear=2016 then y2016=1; else y2016=0;
if nyear=2017 then y2017=1; else y2017=0;
if nyear=2018 then y2018=1; else y2018=0;
if nyear=2019 then y2019=1; else y2019=0;
if nyear=2020 then y2020=1; else y2020=0;
if nyear=2021 then y2021=1; else y2021=0;
if nyear=2022 then y2022=1; else y2022=0;
run;

/*PROC FREQ DATA=a7;*/
/*  TABLES sic2 / OUT=frequency_table;*/
/*RUN;*/

data a8; set a7;
proc sort; by sic2;run;

data a9; set a8;
if sic2=2 then nsic2=1; else nsic2=0;
if sic2=7 then nsic7=1; else nsic7=0;
if sic2=8 then nsic8=1; else nsic8=0;
if sic2=9 then nsic9=1; else nsic9=0;
if sic2=10 then nsic10=1; else nsic10=0;
if sic2=12 then nsic12=1; else nsic12=0;
if sic2=13 then nsic13=1; else nsic13=0;
if sic2=14 then nsic14=1; else nsic14=0;
if sic2=15 then nsic15=1; else nsic15=0;
if sic2=16 then nsic16=1; else nsic16=0;
if sic2=17 then nsic17=1; else nsic17=0;
if sic2=20 then nsic20=1; else nsic20=0;
if sic2=21 then nsic21=1; else nsic21=0;
if sic2=22 then nsic22=1; else nsic22=0;
if sic2=23 then nsic23=1; else nsic23=0;
if sic2=24 then nsic24=1; else nsic24=0;
if sic2=25 then nsic25=1; else nsic25=0;
if sic2=26 then nsic26=1; else nsic26=0;
if sic2=27 then nsic27=1; else nsic27=0;
if sic2=28 then nsic28=1; else nsic28=0;
if sic2=29 then nsic29=1; else nsic29=0;
if sic2=30 then nsic30=1; else nsic30=0;
if sic2=31 then nsic31=1; else nsic31=0;
if sic2=32 then nsic32=1; else nsic32=0;
if sic2=33 then nsic33=1; else nsic33=0;
if sic2=34 then nsic34=1; else nsic34=0;
if sic2=35 then nsic35=1; else nsic35=0;
if sic2=36 then nsic36=1; else nsic36=0;
if sic2=37 then nsic37=1; else nsic37=0;
if sic2=38 then nsic38=1; else nsic38=0;
if sic2=39 then nsic39=1; else nsic39=0;
if sic2=40 then nsic40=1; else nsic40=0;
if sic2=41 then nsic41=1; else nsic41=0;
if sic2=42 then nsic42=1; else nsic42=0;
if sic2=44 then nsic44=1; else nsic44=0;
if sic2=45 then nsic45=1; else nsic45=0;
if sic2=46 then nsic46=1; else nsic46=0;
if sic2=47 then nsic47=1; else nsic47=0;
if sic2=48 then nsic48=1; else nsic48=0;
if sic2=49 then nsic49=1; else nsic49=0;
if sic2=50 then nsic50=1; else nsic50=0;
if sic2=51 then nsic51=1; else nsic51=0;
if sic2=52 then nsic52=1; else nsic52=0;
if sic2=53 then nsic53=1; else nsic53=0;
if sic2=54 then nsic54=1; else nsic54=0;
if sic2=55 then nsic55=1; else nsic55=0;
if sic2=56 then nsic56=1; else nsic56=0;
if sic2=57 then nsic57=1; else nsic57=0;
if sic2=58 then nsic58=1; else nsic58=0;
if sic2=59 then nsic59=1; else nsic59=0;
if sic2=60 then nsic60=1; else nsic60=0;
if sic2=61 then nsic61=1; else nsic61=0;
if sic2=62 then nsic62=1; else nsic62=0;
if sic2=63 then nsic63=1; else nsic63=0;
if sic2=64 then nsic64=1; else nsic64=0;
if sic2=65 then nsic65=1; else nsic65=0;
if sic2=67 then nsic67=1; else nsic67=0;
if sic2=70 then nsic70=1; else nsic70=0;
if sic2=72 then nsic72=1; else nsic72=0;
if sic2=73 then nsic73=1; else nsic73=0;
if sic2=75 then nsic75=1; else nsic75=0;
if sic2=76 then nsic76=1; else nsic76=0;
if sic2=78 then nsic78=1; else nsic78=0;
if sic2=79 then nsic79=1; else nsic79=0;
if sic2=80 then nsic80=1; else nsic80=0;
if sic2=81 then nsic81=1; else nsic81=0;
if sic2=82 then nsic82=1; else nsic82=0;
if sic2=83 then nsic83=1; else nsic83=0;
if sic2=86 then nsic86=1; else nsic86=0;
if sic2=87 then nsic87=1; else nsic87=0;
if sic2=89 then nsic89=1; else nsic89=0;
if sic2=99 then nsic99=1; else nsic99=0;
run;

data a10; set a9;
proc sort; by gvkey2 nyear;

data tmp1.m_cashestimation_outliers; set a10;
proc means;run;


