SELECT USER_ID, PRODUCT_ID
FROM online_sale
group by user_id,product_id
having count(user_id) >1
ORDER BY USER_ID ASC, PRODUCT_ID DESC;

