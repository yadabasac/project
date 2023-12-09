
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;


/* ******************** */
/*Create Cash From Operation */
/* ******************** */

data a2; set a1;
if not missing(oancf);
if not missing(che);
if not missing(at);
keep gvkey2 nyear oancf at che;
proc means; run;

data a3; set a2;
if (at-che) ne 0;
cashop=oancf/(at-che);
if cashop ne ".";run;

data a4; set a3;
keep gvkey2 nyear cashop;
proc means; run;

data tmp1.m_cashop; set a4;run;
