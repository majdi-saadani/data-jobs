- Demateralization rate (= number of papered communication / total number of communication) for each `liberal` doctors
 ------
Requete sur MySQL :
        SELECT (COUNT(id) / total_communication.total_com)  AS Demateralization_rate,
               lifen.sender_name
          FROM lifen AS lifen
     LEFT JOIN (SELECT COUNT(id) AS total_com ,
                       sender_name
                  FROM lifen
                 WHERE sender_category = 'liberal'
              GROUP BY sender_name ) AS  total_communication
            ON total_communication.sender_name = lifen.sender_name
         WHERE telecom = 'paper'
           AND sender_category = 'liberal'
      GROUP BY sender_name
--------------------

- Doctors list that have sent at least 5 communications during the 7 days following their first communication.

        SELECT sender_name ,
               COUNT(id_com) AS nbr_com
          FROM (
                    SELECT lifen.sender_name AS sender_name,
                           created_at  AS com_date ,
                           lifen.id AS id_com,
                           get_first_com.min_com_date  AS min_com_date ,
                           min_com_date_after_seven_days
                      FROM lifen lifen
                 LEFT JOIN ( SELECT MIN(created_at) AS min_com_date ,
                                    DATE_ADD(MIN(created_at), INTERVAL 7 DAY) AS min_com_date_after_seven_days,
                                    sender_name
                               FROM lifen
                           GROUP BY sender_name) AS get_first_com
                       ON lifen.sender_name = get_first_com.sender_name) AS t
         WHERE  com_date BETWEEN min_com_date AND min_com_date_after_seven_days
      GROUP BY sender_name
  HAVING COUNT(id_com) > 4

 ------
