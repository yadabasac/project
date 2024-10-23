
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;


/* ******************** */
/*Create Capital Expenditures*/
/* ******************** */

data a2; set a1;
if not missing(capx);
if not missing(che);
if not missing(at);
keep gvkey2 nyear capx at che;run;


data a3; set a2;
if (at-che) ne 0;
capx2=capx/(at-che);
if capx2 ne ".";run;

data a4; set a3;
keep gvkey2 nyear capx2;
proc means; run;

data tmp1.m_capx; set a4;run;
