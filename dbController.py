import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='33!Talo10@',
                             database='resource_menager',
                             cursorclass=pymysql.cursors.DictCursor)

print(connection)
with connection:
    # with connection.cursor() as cursor:
        # Create a new record
        # sql = "INSERT INTO `administrator` (`name`, `resource_idresource`) VALUES ('vitoria', 1)"
        # sql = "INSERT INTO `User` (`name`, `Admintrator_idAdmintrator`) VALUES ('italo santos', 1)"
        # sql = "INSERT INTO `resource_file` (`name`) VALUES ('Ola mundo 123')"
        # cursor.execute(sql)

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `administrator`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)