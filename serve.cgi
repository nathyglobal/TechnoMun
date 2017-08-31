#!/usr/bin/python
import cgi
import cgitb

cgitb.enable()                                      
form = cgi.FieldStorage()  

import json

from MySQLdb import *

import admin.py

db = connect(host="localhost",user="root", passwd="sudomcnuggets",db="technomun", cursorclass=cursors.DictCursor)
cursor = db.cursor()
cursor.execute("USE technomun")

def handleRequest():
    print "Content-type: text/plain"
    print "Access-Control-Allow-Origin: *"
    print ""
    
    type = form.getvalue('req_type')
    
    print type
    #Admin functions
    if type == "country_init": #This function allows the admin to add in all the countries for the round (input -> array of countries | output -> idgaf)
        output = country_init(cursor, form.getvalue(countries))
    elif type == "verify_facs1": #This allows the admin to get the validation digits and give them to the pres/sec/asec (input -> idgaf | output -> array [pres, sec, asec])
        output = verify_facs(cursor, '1', '')
    elif type == "verify_facs2": #This is used by pres/sec/asec individually in order to verify their identity (input -> validation digits | output -> access token)
        output = verify_facs(cursor, '2', form.getvalue(digits)) 
    #Del Functions
    elif type == "get_countries":
        output = get_countries(cursor)
    elif type == "country_select": #This allows dels to choose their country and generates a row in the db for them (input -> country select | output -> either del_id or access token)
        output = country_select(cursor, form.getvalue(country))
    elif type == "send_ammend": #This allowa dels to send a new ammendment (input -> del_id, ammendment | output -> success/failure (failure caused by ammendments not open))
       output = send_ammend(cursor, form.getvalue(del_id), form.getvalue(ammendment))
    elif type == "send_note": #This allows dels to send a new notes (input -> del_id, note | output -> success/failure (failure caused by note passing not open))
       output = send_note(cursor, form.getvalue(del_id), form.getvalue(note))
    elif type == "send_speakers": #This allows dels to add their name to either side of the speakers list (input -> del_id, side | output -> success/failure)
       output = send_speakers(cursor, form.getvalue(del_id), form.getvalue(side))
    elif type == "cast_vote": #This allows delegates to cast their vote on a current vote (input -> del_id, vote | output -> success/failure)
       output = cast_vote(cursor, form.getvalue(del_id), form.getvalue(vote))
    elif type == "check_new": #Gets all new data (Notes, Ammendments, etc..) (input -> del_id | output -> array([type, data]...)
       output = check_new(cursor, form.getvalue(del_id))
    #Pres Functions
    elif type == "get_sorted_ammend": #This gets the new/all? sorted ammendments from the secretary
       output = get_sorted_ammend(cursor, form.getvalue(accessToken))
    elif type == "get_speakers_list":
       output = get_speakers_list(cursor, form.getvalue(accessToken))
    elif type == "add_new_ammend": #This allows the adding of a new ammendment, automatically creates new speakers list returns an ammendment ID (resolution's ammend ID  = 0)
       output = add_new_ammend(cursor, form.getvalue(ammendment), form.getvalue(accessToken))
    elif type == "init_vote": #This allows the presidents to call for a vote
       output = init_vote(cursor, form.getvalue(ammendID), form.getvalue(accessToken))
    #Sec Functions
    elif type == "get_new_ammend":
       output = get_new_ammend(cursor, form.getvalue(accessToken))
    elif type == "get_ammend":
       output = get_ammend(cursor, form.getvalue(accessToken))
    elif type == "send_sorted_ammend":
       output = send_sorted_ammend(cursor, form.getvalue(ammends),form.getvalue(accessToken))
    #ASec Functions
    elif type == "get_new_notes":
       output = get_new_notes(cursor, form.getvalue(accessToken))
    elif type == "judge_note":
       output = approve_note(cursor, form.getvalue(noteID), form.getvalue(judgement),form.getvalue(accessToken))
    else:
       output = ["1", "no request type"]
    db.commit()
    return json.dumps(output)



handleRequest()
