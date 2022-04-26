
import psycopg2

def enter_sheelon_row(
        arrive_to_uni_times,
        eating_habits,
        preferred_dish,
        eat_kosher,
        food_preferences,
        preferred_uni_food_shop,
        food_styles,
        allergies,
        key
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
        INSERT INTO sheelon (arrive_to_uni_times,eating_habits,preferred_dish,eat_kosher,food_preferences,preferred_uni_food_shop,food_styles,allergies, key)
        VALUES ('{arrive_to_uni_times}','{eating_habits}','{preferred_dish}','{eat_kosher}','{food_preferences}','{preferred_uni_food_shop}','{food_styles}','{allergies}', '{key}');
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
        algorithm_subjective,
        recommendation_accept_number,
        algorithm_trust_result,
        other_causes_for_result,
        is_restaurant_known,
        restaurant_score,
        key
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
        INSERT INTO sheelon2 (accept_recommendation,algorithm_subjective,recommendation_accept_number,algorithm_trust_result,other_causes_for_result,is_restaurant_known,restaurant_score, key)
        VALUES ('{accept_recommendation}','{algorithm_subjective}','{recommendation_accept_number}','{algorithm_trust_result}','{other_causes_for_result}', '{is_restaurant_known}', '{restaurant_score}', '{key}');
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


def enter_sheelon3_row(device, age, gender, studies, hours_computer, hours_mobile, open_space, public_space,
                       large_space, noise, darkness, crowd, key):
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
        INSERT INTO sheelon3 (device,age,gender,studies,hours_computer, hours_mobile, open_space, public_space, large_space, noise, darkness, crowd, key)
        VALUES ('{device}','{age}','{gender}','{studies}','{hours_computer}', '{hours_mobile}', '{open_space}', '{public_space}', '{large_space}', '{noise}', '{darkness}', '{crowd}', '{key}');
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
            allergies varchar(256),
            key varchar(256)
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
        # (accept_recommendation,algorithm_subjective,recommendation_accept_number,algorithm_trust_result,other_causes_for_result,is_restaurant_known,restaurant_score, key)
        query = """
        CREATE TABLE sheelon2 (
            accept_recommendation varchar(45),
            algorithm_subjective varchar(45),
            recommendation_accept_number varchar(45),
            algorithm_trust_result varchar(45),
            other_causes_for_result varchar(45),
            is_restaurant_known varchar(45),
            restaurant_score varchar(45),
            key varchar(256)
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


def create_sheelon3_table():
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
        CREATE TABLE sheelon3 (
            device varchar(45),
            age varchar(45),
            gender varchar(45),
            studies varchar(45),
            hours_computer varchar(45),
            hours_mobile varchar(45),
            open_space varchar(45),
            public_space varchar(45),
            large_space varchar(45),
            noise varchar(45),
            darkness varchar(45),
            crowd varchar(45),
            key varchar(256)
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


def create_keys_table(keys):
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
        CREATE TABLE keys (
            key varchar(45),
            is_mobile bool,
            was_used bool
        )
        """
        cur.execute(query)
        conn.commit()
        # First 90 keys to mobile
        mobile_keys = []
        desktop_keys = []
        count = 0
        for key in keys:
            is_mobile = count < 90
            if is_mobile:
                mobile_keys.append(key)
            else:
                desktop_keys.append(key)
            query = f"""
            INSERT INTO keys (key, is_mobile, was_used)
            VALUES ('{key}', {is_mobile}, false);
            """
            count += 1
            cur.execute(query)
            conn.commit()
        print(mobile_keys)
        print(desktop_keys)
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def add_key(key, is_mobile):
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
        INSERT INTO keys (key, is_mobile, was_used)
        VALUES ('{key}', {is_mobile}, false);
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


def get_keys():
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
        SELECT * FROM keys;
        """
        cur.execute(query)
        keys = cur.fetchall()

        cur.close()
        conn.close()

        return keys
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def delete_sheelon_tables():
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
        DROP TABLE sheelon
        """
        cur.execute(query)
        conn.commit()

        query = """
        DROP TABLE sheelon2
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


def update_used_key(key):
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
        UPDATE keys set was_used=true WHERE key='{key}'
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


if __name__ == '__main__':
    add_key('axb', False)
    # delete_sheelon_tables()
    # create_sheelon_table()
    # create_sheelon2_table()