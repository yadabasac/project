
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;
proc means;run;


/* ******************** */
/*Create stock prices */
/* ******************** */

data a2; set a1;
keep gvkey2 nyear che at sale seq prcc_c;run;
proc means;run;

data tmp1.m_stockprice; set a2;run;
