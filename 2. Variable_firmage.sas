/*libname tmp1 '/home/u63644257/Data';*/
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;


/* ******************** */
/*9. Create Firm Year*/
/* ******************** */

data a1; set tmp1.r_all;
proc means;run;

data a2; set a1;
if at = '.' then delete;
gvkey2 = gvkey*1;
nyear = year(datadate);
proc sort nodupkey; by gvkey2 nyear;run;

data a3; set a2;
drop consol indfmt datafmt popsrc curcd costat tic fyear datadate;run;

data a4; set a3;
proc sort; by gvkey2 nyear;run;

data a5; set a4;
by gvkey2;
first = first.gvkey2; run;

data a6; set a5;
if first=1;
if first=1 then firstyear=nyear;
keep gvkey2 firstyear;run;

data a7;
merge a4 a6;
by gvkey2;run;

data a8; set a7;
firmage = log(nyear - firstyear +1);
keep gvkey2 nyear firmage; run;

data a9; set a8;
proc means; run;

data tmp1.m_firmage; set a9;run;


