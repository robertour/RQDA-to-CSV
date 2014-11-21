import sqlite3
import csv

class RQDA():
    """ An RQDA object that self.connects to an RQDA database """


    def __init__(self, rqda_db):
        self.conn = sqlite3.connect(rqda_db)# or use :memory: to put it in RAM
        self.cursor1 = self.conn.cursor()


    def get_all_file_cats(self):
        """ Get all file categories """

        try:
            return self.all_file_cats
        except AttributeError:
            sql="""
            SELECT DISTINCT name
            FROM filecat
            WHERE status = 1
            """
            self.cursor1.execute(sql)

            col = 0
            self.all_file_cats = [elt[col] for elt in self.cursor1.fetchall()]

            return self.all_file_cats


    def get_files(self):
        """" Get all files """

        sql = """
        SELECT source.id, source.name, GROUP_CONCAT(filecat.name) as categories
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
        self.cursor1.execute(sql)

        all_file_cats = self.get_all_file_cats()
        files = {}
        for _id, name, categories in self.cursor1.fetchall():
            files[_id] = [name]
            for cat in all_file_cats:
                if cat in categories:
                    files[_id].append(1)
                else:
                    files[_id].append(0)
        return files


    def get_all_code_cats(self):
        """ Get all code categories """

        try:
            return self.all_code_cats
        except AttributeError:
            sql="""
            SELECT DISTINCT name
            FROM codecat
            WHERE status = 1
            """
            self.cursor1.execute(sql)

            col = 0
            self.all_code_cats = [elt[col] for elt in self.cursor1.fetchall()]
            return self.all_code_cats


    def get_codes(self):
        """ Get all codes """



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
        self.cursor1.execute(sql)

        all_code_cats = self.get_all_code_cats()
        for _id, name, categories in self.cursor1.fetchall():
            codes[_id] = [_id, name]
            for cat in all_code_cats:
                # TODO: cat in categories is actually looking for the string
                if categories and cat in categories:
                    codes[_id].append(1)
                else:
                    codes[_id].append(0)
        return codes




    #######################################
    ############ CODING QUERY #############
    #######################################
    # 1 is open, 2 is closed on source.id IN...

    def get_codings(self, file_catid):
        """ get all the actual codings """

        where_file = "1"
        if file_catid:
            where_file = """catid= """ + str(file_catid)


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
                AND source.id IN (SELECT fid FROM treefile WHERE """ + where_file + """ )
        ORDER BY coding.cid """

        self.cursor1.execute(sql)
        return self.cursor1.fetchall()
