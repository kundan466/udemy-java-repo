CREATE OR REPLACE FUNCTION calculate_sum(a INT, b INT)
RETURNS INT as $$
DECLARE
    result INT;
BEGIN
    result := a + b;
    RETURN result;
END;
$$ LANGUAGE plpgsql;


SELECT calculate_sum(5, 7) AS sum_result;