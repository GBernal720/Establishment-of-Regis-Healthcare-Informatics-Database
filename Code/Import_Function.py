import csv, ast, psycopg2
from info import *



def run_test(fullpath,name):
    f=open(fullpath, 'r')
    reader = csv.reader(f)
    longest, headers, type_list=[],[],[]

    def dataType(val, current_type):
        try:
            t=ast.literal_eval(val)
        except ValueError:
            return 'varchar'
        except SyntaxError:
            return 'varchar'
        if type(t) in [int,long,float]:
            if (type(t) in [int, long]) and current_type not in ['float','varchar']:
                if (-32768 < t < 32767) and current_type not in ['int','bigint']:
                    return 'smallint'
                elif (-2147483648 < t < 2147483647) and current_type not in ['bigint']:
                    return 'int'
                else:
                    return 'bigint'
            if type(t) is float and current_type not in ['varchar']:
                return 'decimal'
        else:
            return 'varchar'

    for row in reader:
        if len(headers) ==0:
            headers = row
            for col in row:
                longest.append(0)
                type_list.append(' ')
        else:
            for i in range(len(row)):
                if type_list[i] == 'varchar' or row[i] == 'NA':
                    pass
                else:
                    var_type = dataType(row[i],type_list[i])
                    type_list[i] = var_type
                if len(row[i]) > longest[i]:
                    longest[i] = len(row[i])
    f.close()

    statement = 'create table '+name+'('

    for i in range(len(headers)):
        if type_list[i] == 'varchar':
            statement = (statement + '\n{} varchar({}),').format(headers[i].lower(), str(longest[i]))
        else:
            statement = (statement +'\n' + '{} {}' + ',').format(headers[i].lower(), type_list[i])

    statement = statement[:-1]+');'



    connection = psycopg2.connect(user = User, password = Password, host = Host, port = Port, database = Database)
    cursor = connection.cursor()
    cursor.execute('Drop table '+name)
    connection.commit()
    print("Table dropped PostgreSQL ")
    cursor.close()
    connection.close()

    connection = psycopg2.connect(user = User, password = Password, host = Host, port = Port, database = Database)
    cursor = connection.cursor()
    cursor.execute(statement)
    connection.commit()
    print (statement)
    print("Table created successfully in PostgreSQL ")
    cursor.close()
    connection.close()


    connection = psycopg2.connect(user = User, password = Password, host = Host, port = Port, database = Database)
    cursor = connection.cursor()
    cursor.execute('copy PUBLIC.'+name+ ' from '+"'"+fullpath+"'"+" with delimiter ',' csv header;")
    connection.commit()
    print("Data uploaded to PostgreSQL ")
    cursor.close()
    connection.close()

