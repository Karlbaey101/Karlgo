\# 8. LeetCode584-寻找用户推荐人

\# 题面描述：https://leetcode.cn/problems/find-customer-referee/description/

```mysql
SELECT name
FROM customer
WHERE referee_Id != 2
   OR referee_Id IS NULL
```

\# 9. LeetCode1757-可回收且低脂的产品

\# 题面描述：https://leetcode.cn/problems/recyclable-and-low-fat-products/description/

```mysql
SELECT product_id
FROM Products AS pr
WHERE pr.low_fats = 'Y' 
  AND pr.recyclable = 'Y';
```

