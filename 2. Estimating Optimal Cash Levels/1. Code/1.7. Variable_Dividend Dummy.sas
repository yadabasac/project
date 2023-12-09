
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;

/* ******************** */
/*Create Dividend Dummy*/
/* ******************** */

data a2; set a1;
if missing(dvc) then dvc=0;
keep gvkey2 nyear dvc;
proc sort; by gvkey2 nyear;run;

data a3; set a2;
by gvkey2;
first = first.gvkey2; 
prev_dvc= lag(dvc);
if first = 1 then prev_dvc = 0;
run;

data a4; set a3;
if missing(prev_dvc) then prev_dvc =0;
dvc2 = 0;
if prev_dvc > 0 then dvc2 = 1;
if prev_dvc <= 0 then dvc2 = 0;
keep gvkey2 nyear dvc2;
proc means;run;

data tmp1.m_dividend; set a4;run;
