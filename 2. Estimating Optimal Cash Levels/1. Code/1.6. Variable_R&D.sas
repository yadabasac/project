
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;


/* ******************** */
/*Create Research and Development*/
/* ******************** */

data a2; set a1;
if missing(xrd) then xrd = 0;
keep gvkey2 nyear xrd at;run;

data a3; set a2;
if at ne 0;
xrd2=xrd/at;
if xrd2 ne ".";run;

data a4; set a3;
keep gvkey2 nyear xrd2;
proc means; run;

data tmp1.m_xrd; set a4;run;

