#!/usr/bin/python
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

from random import randint

from MySQLdb import *

def country_init(cursor, countries):
        '''
        Ok so my plan with this is to have the verification code saved in the first row of each round. This allows for multiple round and also lends a place to dump the codes

        I'm starting to realise this is not gunna work, as you need to be able to verify people more than once. The solution to this is adding a round id that'll go on the front of the verif codes

        Dels should work fine tho, cause they'll store their own del_id and we can just grab data about that from their row 
        '''
        sqlquery = "SELECT * FROM del_identity WHERE del_id = '1'"
        cursor.execute(sqlquery)
        response =  cursor.fetchone()
        round_id = int(response["verif_codes"]) + 1
        sqlquery = "UPDATE del_identity SET verif_codes = {0} WHERE del_id = '1'".format(round_id)
        cursor.execute(sqlquery)
        countries = eval(countries)
        sqlquery = "INSERT INTO del_identity (country) VALUES (-1)"
        cursor.execute(sqlquery
        for i in range(len(countries)):
            sqlquery = "INSERT INTO del_identity (country) VALUES ({0})".format(countries[i])
            cursor.execute(sqlquery)
        return ["0"]

def verify_facs(cursor, type, digits):
        if type = '1':
                pres_ver = random.randint(10000, 99999)
                sec_ver = random.randint(10000, 99999)
                asec_ver = random.randint(10000, 99999)
		verif_codes = str(pres_ver)+chr(31)+str(sec_ver)+chr(31)+str(asec_ver)
                sqlquery = "UPDATE  del_identity SET verif_code = {0} WHERE country = '-1'".format(verif_codes) 
                cursor.execute(sqlquery)
                return ["0", pres_ver, sec_ver, asec_ver]
        if type == '2':
                sqlquery = "SELECT * FROM del_identity WHERE country = -1"
                cursor.execute(sqlquery)
                response = cursor.fetchall()
                for i in range(len(response)):
                    verif_codes = response[i]["verif_codes"]
                    verif_codes = verif_codes.split(chr(31))
                    if verif_codes[0] == digits[0]:
                       #This means they are the president and etc
                       accessToken = "pres"
                    elif verif_codes[1] == digits[1]:
                       accesToken = "sec"
                    elif verif_codes[2] == digits[2]:
                       accessToken = "asec"
                    else:
                       accessToken = "-1"
                return ["0", accessToken]
		
                


