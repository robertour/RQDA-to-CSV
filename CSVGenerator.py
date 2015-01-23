import sys
import os
import csv
import RQDA

r = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
c = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
d = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
x = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
y = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
z = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
a = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
b = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
e = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
f = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}
g = {'fid': 0, 'fname': 0, 'cid': 0, 'cname': 0, 'begin': 0, 'end': 0}


class CSVGenerator:
    """ Generate different CSVs according to different criterias. Some for Gephi """


    def __init__(self, codings, file_catnames, code_catnames, code_names, code_filters):

        rqda = RQDA.RQDA("db.rqda")
        self.all_file_cats = rqda.get_all_file_cats()
        self.files = rqda.get_files()
        self.all_code_cats = rqda.get_all_code_cats()

        code_names_all = code_names
        if code_filters:
            if code_names_all:
                code_names_all = code_names + "," + code_filters
            else:
                code_names_all = code_filters

        self.node_codes = rqda.get_codes(code_names, code_catnames)
        self.codes = rqda.get_codes(code_names_all, code_catnames)
        self.cods = rqda.get_codings(file_catnames, code_names, code_catnames)
        self.filters = rqda.get_codings(file_catnames, code_filters, None)

        xstr = lambda s: s or ""
        self.directory = (str(codings) + " - " + xstr(file_catnames) + " - " +
            xstr(code_filters) + " - " + xstr(code_catnames) + " - " +\
            xstr(code_names)).replace("'", "")

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)


    def are_related(self, relations, a):
        for r in relations:
            if not self.is_related(r, a):
                return False;
        return True


    def is_related(self, c, r):
        if r['fid'] == c['fid'] and r['cid'] < c['cid']:
            if r['begin'] <= c['begin'] and c['end'] <= r['end'] or \
                c['begin'] <= r['begin'] and r['end'] <= c['end'] or \
                c['begin'] > r['begin'] and c['begin'] <= r['end'] and c['end'] > r['end'] or \
                c['end'] < r['end'] and c['end'] >= r['begin'] and c['begin'] < r['begin']:
                return True
        return False

    def are_related_full(self, relations, a):
        for r in relations:
            if not self.is_related_full(r, a):
                return False;
        return True

    def is_related_full(self, c, r):
        if r['fid'] == c['fid']:
            if r['begin'] <= c['begin'] and c['end'] <= r['end'] or \
                c['begin'] <= r['begin'] and r['end'] <= c['end'] or \
                c['begin'] > r['begin'] and c['begin'] <= r['end'] and c['end'] > r['end'] or \
                c['end'] < r['end'] and c['end'] >= r['begin'] and c['begin'] < r['begin']:
                return True
        return False

    def get_header(self, level):
        header=['filename']
        header.extend(self.all_file_cats)
        for ind in range(level):
            header.append('id_' + str(ind + 1))
            header.append('codename_' + str(ind + 1))
            header.append('categories_' + str(ind + 1))
            for el in self.all_code_cats:
                header.append(el + str(ind + 1))
        header.append('codes')
        return header


    def generate_nodes(self):
        the_file = open( self.directory + '/nodes.csv','wb')
        nodes = csv.writer(the_file)
        header=['Id','Label','Categories']
        header.extend(self.all_code_cats)
        nodes.writerow (header)
        for the_line in self.node_codes:
            nodes.writerow (self.codes[the_line])
        the_file.close()


    def codings_gephi(self):
        self.generate_nodes()
        level = 2
        the_file = open( self.directory + "/edges.csv",'wb')
        edges = csv.writer(the_file)

        header=['Source','Target','Type', 'filename']
        header.extend(self.all_file_cats)
        for ind in range(level):
            header.append('id_' + str(ind + 1))
            header.append('codename_' + str(ind + 1))
            header.append('categories_' + str(ind + 1))
            for el in self.all_code_cats:
                header.append(el + str(ind + 1))
        edges.writerow (header)

        counter = 0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    counter += 1
                    the_relation = [r['cid'], c['cid'], "Undirected",]
                    the_relation.extend(self.files[r['fid']])
                    the_relation.extend(self.codes[r['cid']])
                    the_relation.extend(self.codes[c['cid']])
                    edges.writerow (the_relation)

        the_file.close()
        print self.directory  + "(level = " + str(level) + "): " + str(counter)


    def filtered_codings_gephi(self):
        self.generate_nodes()
        level = 2 + 1
        the_file = open( self.directory + "/edges.csv",'wb')
        edges = csv.writer(the_file)

        header=['Source','Target','Type', 'filename']
        header.extend(self.all_file_cats)
        for ind in range(level):
            header.append('id_' + str(ind + 1))
            header.append('codename_' + str(ind + 1))
            header.append('categories_' + str(ind + 1))
            for el in self.all_code_cats:
                header.append(el + str(ind + 1))
        edges.writerow (header)

        counter=0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in self.filters:
                        if self.are_related_full([c,r], d):
                            counter+=1
                            the_relation = [r['cid'], c['cid'], "Undirected",]
                            the_relation.extend(self.files[r['fid']])
                            the_relation.extend(self.codes[r['cid']])
                            the_relation.extend(self.codes[c['cid']])
                            the_relation.extend(self.codes[d['cid']])
                            edges.writerow (the_relation)

        the_file.close()
        print self.directory  + "(level = " + str(level) + "): " + str(counter)

    def codings(self, level):

        the_file = open( self.directory + "/codings" + str(level) + ".csv",'wb')
        csv_writer = csv.writer(the_file)
        csv_writer.writerow (self.get_header(level))

        counter = 0

        if level == 1:
            counter = self.codings1(csv_writer)
        elif level == 2:
            counter = self.codings2(csv_writer)
        elif level == 3:
            counter = self.codings3(csv_writer)
        elif level == 4:
            counter = self.codings4(csv_writer)
        elif level == 5:
            counter = self.codings5(csv_writer)
        elif level == 6:
            counter = self.codings6(csv_writer)
        elif level == 7:
            counter = self.codings7(csv_writer)
        elif level == 8:
            counter = self.codings8(csv_writer)
        elif level == 9:
            counter = self.codings9(csv_writer)
        elif level == 10:
            counter = self.codings10(csv_writer)
        elif level == 11:
            counter = self.codings11(csv_writer)

        the_file.close()
        print self.directory  + "(level = " + str(level) + "): " + str(counter)


    def codings1(self, csv_writer):
        counter=0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            counter+=1
            the_relation = []
            the_relation.extend(self.files[r['fid']])
            the_relation.extend(self.codes[r['cid']])
            the_relation.append(r['cname'])
            csv_writer.writerow (the_relation)
        return counter


    def codings2(self, csv_writer):
        counter=0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                        counter+=1
                        the_relation = []
                        the_relation.extend(self.files[r['fid']])
                        the_relation.extend(self.codes[r['cid']])
                        the_relation.extend(self.codes[c['cid']])
                        the_relation.append(r['cname'] + "-" + c['cname'])
                        csv_writer.writerow (the_relation)
        return counter



    def codings3(self, csv_writer):
        counter=0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in self.cods:
                        if self.are_related([c,r], d):
                            counter+=1
                            the_relation = []
                            the_relation.extend(self.files[r['fid']])
                            the_relation.extend(self.codes[r['cid']])
                            the_relation.extend(self.codes[c['cid']])
                            the_relation.extend(self.codes[d['cid']])
                            the_relation.append(r['cname'] + "-" + c['cname'] + "-" + d['cname'])
                            csv_writer.writerow (the_relation)
        return counter


    def codings4(self, csv_writer):
        counter=0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in self.cods:
                        if self.are_related([c,r], d):
                            for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in self.cods:
                                if self.are_related([c,r,d], x):
                                    counter+=1
                                    the_relation = []
                                    the_relation.extend(self.files[r['fid']])
                                    the_relation.extend(self.codes[r['cid']])
                                    the_relation.extend(self.codes[c['cid']])
                                    the_relation.extend(self.codes[d['cid']])
                                    the_relation.extend(self.codes[x['cid']])
                                    the_relation.append(r['cname'] + "-" + c['cname'] + "-" + d['cname'] + "-" + x['cname'])
                                    csv_writer.writerow (the_relation)
        return counter

    def codings5(self, csv_writer):
        counter=0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in self.cods:
                        if self.are_related([c,r], d):
                            for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in self.cods:
                                if self.are_related([c,r,d], x):
                                    for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in self.cods:
                                        if self.are_related([c,r,d,x], y):
                                            counter+=1
                                            the_relation = []
                                            the_relation.extend(self.files[r['fid']])
                                            the_relation.extend(self.codes[r['cid']])
                                            the_relation.extend(self.codes[c['cid']])
                                            the_relation.extend(self.codes[d['cid']])
                                            the_relation.extend(self.codes[x['cid']])
                                            the_relation.extend(self.codes[y['cid']])
                                            the_relation.append(r['cname'] + "-" + c['cname'] + "-" + d['cname'] + "-" + x['cname'] + "-" + y['cname'])
                                            csv_writer.writerow (the_relation)
        return counter


    def codings6(self, csv_writer):
        counter=0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in self.cods:
                        if self.are_related([c,r], d):
                            for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in self.cods:
                                if self.are_related([c,r,d], x):
                                    for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in self.cods:
                                        if self.are_related([c,r,d,x], y):
                                            for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in self.cods:
                                                if self.are_related([c,r,d,x,y], z):
                                                    counter+=1
                                                    the_relation = []
                                                    the_relation.extend(self.files[r['fid']])
                                                    the_relation.extend(self.codes[r['cid']])
                                                    the_relation.extend(self.codes[c['cid']])
                                                    the_relation.extend(self.codes[d['cid']])
                                                    the_relation.extend(self.codes[x['cid']])
                                                    the_relation.extend(self.codes[y['cid']])
                                                    the_relation.extend(self.codes[z['cid']])
                                                    the_relation.append(r['cname'] + "-" + c['cname'] + "-" + d['cname'] + "-" + x['cname'] + "-" + y['cname'] + "-" + z['cname'])
                                                    csv_writer.writerow (the_relation)
        return counter


    def codings7(self, csv_writer):
        counter = 0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in self.cods:
                        if self.are_related([c,r], d):
                            for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in self.cods:
                                if self.are_related([c,r,d], x):
                                    for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in self.cods:
                                        if self.are_related([c,r,d,x], y):
                                            for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in self.cods:
                                                if self.are_related([c,r,d,x,y], z):
                                                    for a['fid'], a['fname'], a['cid'], a['cname'], a['begin'], a['end'] in self.cods:
                                                        if self.are_related([c,r,d,x,y,z], a):
                                                            counter+=1
                                                            the_relation = []
                                                            the_relation.extend(self.files[r['fid']])
                                                            the_relation.extend(self.codes[r['cid']])
                                                            the_relation.extend(self.codes[c['cid']])
                                                            the_relation.extend(self.codes[d['cid']])
                                                            the_relation.extend(self.codes[x['cid']])
                                                            the_relation.extend(self.codes[y['cid']])
                                                            the_relation.extend(self.codes[z['cid']])
                                                            the_relation.extend(self.codes[a['cid']])
                                                            the_relation.append(r['cname'] + "-" + c['cname'] + "-" + d['cname'] + "-" + x['cname'] + "-" + y['cname'] + "-" + z['cname'] + "-" + a['cname'])
                                                            csv_writer.writerow (the_relation)
        return counter

    def codings8(self, csv_writer):
        counter = 0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in self.cods:
                        if self.are_related([c,r], d):
                            for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in self.cods:
                                if self.are_related([c,r,d], x):
                                    for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in self.cods:
                                        if self.are_related([c,r,d,x], y):
                                            for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in self.cods:
                                                if self.are_related([c,r,d,x,y], z):
                                                    for a['fid'], a['fname'], a['cid'], a['cname'], a['begin'], a['end'] in self.cods:
                                                        if self.are_related([c,r,d,x,y,z], a):
                                                            for b['fid'], b['fname'], b['cid'], b['cname'], b['begin'], b['end'] in self.cods:
                                                                if self.are_related([c,r,d,x,y,z,a], b):
                                                                    counter+=1
                                                                    the_relation = []
                                                                    the_relation.extend(self.files[r['fid']])
                                                                    the_relation.extend(self.codes[r['cid']])
                                                                    the_relation.extend(self.codes[c['cid']])
                                                                    the_relation.extend(self.codes[d['cid']])
                                                                    the_relation.extend(self.codes[x['cid']])
                                                                    the_relation.extend(self.codes[y['cid']])
                                                                    the_relation.extend(self.codes[z['cid']])
                                                                    the_relation.extend(self.codes[a['cid']])
                                                                    the_relation.extend(self.codes[b['cid']])
                                                                    the_relation.append(r['cname'] + "-" + c['cname'] + "-" + d['cname'] + "-" +
                                                                        x['cname'] + "-" + y['cname'] + "-" + z['cname'] + "-" + a['cname'] + "-" +
                                                                        b['cname'])
                                                                    csv_writer.writerow (the_relation)
        return counter

    def codings9(self, csv_writer):
        counter = 0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in self.cods:
                        if self.are_related([c,r], d):
                            for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in self.cods:
                                if self.are_related([c,r,d], x):
                                    for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in self.cods:
                                        if self.are_related([c,r,d,x], y):
                                            for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in self.cods:
                                                if self.are_related([c,r,d,x,y], z):
                                                    for a['fid'], a['fname'], a['cid'], a['cname'], a['begin'], a['end'] in self.cods:
                                                        if self.are_related([c,r,d,x,y,z], a):
                                                            for b['fid'], b['fname'], b['cid'], b['cname'], b['begin'], b['end'] in self.cods:
                                                                if self.are_related([c,r,d,x,y,z,a], b):
                                                                    for e['fid'], e['fname'], e['cid'], e['cname'], e['begin'], e['end'] in self.cods:
                                                                        if self.are_related([c,r,d,x,y,z,a,b], e):
                                                                            counter+=1
                                                                            the_relation = []
                                                                            the_relation.extend(self.files[r['fid']])
                                                                            the_relation.extend(self.codes[r['cid']])
                                                                            the_relation.extend(self.codes[c['cid']])
                                                                            the_relation.extend(self.codes[d['cid']])
                                                                            the_relation.extend(self.codes[x['cid']])
                                                                            the_relation.extend(self.codes[y['cid']])
                                                                            the_relation.extend(self.codes[z['cid']])
                                                                            the_relation.extend(self.codes[a['cid']])
                                                                            the_relation.extend(self.codes[b['cid']])
                                                                            the_relation.extend(self.codes[e['cid']])
                                                                            the_relation.append(r['cname'] + "-" + c['cname'] + "-" + d['cname'] + "-" +
                                                                                x['cname'] + "-" + y['cname'] + "-" + z['cname'] + "-" + a['cname'] + "-" +
                                                                                b['cname'] + "-" + e['cname'])
                                                                            csv_writer.writerow (the_relation)
        return counter

    def codings10(self, csv_writer):
        counter = 0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in self.cods:
                        if self.are_related([c,r], d):
                            for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in self.cods:
                                if self.are_related([c,r,d], x):
                                    for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in self.cods:
                                        if self.are_related([c,r,d,x], y):
                                            for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in self.cods:
                                                if self.are_related([c,r,d,x,y], z):
                                                    for a['fid'], a['fname'], a['cid'], a['cname'], a['begin'], a['end'] in self.cods:
                                                        if self.are_related([c,r,d,x,y,z], a):
                                                            for b['fid'], b['fname'], b['cid'], b['cname'], b['begin'], b['end'] in self.cods:
                                                                if self.are_related([c,r,d,x,y,z,a], b):
                                                                    for e['fid'], e['fname'], e['cid'], e['cname'], e['begin'], e['end'] in self.cods:
                                                                        if self.are_related([c,r,d,x,y,z,a,b], e):
                                                                            for f['fid'], f['fname'], f['cid'], f['cname'], f['begin'], f['end'] in self.cods:
                                                                                if self.are_related([c,r,d,x,y,z,a,b,e], f):
                                                                                    counter+=1
                                                                                    the_relation = []
                                                                                    the_relation.extend(self.files[r['fid']])
                                                                                    the_relation.extend(self.codes[r['cid']])
                                                                                    the_relation.extend(self.codes[c['cid']])
                                                                                    the_relation.extend(self.codes[d['cid']])
                                                                                    the_relation.extend(self.codes[x['cid']])
                                                                                    the_relation.extend(self.codes[y['cid']])
                                                                                    the_relation.extend(self.codes[z['cid']])
                                                                                    the_relation.extend(self.codes[a['cid']])
                                                                                    the_relation.extend(self.codes[b['cid']])
                                                                                    the_relation.extend(self.codes[e['cid']])
                                                                                    the_relation.extend(self.codes[f['cid']])
                                                                                    the_relation.append(r['cname'] + "-" + c['cname'] + "-" + d['cname'] + "-" +
                                                                                        x['cname'] + "-" + y['cname'] + "-" + z['cname'] + "-" + a['cname'] + "-" +
                                                                                        b['cname'] + "-" + e['cname'] + "-" + f['cname'])
                                                                                    csv_writer.writerow (the_relation)
        return counter

    def codings11(self, csv_writer):
        counter = 0
        for r['fid'], r['fname'], r['cid'], r['cname'], r['begin'], r['end'] in self.cods:
            for c['fid'], c['fname'], c['cid'], c['cname'], c['begin'], c['end'] in self.cods:
                if self.are_related([c],r):
                    for d['fid'], d['fname'], d['cid'], d['cname'], d['begin'], d['end'] in self.cods:
                        if self.are_related([c,r], d):
                            for x['fid'], x['fname'], x['cid'], x['cname'], x['begin'], x['end'] in self.cods:
                                if self.are_related([c,r,d], x):
                                    for y['fid'], y['fname'], y['cid'], y['cname'], y['begin'], y['end'] in self.cods:
                                        if self.are_related([c,r,d,x], y):
                                            for z['fid'], z['fname'], z['cid'], z['cname'], z['begin'], z['end'] in self.cods:
                                                if self.are_related([c,r,d,x,y], z):
                                                    for a['fid'], a['fname'], a['cid'], a['cname'], a['begin'], a['end'] in self.cods:
                                                        if self.are_related([c,r,d,x,y,z], a):
                                                            for b['fid'], b['fname'], b['cid'], b['cname'], b['begin'], b['end'] in self.cods:
                                                                if self.are_related([c,r,d,x,y,z,a], b):
                                                                    for e['fid'], e['fname'], e['cid'], e['cname'], e['begin'], e['end'] in self.cods:
                                                                        if self.are_related([c,r,d,x,y,z,a,b], e):
                                                                            for f['fid'], f['fname'], f['cid'], f['cname'], f['begin'], f['end'] in self.cods:
                                                                                if self.are_related([c,r,d,x,y,z,a,b,e], f):
                                                                                    for g['fid'], g['fname'], g['cid'], g['cname'], g['begin'], g['end'] in self.cods:
                                                                                        if self.are_related([c,r,d,x,y,z,a,b,e,f], g):
                                                                                            counter+=1
                                                                                            the_relation = []
                                                                                            the_relation.extend(self.files[r['fid']])
                                                                                            the_relation.extend(self.codes[r['cid']])
                                                                                            the_relation.extend(self.codes[c['cid']])
                                                                                            the_relation.extend(self.codes[d['cid']])
                                                                                            the_relation.extend(self.codes[x['cid']])
                                                                                            the_relation.extend(self.codes[y['cid']])
                                                                                            the_relation.extend(self.codes[z['cid']])
                                                                                            the_relation.extend(self.codes[a['cid']])
                                                                                            the_relation.extend(self.codes[b['cid']])
                                                                                            the_relation.extend(self.codes[e['cid']])
                                                                                            the_relation.extend(self.codes[f['cid']])
                                                                                            the_relation.extend(self.codes[g['cid']])
                                                                                            the_relation.append(r['cname'] + "-" + c['cname'] + "-" + d['cname'] + "-" +
                                                                                                x['cname'] + "-" + y['cname'] + "-" + z['cname'] + "-" + a['cname'] + "-" +
                                                                                                b['cname'] + "-" + e['cname'] + "-" + f['cname'] + "-" + g['cname'])
                                                                                            csv_writer.writerow (the_relation)
        return counter
