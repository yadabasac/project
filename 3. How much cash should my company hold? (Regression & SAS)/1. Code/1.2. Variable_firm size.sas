libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;


/* ******************** */
/* Create Firm Size*/
/* ******************** */

data a2; set a1;
if not missing(at);
keep gvkey2 nyear at;run;

data a3; set a2;
if at ne 0;
size=log(at);
if size ne ".";run;

data a4; set a3;
keep gvkey2 nyear size;
proc means; run;

data tmp1.m_size; set a4;run;


