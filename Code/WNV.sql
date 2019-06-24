SELECT
WNV.Year,
WNV.County,
RF.rainfall,
SUM(WNV.Positive_cases) AS TOTAL_CASES
FROM public.gbernal_wnv_human_cases WNV
LEFT JOIN PUBLIC.gbernal_la_avg_rain_fall RF ON  RF."﻿rain_year" = WNV.year
WHERE WNV.COUNTY='Los Angeles'

GROUP BY 
1,2,3