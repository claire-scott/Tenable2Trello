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
                api_key='b21f444e87b41ef579932841e026aea0',
                api_secret='4334bbc2a87ce3942fd6531bb47add57f97b7191703a3499eb89d506bba422eb',
                token='eff7de29575d32b029ad8487a72dd680d0436bc11c098bbc9d7c53705af68738'
        )
        
    def TenableIOExport(self):
        '''
        Instantiate an instance of the TenableIOClient.
        '''
        client = TenableIOClient(access_key='0261d1c97111a4e5bca0c1b0d81d87b418b49b567dc0408a2cf117efa608d1d5', secret_key='199ffbaa401258d1a3b474b26df556adf182814b3ad433cb1d303719e9efa107')
    
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
             


#trello key   b21f444e87b41ef579932841e026aea0
#secret 4334bbc2a87ce3942fd6531bb47add57f97b7191703a3499eb89d506bba422eb
#trello token   eff7de29575d32b029ad8487a72dd680d0436bc11c098bbc9d7c53705af68738

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



       