SELECT ws.Team, FIFA_Ranking, Is_Local_Coach, SUM(Caps) Total_Caps, SUM(Goals) AS Total_Goals, ROUND (AVG(age),2) AS Average_age
FROM wc_squad ws
JOIN wc_ranking wr
ON ws.Team = wr.Team
JOIN coach_analysis ca
ON wr.Team = ca.Team
GROUP BY ws.Team, FIFA_Ranking, Is_Local_Coach
ORDER BY FIFA_Ranking ;
