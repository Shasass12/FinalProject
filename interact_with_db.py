import psycopg2


def enter_sheelon_row(
        arrive_to_uni_times,
        eating_habits,
        preferred_dish,
        eat_kosher,
        food_preferences,
        preferred_uni_food_shop,
        food_styles,
        allergies
):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        conn = psycopg2.connect(host='ec2-34-231-183-74.compute-1.amazonaws.com',
                                user='idayggcayroafv',
                                port=5432,
                                password='29d8e5aa0519b354029cdf2848fdcaec98690fdefcbff037bc39fde1b1547ce3',
                                database='dar7m8bk3j59f6')

        # create a cursor
        cur = conn.cursor()
        query = f"""
        INSERT INTO sheelon (arrive_to_uni_times,eating_habits,preferred_dish,eat_kosher,food_preferences,preferred_uni_food_shop,food_styles,allergies)
        VALUES ('{arrive_to_uni_times}','{eating_habits}','{preferred_dish}','{eat_kosher}','{food_preferences}','{preferred_uni_food_shop}','{food_styles}','{allergies}');
        """
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def enter_sheelon2_row(
        accept_recommendation,
        business_interest,
        recommendation_accept_number,
        algorithm_precision_number,
        recommendation_success_number
):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        conn = psycopg2.connect(host='ec2-34-231-183-74.compute-1.amazonaws.com',
                                user='idayggcayroafv',
                                port=5432,
                                password='29d8e5aa0519b354029cdf2848fdcaec98690fdefcbff037bc39fde1b1547ce3',
                                database='dar7m8bk3j59f6')

        # create a cursor
        cur = conn.cursor()
        query = f"""
        INSERT INTO sheelon2 (accept_recommendation,business_interest,recommendation_accept_number,algorithm_precision_number,recommendation_success_number)
        VALUES ('{accept_recommendation}','{business_interest}','{recommendation_accept_number}','{algorithm_precision_number}','{recommendation_success_number}');
        """
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def create_sheelon_table():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        conn = psycopg2.connect(host='ec2-34-231-183-74.compute-1.amazonaws.com',
                                user='idayggcayroafv',
                                port=5432,
                                password='29d8e5aa0519b354029cdf2848fdcaec98690fdefcbff037bc39fde1b1547ce3',
                                database='dar7m8bk3j59f6')

        # create a cursor
        cur = conn.cursor()
        query = """
        CREATE TABLE sheelon (
            arrive_to_uni_times varchar(45),
            eating_habits varchar(45),
            preferred_dish varchar(45),
            eat_kosher varchar(45),
            food_preferences varchar(45),
            preferred_uni_food_shop varchar(45),
            food_styles varchar(45),
            allergies varchar(256)
        )
        """
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def create_sheelon2_table():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        conn = psycopg2.connect(host='ec2-34-231-183-74.compute-1.amazonaws.com',
                                user='idayggcayroafv',
                                port=5432,
                                password='29d8e5aa0519b354029cdf2848fdcaec98690fdefcbff037bc39fde1b1547ce3',
                                database='dar7m8bk3j59f6')

        # create a cursor
        cur = conn.cursor()
        query = """
        CREATE TABLE sheelon2 (
            accept_recommendation varchar(45),
            business_interest varchar(45),
            recommendation_accept_number varchar(45),
            algorithm_precision_number varchar(45),
            recommendation_success_number varchar(45)
        )
        """
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
