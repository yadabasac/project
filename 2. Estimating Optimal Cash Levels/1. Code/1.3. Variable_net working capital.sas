
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;


/* ******************** */
/*Create Net Working Capital*/
/* ******************** */

data a2; set a1;
if not missing(act);
if not missing(lct);
if not missing(at);
if not missing(che);
keep gvkey2 nyear act lct at che;run;

data a3; set a2;
if (at-che) ne 0;
nwc=(act-lct-che)/(at-che);
if nwc ne ".";run;

data a4; set a3;
keep gvkey2 nyear nwc;
proc means;run;

data tmp1.m_nwc; set a4;run;
