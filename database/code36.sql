DO $$ 
DECLARE
    -- Global variables
    num1 INT := 95;
    num2 INT := 85;
BEGIN
    RAISE NOTICE 'Outer Variable num1: %', num1;
    RAISE NOTICE 'Outer Variable num2: %', num2;

    DECLARE
        -- Local variables
        num1 INT := 195;
        num2 INT := 185;
    BEGIN
        RAISE NOTICE 'Inner Variable num1: %', num1;
        RAISE NOTICE 'Inner Variable num2: %', num2;
    END;
END $$;
