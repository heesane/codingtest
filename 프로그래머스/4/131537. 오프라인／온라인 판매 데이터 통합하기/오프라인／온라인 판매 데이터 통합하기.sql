-- 코드를 입력하세요
SELECT 
date_format(sales_date,"%Y-%m-%d") as SALES_DATE,
product_id as PRODUCT_ID,
NULL as USER_ID,
sales_amount as SALES_AMOUNT
from offline_sale
where month(SALES_DATE) = 3

union all

SELECT
date_format(sales_date,"%Y-%m-%d") as SALES_DATE,
product_id as PRODUCT_ID,
USER_ID,
sales_amount as SALES_AMOUNT
from online_sale
where month(SALES_DATE) = 3
order by sales_date asc,product_id asc,user_id asc