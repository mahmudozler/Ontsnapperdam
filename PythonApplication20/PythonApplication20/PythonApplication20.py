import psycopg2

import math


# Use the database
def interact_with_database(command):
    # Connect and set up cursor
	connection = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='2450086'")
	cursor = connection.cursor()
    
    # Execute the command
	cursor.execute(command)
	connection.commit()

    # Save results
	results = None
	try:
		results = cursor.fetchall()
	except psycopg2.ProgrammingError:
        # Nothing to fetch
		pass

    # Close connection
	cursor.close()
	connection.close()
    
	return results


# Uploads a score into the hiscore table
def upload_score(name, score):
	interact_with_database("UPDATE score SET score = {} WHERE name = '{}'".format(name , score))


# Downloads score data from database
def download_scores():
	return interact_with_database("SELECT * FROM users")
print(download_scores())

# Downloads the top score from database
def download_top_score():
	result = interact_with_database("SELECT * FROM score ORDER BY score")[0][1]
	return result

interact_with_database("UPDATE users SET score = 5")