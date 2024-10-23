
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;


/* ******************** */
/*Create sales growth */
/* ******************** */

data a2; set a1;
if not missing(sale);
keep gvkey2 sale nyear ;
proc sort; by gvkey2 nyear;run;

data a3; set a2;
by gvkey2;
first = first.gvkey2; 
prev_sale= lag(sale);
if first = 1 then prev_sale = 0;
run;

data a4; set a3;
if prev_sale ne '.';
if prev_sale ne 0;
salesgrowth = (sale-prev_sale)/prev_sale;
if salesgrowth ne '.';
keep gvkey2 nyear salesgrowth;
proc means; run;

data tmp1.m_salesgrowth; set a4;run;
