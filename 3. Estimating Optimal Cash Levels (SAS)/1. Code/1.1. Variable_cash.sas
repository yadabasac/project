
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;

/* ******************** */
/*Create Cash*/
/* ******************** */

data a2; set a1;
if not missing(at);
if not missing(che);
keep gvkey2 nyear at che; run;

data a3; set a2;
if (at-che)=0 then delete;
che2=che/(at-che);
if che2 ne ".";run;

data a4; set a3;
keep gvkey2 nyear che2;
proc means; run;

data tmp1.m_che2; set a4;run;

