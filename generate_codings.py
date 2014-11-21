import sqlite3
import csv
import sys

# from 1 to 11 or -1 for gephi files
codings = -1
# 1 is open, 2 is closed
skill = 1

conn = sqlite3.connect("db.rqda") # or use :memory: to put it in RAM

cursor1 = conn.cursor()

#######################################
############ FILES QUERY ##############
#######################################

sql="""
SELECT DISTINCT name
FROM filecat
WHERE status = 1
"""
cursor1.execute(sql)

col = 0
all_file_cats=[elt[col] for elt in cursor1.fetchall()]

sql = """
SELECT source.id, source.name, GROUP_CONCAT(filecat.name)  as categories
FROM source
	LEFT JOIN treefile
		ON source.id = treefile.fid
		LEFT JOIN filecat
			ON treefile.catid = filecat.catid
WHERE source.status = 1
	AND treefile.status = 1
	AND filecat.status = 1
GROUP BY source.id
"""
cursor1.execute(sql)

files = {}
for _id, name, categories in cursor1.fetchall():
    files[_id] = [name]
    for cat in all_file_cats:
        if cat in categories:
            files[_id].append(1)
        else:
            files[_id].append(0)



#######################################
############ CODES QUERY ##############
#######################################

sql="""
SELECT DISTINCT name
FROM codecat
WHERE status = 1
"""
cursor1.execute(sql)

col = 0
all_code_cats=[elt[col] for elt in cursor1.fetchall()]

sql = """
SELECT freecode.id, freecode.name, GROUP_CONCAT(codecat.name)  as categories
FROM freecode
	LEFT JOIN treecode
		ON freecode.id = treecode.cid 
		LEFT JOIN codecat
			ON treecode.catid = codecat.catid 
WHERE freecode.status = 1

GROUP BY freecode.id
"""
codes = {}
cursor1.execute(sql)

the_file = open('nodes.csv','wb')
nodes = csv.writer(the_file)
header=['Id','Label']
header.extend(all_code_cats)
nodes.writerow (header)

for _id, name, categories in cursor1.fetchall():
    codes[_id] = [_id, name]
    the_line = [_id, name]
    for cat in all_code_cats:
        # TODO: cat in categories is actually looking for the string
        if categories and cat in categories:
            codes[_id].append(1)
            the_line.append(1)
        else:
            codes[_id].append(0)
            the_line.append(0)
    nodes.writerow (the_line)
the_file.close()


#######################################
############ CODING QUERY #############
#######################################
# 1 is open, 2 is closed on source.id IN...
sql = """
SELECT  coding.fid AS file_id, source.name AS filename, 
        coding.cid AS code_id, freecode.name AS codename , 
        coding.selfirst, coding.selend 
FROM coding, source, freecode 
WHERE coding.status == 1 
        AND coding.fid == source.id 
        AND coding.status == 1
        AND coding.cid == freecode.id
        AND freecode.status == 1 
        AND source.id IN (SELECT fid FROM treefile WHERE catid= """ + str(skill) + """)
ORDER BY coding.cid """

cursor1.execute(sql)
cods = cursor1.fetchall()


r={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
c={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
d={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
x={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
y={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
z={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
a={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
b={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
e={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
f={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
g={'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}

def are_related(relations, a):
    for r in relations:
        if not is_related(r, a):
            return False;
    return True


def is_related(c, r):
    if r['fid'] == c['fid'] and r['cid'] < c['cid']:
        if r['begin'] <= c['begin'] and c['end'] <= r['end'] or \
            c['begin'] <= r['begin'] and r['end'] <= c['end'] or \
            c['begin'] > r['begin'] and c['begin'] <= r['end'] and c['end'] > r['end'] or \
            c['end'] < r['end'] and c['end'] >= r['begin'] and c['begin'] < r['begin']:
            return True
    return False


def get_header(level):
    header=['filename']
    header.extend(all_file_cats)
    for ind in range(level):
        header.append('id_' + str(ind + 1))
        header.append('codename_' + str(ind + 1))
        for el in all_code_cats:
            header.append(el + str(ind + 1))
    return header


def codings_gephi():
    level = 2
    the_file = open("edges.csv",'wb')
    edges = csv.writer(the_file)

    header=['Source','Target','Type', 'filename']
    header.extend(all_file_cats)
    for ind in range(level):
        header.append('id_' + str(ind + 1))
        header.append('codename_' + str(ind + 1))
    edges.writerow (header)

    counter = 0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                counter += 1
                the_relation = [r['cid'], c['cid'], "Undirected",]
                the_relation.extend(files[r['fid']])
                the_relation.extend(codes[r['cid']])
                the_relation.extend(codes[c['cid']])
                edges.writerow (the_relation)

    the_file.close()    
    print "Total of codings " + str(level) + ": " + str(counter)


def codings2():
    level = 2
    the_file = open("codings" + str(level) + ".csv",'wb')
    csv_writer = csv.writer(the_file)
    csv_writer.writerow (get_header(level))

    counter=0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                    counter+=1
                    the_relation = []
                    the_relation.extend(files[r['fid']])
                    the_relation.extend(codes[r['cid']])
                    the_relation.extend(codes[c['cid']])
                    csv_writer.writerow (the_relation)

    the_file.close()    
    print "Total of codings " + str(level) + ": " + str(counter)


def codings3():
    level = 3
    the_file = open("codings" + str(level) + ".csv",'wb')
    csv_writer = csv.writer(the_file)
    csv_writer.writerow (get_header(level))

    counter=0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in cods:
                    if are_related([c,r], d):
                        counter+=1
                        the_relation = []
                        the_relation.extend(files[r['fid']])
                        the_relation.extend(codes[r['cid']])
                        the_relation.extend(codes[c['cid']])
                        the_relation.extend(codes[d['cid']])
                        csv_writer.writerow (the_relation)

    the_file.close()    
    print "Total of codings " + str(level) + ": " + str(counter)


def codings4():
    level = 4
    the_file = open("codings" + str(level) + ".csv",'wb')
    csv_writer = csv.writer(the_file)
    csv_writer.writerow (get_header(level))

    counter=0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in cods:
                    if are_related([c,r], d):
                        for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in cods:
                            if are_related([c,r,d], x):
                                counter+=1
                                the_relation = []
                                the_relation.extend(files[r['fid']])
                                the_relation.extend(codes[r['cid']])
                                the_relation.extend(codes[c['cid']])
                                the_relation.extend(codes[d['cid']])
                                the_relation.extend(codes[x['cid']])
                                csv_writer.writerow (the_relation)
    the_file.close()    
    print "Total of codings " + str(level) + ": " + str(counter)

def codings5():
    level = 5
    the_file = open("codings" + str(level) + ".csv",'wb')
    csv_writer = csv.writer(the_file)
    csv_writer.writerow (get_header(level))

    counter=0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in cods:
                    if are_related([c,r], d):
                        for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in cods:
                            if are_related([c,r,d], x):
                                for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in cods:
                                    if are_related([c,r,d,x], y):
                                        counter+=1
                                        the_relation = []
                                        the_relation.extend(files[r['fid']])
                                        the_relation.extend(codes[r['cid']])
                                        the_relation.extend(codes[c['cid']])
                                        the_relation.extend(codes[d['cid']])
                                        the_relation.extend(codes[x['cid']])
                                        the_relation.extend(codes[y['cid']])
                                        csv_writer.writerow (the_relation)
    the_file.close()    
    print "Total of codings " + str(level) + ": " + str(counter)


def codings6():
    level = 6
    the_file = open("codings" + str(level) + ".csv",'wb')
    csv_writer = csv.writer(the_file)
    csv_writer.writerow (get_header(level))

    counter=0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in cods:
                    if are_related([c,r], d):
                        for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in cods:
                            if are_related([c,r,d], x):
                                for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in cods:
                                    if are_related([c,r,d,x], y):
                                        for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in cods:
                                            if are_related([c,r,d,x,y], z):
                                                counter+=1
                                                the_relation = []
                                                the_relation.extend(files[r['fid']])
                                                the_relation.extend(codes[r['cid']])
                                                the_relation.extend(codes[c['cid']])
                                                the_relation.extend(codes[d['cid']])
                                                the_relation.extend(codes[x['cid']])
                                                the_relation.extend(codes[y['cid']])
                                                the_relation.extend(codes[z['cid']])
                                                csv_writer.writerow (the_relation)

    the_file.close()    
    print "Total of codings " + str(level) + ": " + str(counter)


def codings7():
    level = 7
    the_file = open("codings" + str(level) + ".csv",'wb')
    csv_writer = csv.writer(the_file)
    csv_writer.writerow (get_header(level))

    counter = 0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in cods:
                    if are_related([c,r], d):
                        for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in cods:
                            if are_related([c,r,d], x):
                                for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in cods:
                                    if are_related([c,r,d,x], y):
                                        for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in cods:
                                            if are_related([c,r,d,x,y], z):
                                                for a['fid'], a['fname'], a['cid'], a['cname'], a['begin'], a['end'] in cods:
                                                    if are_related([c,r,d,x,y,z], a):
                                                        counter+=1
                                                        the_relation = []
                                                        the_relation.extend(files[r['fid']])
                                                        the_relation.extend(codes[r['cid']])
                                                        the_relation.extend(codes[c['cid']])
                                                        the_relation.extend(codes[d['cid']])
                                                        the_relation.extend(codes[x['cid']])
                                                        the_relation.extend(codes[y['cid']])
                                                        the_relation.extend(codes[z['cid']])
                                                        the_relation.extend(codes[a['cid']])
                                                        csv_writer.writerow (the_relation)

    the_file.close()    
    print "Total of codings " + str(level) + ": " + str(counter)

def codings8():
    level = 8
    the_file = open("codings" + str(level) + ".csv",'wb')
    csv_writer = csv.writer(the_file)
    csv_writer.writerow (get_header(level))

    counter = 0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in cods:
                    if are_related([c,r], d):
                        for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in cods:
                            if are_related([c,r,d], x):
                                for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in cods:
                                    if are_related([c,r,d,x], y):
                                        for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in cods:
                                            if are_related([c,r,d,x,y], z):
                                                for a['fid'], a['fname'], a['cid'], a['cname'], a['begin'], a['end'] in cods:
                                                    if are_related([c,r,d,x,y,z], a):
                                                        for b['fid'], b['fname'], b['cid'], b['cname'], b['begin'], b['end'] in cods:
                                                            if are_related([c,r,d,x,y,z,a], b):
                                                                counter+=1
                                                                the_relation = []
                                                                the_relation.extend(files[r['fid']])
                                                                the_relation.extend(codes[r['cid']])
                                                                the_relation.extend(codes[c['cid']])
                                                                the_relation.extend(codes[d['cid']])
                                                                the_relation.extend(codes[x['cid']])
                                                                the_relation.extend(codes[y['cid']])
                                                                the_relation.extend(codes[z['cid']])
                                                                the_relation.extend(codes[a['cid']])
                                                                the_relation.extend(codes[b['cid']])
                                                                csv_writer.writerow (the_relation)

    the_file.close()    
    print "Total of codings " + str(level) + ": " + str(counter)

def codings9():
    level = 9
    the_file = open("codings" + str(level) + ".csv",'wb')
    csv_writer = csv.writer(the_file)
    csv_writer.writerow (get_header(level))

    counter = 0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in cods:
                    if are_related([c,r], d):
                        for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in cods:
                            if are_related([c,r,d], x):
                                for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in cods:
                                    if are_related([c,r,d,x], y):
                                        for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in cods:
                                            if are_related([c,r,d,x,y], z):
                                                for a['fid'], a['fname'], a['cid'], a['cname'], a['begin'], a['end'] in cods:
                                                    if are_related([c,r,d,x,y,z], a):
                                                        for b['fid'], b['fname'], b['cid'], b['cname'], b['begin'], b['end'] in cods:
                                                            if are_related([c,r,d,x,y,z,a], b):
                                                                for e['fid'], e['fname'], e['cid'], e['cname'], e['begin'], e['end'] in cods:
                                                                    if are_related([c,r,d,x,y,z,a,b], e):
                                                                        counter+=1
                                                                        the_relation = []
                                                                        the_relation.extend(files[r['fid']])
                                                                        the_relation.extend(codes[r['cid']])
                                                                        the_relation.extend(codes[c['cid']])
                                                                        the_relation.extend(codes[d['cid']])
                                                                        the_relation.extend(codes[x['cid']])
                                                                        the_relation.extend(codes[y['cid']])
                                                                        the_relation.extend(codes[z['cid']])
                                                                        the_relation.extend(codes[a['cid']])
                                                                        the_relation.extend(codes[b['cid']])
                                                                        the_relation.extend(codes[e['cid']])
                                                                        csv_writer.writerow (the_relation)


    the_file.close()    
    print "Total of codings " + str(level) + ": " + str(counter)

def codings10():
    level = 10
    the_file = open("codings" + str(level) + ".csv",'wb')
    csv_writer = csv.writer(the_file)
    csv_writer.writerow (get_header(level))

    counter = 0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in cods:
                    if are_related([c,r], d):
                        for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in cods:
                            if are_related([c,r,d], x):
                                for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in cods:
                                    if are_related([c,r,d,x], y):
                                        for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in cods:
                                            if are_related([c,r,d,x,y], z):
                                                for a['fid'], a['fname'], a['cid'], a['cname'], a['begin'], a['end'] in cods:
                                                    if are_related([c,r,d,x,y,z], a):
                                                        for b['fid'], b['fname'], b['cid'], b['cname'], b['begin'], b['end'] in cods:
                                                            if are_related([c,r,d,x,y,z,a], b):
                                                                for e['fid'], e['fname'], e['cid'], e['cname'], e['begin'], e['end'] in cods:
                                                                    if are_related([c,r,d,x,y,z,a,b], e):
                                                                        for f['fid'], f['fname'], f['cid'], f['cname'], f['begin'], f['end'] in cods:
                                                                            if are_related([c,r,d,x,y,z,a,b,e], f):
                                                                                counter+=1
                                                                                the_relation = []
                                                                                the_relation.extend(files[r['fid']])
                                                                                the_relation.extend(codes[r['cid']])
                                                                                the_relation.extend(codes[c['cid']])
                                                                                the_relation.extend(codes[d['cid']])
                                                                                the_relation.extend(codes[x['cid']])
                                                                                the_relation.extend(codes[y['cid']])
                                                                                the_relation.extend(codes[z['cid']])
                                                                                the_relation.extend(codes[a['cid']])
                                                                                the_relation.extend(codes[b['cid']])
                                                                                the_relation.extend(codes[e['cid']])
                                                                                the_relation.extend(codes[f['cid']])
                                                                                csv_writer.writerow (the_relation)


    the_file.close()    
    print "Total of codings " + str(level) + ":" + str(counter)

def codings11():
    level = 11
    the_file = open("codings" + str(level) + ".csv",'wb')
    csv_writer = csv.writer(the_file)
    csv_writer.writerow (get_header(level))

    counter = 0
    for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in cods:
        for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in cods:
            if are_related([c],r):
                for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in cods:
                    if are_related([c,r], d):
                        for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in cods:
                            if are_related([c,r,d], x):
                                for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in cods:
                                    if are_related([c,r,d,x], y):
                                        for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in cods:
                                            if are_related([c,r,d,x,y], z):
                                                for a['fid'], a['fname'], a['cid'], a['cname'], a['begin'], a['end'] in cods:
                                                    if are_related([c,r,d,x,y,z], a):
                                                        for b['fid'], b['fname'], b['cid'], b['cname'], b['begin'], b['end'] in cods:
                                                            if are_related([c,r,d,x,y,z,a], b):
                                                                for e['fid'], e['fname'], e['cid'], e['cname'], e['begin'], e['end'] in cods:
                                                                    if are_related([c,r,d,x,y,z,a,b], e):
                                                                        for f['fid'], f['fname'], f['cid'], f['cname'], f['begin'], f['end'] in cods:
                                                                            if are_related([c,r,d,x,y,z,a,b,e], f):
                                                                                for g['fid'], g['fname'], g['cid'], g['cname'], g['begin'], g['end'] in cods:
                                                                                    if are_related([c,r,d,x,y,z,a,b,e,f], g):
                                                                                        counter+=1
                                                                                        the_relation = []
                                                                                        the_relation.extend(files[r['fid']])
                                                                                        the_relation.extend(codes[r['cid']])
                                                                                        the_relation.extend(codes[c['cid']])
                                                                                        the_relation.extend(codes[d['cid']])
                                                                                        the_relation.extend(codes[x['cid']])
                                                                                        the_relation.extend(codes[y['cid']])
                                                                                        the_relation.extend(codes[z['cid']])
                                                                                        the_relation.extend(codes[a['cid']])
                                                                                        the_relation.extend(codes[b['cid']])
                                                                                        the_relation.extend(codes[e['cid']])
                                                                                        the_relation.extend(codes[f['cid']])
                                                                                        the_relation.extend(codes[g['cid']])
                                                                                        csv_writer.writerow (the_relation)


    the_file.close()    
    print "Total of codings " + str(level) + ": " + str(counter)



if codings == 1:
    codings1()
elif codings == 2:
    codings2()
elif codings == 3:
    codings3()
elif codings == 4:
    codings4()
elif codings == 5:
    codings5()
elif codings == 6:
    codings6()
elif codings == 7:
    codings7()
elif codings == 8:
    codings8()
elif codings == 9:
    codings9()
elif codings == 10:
    codings10()
elif codings == 11:
    codings11()
else:
    codings_gephi()



