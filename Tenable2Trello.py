# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:52:08 2018

@author: New
"""
#import sys
import json
#import pprint
from tenable_io.client import TenableIOClient
from trello import TrelloClient
import logger


class TenableTrelloIntegration(object):

    def __init__(self):
        self.trello_client = TrelloClient(
                api_key='',
                api_secret='',
                token=''
        )
        
    def TenableIOExport(self):
        '''
        Instantiate an instance of the TenableIOClient.
        '''
        client = TenableIOClient(access_key='', secret_key='')
    
        '''
        Export and download vulnerabilities.
        Note: The file name can be optionally parameterized with "%(chunk_id)s" to allow multiple chunks. Otherwise the
            chunk ID will be append to the file name.
        '''
        chunks_available = client.export_helper.download_vulns('c:/temp/tenable/vuln')
    
        '''
        Export and download assets.
        Note: The file name can be optionally parameterized with "%(chunk_id)s" to allow multiple chunks. Otherwise the
            chunk ID will be append to the file name.
        '''
        chunks_available = client.export_helper.download_assets('c:/temp/tenable/asset', chunk_size=100)        
        
    
    def GetOrCreateBoard(self,board_name):
        
        all_boards = trello_client.list_boards()

        board_exists = False
                
        for board in all_boards:
            if board.name == trello_board_name:
                logger.info('Found board {}'.format(trello_board_name))
                board_exists = True
                return board
                break
            
        if board_exists == False:
            logger.info('Board {} not found, creating'.format(trello_board_name))
            return  trello_client.add_board(board_name=trello_board_name)        

    def GetList(self,board, name):
        for list in board.list_lists():
            if list.name == name:
                return list
        raise Exception('list {} not found'.format(name))
             


with open('c:/temp/tenable/vuln_1.json','r') as read_file:
    data = json.load(read_file)
    

#upload_list = ['info','high','critical','medium','low']
# choosing these because there aren't as many of them
upload_list = ['low','critical']

severity = {}    

for i in range(len(data)):
    sev = data[i]['severity']
    if sev in severity.keys():
        severity[sev] = severity[sev] + 1
    else:
        severity[sev] = 1
        
        
tti = TenableTrelloIntegration()
board = tti.GetOrCreateBoard('Vulnerabilities')


criticals = []

for vuln in data:
    if vuln['severity'] == 'critical':
        criticals.append(vuln)

board.list_lists()


for vuln in criticals:
    print(vuln['plugin']['name'])

# Check to make sure the board exists



       
