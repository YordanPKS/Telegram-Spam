import subprocess, requests, time, os, re, traceback, random, logging, telethon, colorama, csv, json, configparser
from csv import reader
import argparse
import sys
from sys import argv
from datetime import MINYEAR, datetime, timedelta
from colorama import Fore, Back, Style, init
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, UserStatusLastWeek, PeerUser, PeerChannel, InputPeerChannel, InputPeerUser
from telethon.tl.functions.contacts import GetContactsRequest, DeleteContactsRequest
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.tl.functions.messages import GetDialogsRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError, YouBlockedUserError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import ChatAdminRequiredError, UserNotParticipantError
from telethon.tl.custom import Button
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError


API_ID = 2392599
HashID = '7e14b38d250953c8c1e94fd7b2d63550'

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
wi="\033[1,35m"

if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists('phone.csv'):
    open("phone.csv","w")


photo = 'beast1.jpg'

photo2 = ['beast1.jpg','beast2.jpg']

photo3 = ['beast1.jpg','beast2.jpg','beast3.jpg']

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
# input time in seconds
t = 5
  
# function call


def login():



    banner()
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1

            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
            client.start(phone)
            client.disconnect()
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Presiona enter para ir atras')
    input()

init()
n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
green = lg
red = r
yellow = ye

colors = [lg, r, w, cy, ye]


def banner():

    os.system('clear')

    print(f"""
{r}
 
            Telegram: t.me/Yordan_PKS{r}
            Developer : Yordan_PKS{r}


""")


'''
def messagesender():
    print(f'Elija una cuenta que no este limitada')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']


    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        target_group = to_group
        print('Fetching Members...')
        all_participants = []
       
        all_participants = client.get_participants(target_group, aggressive=False)
        
        print('Saving In file...')
        with open("msend.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['username', 'user id', 'access hash', 'name'])
            for user in all_participants:
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name = user.last_name
                else:
                    last_name = ""
                name = (first_name + ' ' + last_name).strip()
                writer.writerow([username, user.id, user.access_hash, name])
        print(f'Members scraped successfully.{lg}')

       
        acc_name = client.get_me().first_name 
        print(f'Message was sending throuh {acc_name} {ye}')
        
        SLEEP_TIME_2 = 40
        SLEEP_TIME_1 = 20
        SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
        users = []
        with open(r"msend.csv", encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)
        mode = 2
        message = str(input(f"send your messsage{lg}"))  
        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(f"Invalid Mode. Exiting.{lg}")
                client.disconnect()
                sys.exit()
            try:
                print(f"Sending Message to:", user['name'])
                client.send_message(receiver, message.format(user['name']))
                print("Waiting {} seconds".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                print("Waiting {} seconds".format(SLEEP_TIME_2))
                time.sleep(SLEEP_TIME_2)
            except Exception as e:
                print("Error:", e)
                print("Trying to continue...")
                print("Waiting {} seconds".format(SLEEP_TIME_1))
                time.sleep(SLEEP_TIME_1)
        client.disconnect()
        print(f"Done. Message sent to all users.") 
        input(f'\n Press enter to goto main menu...')
    sedmrunal()

def pcsender():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']




    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        target_group = to_group
        print('Fetching Members...')
        all_participants = []
       
        all_participants = client.get_participants(target_group, aggressive=False)
        
        print('Saving In file...')
        with open("msend.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['username', 'user id', 'access hash', 'name'])
            for user in all_participants:
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name = user.last_name
                else:
                    last_name = ""
                name = (first_name + ' ' + last_name).strip()
                writer.writerow([username, user.id, user.access_hash, name])
        print(f'Members scraped successfully.{lg}')

       
        acc_name = client.get_me().first_name 
        print(f'Message was sending throuh {acc_name} {ye}')
        
        SLEEP_TIME_2 = 40
        SLEEP_TIME_1 = 20
        SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
        users = []
        with open(r"msend.csv", encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)

        f = open ('message.txt','rt')
        textmsg = f.read()
        mode = 2
        message = textmsg
        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(f"Invalid Mode. Exiting.{lg}")
                client.disconnect()
                sys.exit()
            try:
                print(f"Sending Message to:", user['name'])
                client.send_file(receiver,'beast1.jpg',caption=message.format(user['name']))
                print("Waiting {} seconds".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                print("Waiting {} seconds".format(SLEEP_TIME_2))
                time.sleep(SLEEP_TIME_2)
            except Exception as e:
                print("Error:", e)
                print("Trying to continue...")
                print("Waiting {} seconds".format(SLEEP_TIME_1))
                time.sleep(SLEEP_TIME_1)
        client.disconnect()
        print(f"Done. Message sent to all users.") 
        input(f'\n Press enter to goto main menu...')
    sedmrunal()

def pcsender2():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']




    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        target_group = to_group
        print('Fetching Members...')
        all_participants = []
       
        all_participants = client.get_participants(target_group, aggressive=False)
        
        print('Saving In file...')
        with open("msend.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['username', 'user id', 'access hash', 'name'])
            for user in all_participants:
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name = user.last_name
                else:
                    last_name = ""
                name = (first_name + ' ' + last_name).strip()
                writer.writerow([username, user.id, user.access_hash, name])
        print(f'Members scraped successfully.{lg}')

       
        acc_name = client.get_me().first_name 
        print(f'Message was sending throuh {acc_name} {ye}')
        
        SLEEP_TIME_2 = 40
        SLEEP_TIME_1 = 20
        SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
        users = []
        with open(r"msend.csv", encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)

        f = open ('message.txt','rt')
        textmsg = f.read()
        mode = 2
        message = textmsg
        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(f"Invalid Mode. Exiting.{lg}")
                client.disconnect()
                sys.exit()
            try:
                print(f"Sending Message to:", user['name'])
                client.send_file(receiver,photo2,caption=message.format(user['name']))
                print("Waiting {} seconds".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                print("Waiting {} seconds".format(SLEEP_TIME_2))
                time.sleep(SLEEP_TIME_2)
            except Exception as e:
                print("Error:", e)
                print("Trying to continue...")
                print("Waiting {} seconds".format(SLEEP_TIME_1))
                time.sleep(SLEEP_TIME_1)
        client.disconnect()
        print(f"Done. Message sent to all users.") 
        input(f'\n Press enter to goto main menu...')
    sedmrunal()

def pcsender3():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']




    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        target_group = to_group
        print('Fetching Members...')
        all_participants = []
       
        all_participants = client.get_participants(target_group, aggressive=False)
        
        print('Saving In file...')
        with open("msend.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['username', 'user id', 'access hash', 'name'])
            for user in all_participants:
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name = user.last_name
                else:
                    last_name = ""
                name = (first_name + ' ' + last_name).strip()
                writer.writerow([username, user.id, user.access_hash, name])
        print(f'Members scraped successfully.{lg}')

       
        acc_name = client.get_me().first_name 
        print(f'Message was sending throuh {acc_name} {ye}')
        
        SLEEP_TIME_2 = 40
        SLEEP_TIME_1 = 20
        SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
        users = []
        with open(r"msend.csv", encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)

        f = open ('message.txt','rt')
        textmsg = f.read()
        mode = 2
        message = textmsg
        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(f"Invalid Mode. Exiting.{lg}")
                client.disconnect()
                sys.exit()
            try:
                print(f"Sending Message to:", user['name'])
                client.send_file(receiver,photo3,caption=message.format(user['name']))
                print("Waiting {} seconds".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                print("Waiting {} seconds".format(SLEEP_TIME_2))
                time.sleep(SLEEP_TIME_2)
            except Exception as e:
                print("Error:", e)
                print("Trying to continue...")
                print("Waiting {} seconds".format(SLEEP_TIME_1))
                time.sleep(SLEEP_TIME_1)
        client.disconnect()
        print(f"Done. Message sent to all users.") 
        input(f'\n Press enter to goto main menu...')
    sedmrunal()
'''
#all section are old dont touch


def groupsender():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']


    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        groups = []
        chats = []
        last_date = None
        chunk_size = 200

        result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash=0
                 ))
        chats.extend(result.chats)

        for chat in chats:
            try:
                if chat.megagroup == True:
                    groups.append(chat)
            except:
                continue

        print('Your Joined Groups List'+lg)
        i = 0
        for group in groups:
            print(str(i) + '- ' + group.title)
            i += 1


        sed = input('PRESS Y to continoue else press N\n')
        if sed == 'N':
            main_menu()
        else:
            pass
        f = open ('message.txt','rt')
        textmsg = f.read()
        msg = textmsg
        er = 0
        done = 0
        for x in client.iter_dialogs():
            if x.is_group:
                chat = x.id
                try:
                    done += 1
                    client.send_message(chat, msg)
                except:
                    er += 1
        print(f"Done in {done} chats, error in {er} chat(s)")

    sedmrunal()   

def groupsender1():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']


    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        groups = []
        chats = []
        last_date = None
        chunk_size = 200

        result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash=0
                 ))
        chats.extend(result.chats)

        for chat in chats:
            try:
                if chat.megagroup == True:
                    groups.append(chat)
            except:
                continue

        print('Your Joined Groups List'+lg)
        i = 0
        for group in groups:
            print(str(i) + '- ' + group.title)
            i += 1


        sed = input('PRESS Y to continoue else press N\n')
        if sed == 'N':
            main_menu()
        else:
            pass
        f = open ('message.txt','rt')
        textmsg = f.read()
        msg = textmsg
        er = 0
        done = 0
        for x in client.iter_dialogs():
            if x.is_group:
                chat = x.id
                try:
                    done += 1
                    client.send_file(chat,photo,caption=msg)
                except:
                    er += 1
        print(f"Done in {done} chats, error in {er} chat(s)")

    sedmrunal()
            

def groupsender2():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']


    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        groups = []
        chats = []
        last_date = None
        chunk_size = 200

        result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash=0
                 ))
        chats.extend(result.chats)

        for chat in chats:
            try:
                if chat.megagroup == True:
                    groups.append(chat)
            except:
                continue

        print('Your Joined Groups List'+lg)
        i = 0
        for group in groups:
            print(str(i) + '- ' + group.title)
            i += 1


        sed = input('PRESS Y to continoue else press N\n')
        if sed == 'N':
            main_menu()
        else:
            pass
        f = open ('message.txt','rt')
        textmsg = f.read()
        msg = textmsg
        er = 0
        done = 0
        for x in client.iter_dialogs():
            if x.is_group:
                chat = x.id
                try:
                    done += 1
                    client.send_file(chat,photo2,caption=msg)
                except:
                    er += 1
        print(f"Done in {done} chats, error in {er} chat(s)")

    sedmrunal()

def groupsender3():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']


    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        groups = []
        chats = []
        last_date = None
        chunk_size = 200

        result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash=0
                 ))
        chats.extend(result.chats)

        for chat in chats:
            try:
                if chat.megagroup == True:
                    groups.append(chat)
            except:
                continue

        print('Your Joined Groups List'+lg)
        i = 0
        for group in groups:
            print(str(i) + '- ' + group.title)
            i += 1


        sed = input('PRESS Y to continoue else press N\n')
        if sed == 'N':
            main_menu()
        else:
            pass
        f = open ('message.txt','rt')
        textmsg = f.read()
        msg = textmsg
        er = 0
        done = 0
        for x in client.iter_dialogs():
            if x.is_group:
                chat = x.id
                try:
                    done += 1
                    client.send_file(chat,photo3,caption=msg)
                except:
                    er += 1
        print(f"Done in {done} chats, error in {er} chat(s)")

    sedmrunal()





def listsender():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']


    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        f = open ('message.txt','rt')
        textmsg = f.read()        
        mrunal = open("grouplist.txt","rt")
        done = 0
        er = 0
        for line in mrunal :
            try:
                client.send_message(line,textmsg)
                done += 1
                print(f"sending done {line} here")
                time.sleep(1)
            except UserNotParticipantError:
                client(JoinChannelRequest(line))
                client.send_message(line,textmsg)
                done += 1
                print(f"sending done {line} here")
                time.sleep(1)

            except ChatWriteForbiddenError as my :
                print(my)
                print(f'admins restricted you in {line}')

            except ChatAdminRequiredError as t :
                print(t)
            except Exception as e:
                print(e)
                
                
        print(f"Done in {done} chats, error in chat(s)")

    sedmrunal()   


def listsender1():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']


    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        f = open ('message.txt','rt')
        textmsg = f.read()        
        mrunal = open("grouplist.txt","rt")
        done = 0
        er = 0
        for line in mrunal :
            try:
                client.send_file(line,photo,caption=textmsg)
                done += 1
                print(f"sending done {line} here")
                time.sleep(1)
            except UserNotParticipantError:
                client(JoinChannelRequest(line))
                client.send_file(line,photo,caption=textmsg)
                done += 1
                print(f"sending done {line} here")
                time.sleep(1)
            except ChatWriteForbiddenError as my :
                print(my)
                print(f'admins restricted you in {line}')
            except ChatAdminRequiredError as t :
                print(t)
            except Exception as e:
                print(e)
                
        print(f"Done in {done} chats, error in chat(s)")

    sedmrunal()   

def listsender2():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']


    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        f = open ('message.txt','rt')
        textmsg = f.read()        
        mrunal = open("grouplist.txt","rt")
        done = 0
        er = 0
        for line in mrunal :
            try:
                client.send_file(line,photo2,caption=textmsg)
                done += 1
                print(f"sending done {line} here")
                time.sleep(1)
            except UserNotParticipantError:
                client(JoinChannelRequest(line))
                client.send_file(line,photo2,caption=textmsg)
                done += 1
                print(f"sending done {line} here")
                time.sleep(1)
            except ChatWriteForbiddenError as my :
                print(my)
                print(f'admins restricted you in {line}')
            except ChatAdminRequiredError as t :
                print(t)
            except Exception as e:
                print(e)
                
        print(f"Done in {done} chats, error in chat(s)")

    sedmrunal()   


def listsender3():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']


    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        f = open ('message.txt','rt')
        textmsg = f.read()        
        mrunal = open("grouplist.txt","rt")
        done = 0
        er = 0
        for line in mrunal :
            try:
                client.send_file(line,photo3,caption=textmsg)
                done += 1
                print(f"sending done {line} here")
                time.sleep(1)
            except UserNotParticipantError:
                client(JoinChannelRequest(line))
                client.send_file(line,photo3,caption=textmsg)
                done += 1
                print(f"sending done {line} here")
                time.sleep(1)
            except ChatWriteForbiddenError as my :
                print(my)
                print(f'admins restricted you in {line}')
            except ChatAdminRequiredError as t :
                print(t)
            except Exception as e:
                print(e)
                
        print(f"Done in {done} chats, error in chat(s)")

    sedmrunal()   




def joiners():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['MRUNAL']['SCRAP_GROUP']


    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
       
        mrunal = open("grouplist.txt","rt")
        er = 0
        done = 0
        for line in mrunal :
            try:
                client(JoinChannelRequest(line))
                done += 1
                print(f"SucessFully Joined {line}")
                time.sleep(10)
            except Exception as e:
                er += 1
                print(f"{e},{line}")
                time.sleep(10)
                
        print(f"Done in {done} chats, error in {er} chat(s)")

    sedmrunal()

def chutia():
    banner()
    
    r = 0
    done = 0
    er = 0
    d = 1
    sur = input("\n\n Send group userame")
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {Style.RESET_ALL} {Style.BRIGHT + Fore.RESET} {phone}")
            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
            client.start(phone)
            #mrunal = open("grouplist.txt","rt")
            #duke = mrunal.readline(po)
            with open('pi.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                list_of_rows = list(csv_reader)
                row_number = po
                col_number = 1
                value = list_of_rows[row_number - 1][col_number - 1]
            try:
                client.send_message(sur,value)
                done += 1
                print(f"SucessFully sent {value}")
                print(value)

                   # time.sleep(10)
            except Exception as e:
                er += 1
                print(f"{e},{value}")
                       #time.sleep(10)
                

    
    print(f'{done} - Accounts Are sent')


def joines():
    r = 0
    k = input("send username")
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {Style.RESET_ALL} {Style.BRIGHT + Fore.RESET} {phone}")
            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
            client.start(phone)
            client(JoinChannelRequest(k))
    print(f'done!')
    input("Done!" if done else "Error!")


def mscrapper():
    print(f'choose accout that are not limited')
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    #to_group = config['MRUNAL']['SCRAP_GROUP']
    to_group = input(f'\n send group username')

    def sedmrunal():

        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)
        target_group = to_group
        print('Fetching Members...')
        all_participants = []
       
        all_participants = client.get_participants(target_group,limit= 4400)
        
        print('Saving In file...')
        with open("msend.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['srno','username', 'user id', 'access hash', 'name'])
            po = 0
            for user in all_participants:
                po += 1
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name = user.last_name
                else:
                    last_name = ""
                name = (first_name + ' ' + last_name).strip()
                writer.writerow([po,username, user.id, user.access_hash, name])
        print(f'Members scraped successfully.{lg}')
    
    sedmrunal()


def blkmsg():

    stacno = 1
    endacno = 100

    with open('phone.csv', 'r') as f:
        #global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Total account: ' + str(len(phlist)))
    message = str(input(f"send your messsage{lg}")) 



    SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
    startfrom = 0
    endto = 4400
      
    

    DevOp_ne_script_banaya_hai = int(stacno) - 1
    telegram_script_banyane_ke_liye_DevOp_ko_dm_kro = int(endacno)
    indexx = 0
    global DevOppro
    DevOppro = 0
    for deltaxd in phlist[DevOp_ne_script_banaya_hai:telegram_script_banyane_ke_liye_DevOp_ko_dm_kro]:
        indexx += 1
        print(f'Index : {indexx}')
        phone = utils.parse_phone(deltaxd)
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.start(phone)
        cd = client.get_me()
        print(f'Logged in as {cd.first_name}')
        SLEEP_TIME_2 = 2
        SLEEP_TIME_1 = 2
        #SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
        users = []
        with open(r"msend.csv", encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['srno'] = row[0]
                user['username'] = row[1]
                user['id'] = int(row[2])
                user['access_hash'] = int(row[3])
                user['name'] = row[4]
                users.append(user)
        peer_flood_status = 0
        mode = 2
        #message = str(input(f"send your messsage{lg}"))  
        for user in users:
            if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                startfrom += 1
                if peer_flood_status == 5:
                    print(f'Too many Peer Flood Errors! Closing session...')
                    break
                if mode == 2:
                    if user['username'] == "":
                        continue
                    receiver = client.get_input_entity(user['username'])
                elif mode == 1:
                    receiver = InputPeerUser(user['id'],user['access_hash'])
                else:
                    print(f"Invalid Mode. Exiting.{lg}")
                    client.disconnect()
                    sys.exit()
                try:
                    print(f"Sending Message to:", user['name'])
                    client.send_message(receiver, message.format(user['name']))
                    print("Waiting {} seconds".format(SLEEP_TIME))
                    time.sleep(SLEEP_TIME)
                except PeerFloodError:
                    print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                    print("Waiting {} seconds".format(SLEEP_TIME_2))
                    peer_flood_status += 1
                    time.sleep(SLEEP_TIME_2)
                    continue
                except Exception as e:
                    print("Error:", e)
                    print("Trying to continue...")
                    print("Waiting {} seconds".format(SLEEP_TIME_1))
                    time.sleep(SLEEP_TIME_1)
                    continue
        client.disconnect()
        print(f"Session Terminited") 
        


def blkmsg1():

    stacno = 1
    endacno = 100

    with open('phone.csv', 'r') as f:
        #global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Total account: ' + str(len(phlist)))



    SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
    startfrom = 0
    endto = 4400
      
    

    DevOp_ne_script_banaya_hai = int(stacno) - 1
    telegram_script_banyane_ke_liye_DevOp_ko_dm_kro = int(endacno)
    indexx = 0
    global DevOppro
    DevOppro = 0
    for deltaxd in phlist[DevOp_ne_script_banaya_hai:telegram_script_banyane_ke_liye_DevOp_ko_dm_kro]:
        indexx += 1
        print(f'Index : {indexx}')
        phone = utils.parse_phone(deltaxd)
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.start(phone)
        cd = client.get_me()
        print(f'Logged in as {cd.first_name}')
        SLEEP_TIME_2 = 2
        SLEEP_TIME_1 = 2
        #SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
        users = []
        with open(r"msend.csv", encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['srno'] = row[0]
                user['username'] = row[1]
                user['id'] = int(row[2])
                user['access_hash'] = int(row[3])
                user['name'] = row[4]
                users.append(user)
        
        f = open ('message.txt','rt')
        textmsg = f.read()
        peer_flood_status = 0
        mode = 2
        #message = str(input(f"send your messsage{lg}"))  
        for user in users:
            if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                startfrom += 1
                if peer_flood_status == 5:
                    print(f'Too many Peer Flood Errors! Closing session...')
                    break
                if mode == 2:
                    if user['username'] == "":
                        continue
                    receiver = client.get_input_entity(user['username'])
                elif mode == 1:
                    receiver = InputPeerUser(user['id'],user['access_hash'])
                else:
                    print(f"Invalid Mode. Exiting.{lg}")
                    client.disconnect()
                    sys.exit()
                try:
                    print(f"Sending Message to:", user['name'])
                    client.send_file(receiver,'beast1.jpg',caption=textmsg)
                    print("Waiting {} seconds".format(SLEEP_TIME))
                    time.sleep(SLEEP_TIME)
                except PeerFloodError:
                    print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                    print("Waiting {} seconds".format(SLEEP_TIME_2))
                    peer_flood_status += 1
                    time.sleep(SLEEP_TIME_2)
                    continue
                except Exception as e:
                    print("Error:", e)
                    print("Trying to continue...")
                    print("Waiting {} seconds".format(SLEEP_TIME_1))
                    time.sleep(SLEEP_TIME_1)
                    continue
        client.disconnect()
        print(f"Session Terminited")


def blkmsg2():

    stacno = 1
    endacno = 100

    with open('phone.csv', 'r') as f:
        #global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Total account: ' + str(len(phlist)))



    SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
    startfrom = 0
    endto = 4400
      
    

    DevOp_ne_script_banaya_hai = int(stacno) - 1
    telegram_script_banyane_ke_liye_DevOp_ko_dm_kro = int(endacno)
    indexx = 0
    global DevOppro
    DevOppro = 0
    for deltaxd in phlist[DevOp_ne_script_banaya_hai:telegram_script_banyane_ke_liye_DevOp_ko_dm_kro]:
        indexx += 1
        print(f'Index : {indexx}')
        phone = utils.parse_phone(deltaxd)
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.start(phone)
        cd = client.get_me()
        print(f'Logged in as {cd.first_name}')
        SLEEP_TIME_2 = 2
        SLEEP_TIME_1 = 2
        #SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
        users = []
        with open(r"msend.csv", encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['srno'] = row[0]
                user['username'] = row[1]
                user['id'] = int(row[2])
                user['access_hash'] = int(row[3])
                user['name'] = row[4]
                users.append(user)
        
        f = open ('message.txt','rt')
        textmsg = f.read()
        peer_flood_status = 0
        mode = 2
        #message = str(input(f"send your messsage{lg}"))  
        for user in users:
            if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                startfrom += 1
                if peer_flood_status == 5:
                    print(f'Too many Peer Flood Errors! Closing session...')
                    break
                if mode == 2:
                    if user['username'] == "":
                        continue
                    receiver = client.get_input_entity(user['username'])
                elif mode == 1:
                    receiver = InputPeerUser(user['id'],user['access_hash'])
                else:
                    print(f"Invalid Mode. Exiting.{lg}")
                    client.disconnect()
                    sys.exit()
                try:
                    print(f"Sending Message to:", user['name'])
                    client.send_file(receiver,photo2,caption=textmsg)
                    print("Waiting {} seconds".format(SLEEP_TIME))
                    time.sleep(SLEEP_TIME)
                except PeerFloodError:
                    print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                    print("Waiting {} seconds".format(SLEEP_TIME_2))
                    peer_flood_status += 1
                    time.sleep(SLEEP_TIME_2)
                    continue
                except Exception as e:
                    print("Error:", e)
                    print("Trying to continue...")
                    print("Waiting {} seconds".format(SLEEP_TIME_1))
                    time.sleep(SLEEP_TIME_1)
                    continue
        client.disconnect()
        print(f"Session Terminited")

def blkmsg3():

    stacno = 1
    endacno = 100

    with open('phone.csv', 'r') as f:
        #global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Total account: ' + str(len(phlist)))



    SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
    startfrom = 0
    endto = 4400
      
    

    DevOp_ne_script_banaya_hai = int(stacno) - 1
    telegram_script_banyane_ke_liye_DevOp_ko_dm_kro = int(endacno)
    indexx = 0
    global DevOppro
    DevOppro = 0
    for deltaxd in phlist[DevOp_ne_script_banaya_hai:telegram_script_banyane_ke_liye_DevOp_ko_dm_kro]:
        indexx += 1
        print(f'Index : {indexx}')
        phone = utils.parse_phone(deltaxd)
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.start(phone)
        cd = client.get_me()
        print(f'Logged in as {cd.first_name}')
        SLEEP_TIME_2 = 2
        SLEEP_TIME_1 = 2
        #SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
        users = []
        with open(r"msend.csv", encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['srno'] = row[0]
                user['username'] = row[1]
                user['id'] = int(row[2])
                user['access_hash'] = int(row[3])
                user['name'] = row[4]
                users.append(user)
        
        f = open ('message.txt','rt')
        textmsg = f.read()
        peer_flood_status = 0
        mode = 2
        #message = str(input(f"send your messsage{lg}"))  
        for user in users:
            if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                startfrom += 1
                if peer_flood_status == 5:
                    print(f'Too many Peer Flood Errors! Closing session...')
                    break
                if mode == 2:
                    if user['username'] == "":
                        continue
                    receiver = client.get_input_entity(user['username'])
                elif mode == 1:
                    receiver = InputPeerUser(user['id'],user['access_hash'])
                else:
                    print(f"Invalid Mode. Exiting.{lg}")
                    client.disconnect()
                    sys.exit()
                try:
                    print(f"Sending Message to:", user['name'])
                    client.send_file(receiver,photo3,caption=textmsg)
                    print("Waiting {} seconds".format(SLEEP_TIME))
                    time.sleep(SLEEP_TIME)
                except PeerFloodError:
                    print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                    print("Waiting {} seconds".format(SLEEP_TIME_2))
                    peer_flood_status += 1
                    time.sleep(SLEEP_TIME_2)
                    continue
                except Exception as e:
                    print("Error:", e)
                    print("Trying to continue...")
                    print("Waiting {} seconds".format(SLEEP_TIME_1))
                    time.sleep(SLEEP_TIME_1)
                    continue
        client.disconnect()
        print(f"Session Terminited")





def main_menu():
    banner()
    print(ye+'Choose a Option:'+n)
    print(cy+'            [0] scrapper'+n)
    print(cy+'            [1] Login'+n)
    print(cy+'            [2] Message Sender'+n)
    print(cy+'            [3] Message Sender[with photo 1 img]'+n)
    print(cy+'            [4] Message Sender[with photo 2 img]'+n)
    print(cy+'            [5] Message Sender[with photo 3 img]'+n)
    print(cy+'            [6] Group Sender                    '+n)
    print(cy+'            [7] Group Sender[with photo 1 img]'+n)
    print(cy+'            [8] Group Sender[with photo 2 img]'+n)
    print(cy+'            [9] Group Sender[with photo 3 img]'+n)
    print(cy+'            [10] List Sender '+n)


    
    a = int(input('\nEnter your choice: '))
    if a==1:
        login()
    elif a==0:
        mscrapper()
    elif a==2:
        blkmsg()
    elif a==3:
        blkmsg1()
    elif a==4:
        blkmsg2()
    elif a==5:
        blkmsg3()
    elif a==6:
        groupsender()
    elif a==7:
        groupsender1()
    elif a==8:
        groupsender2()
    elif a==9:
        groupsender3()
    elif a == 50:
        joiners()  
    elif a == 100:
        chutia()
    elif a == 69:
        joines()    
    elif a==10:
        print(lg+"[+]choose A option"+n)
        print(lg+"[1]    List Sender Message")
        print(lg+"[2]    List Sender with 1 photo and caption"+n)
        print(lg+"[3]    List Sender with 2 photo and caption"+n)
        print(lg+"[4]    List Sender with 3 photo and caption"+n)
        print(lg+"[5]    Main Menu"+n)
        b = int(input('\nEnter your choice: '))
        if b == 1:
            listsender()
        elif b == 2:
            listsender1()
        elif b == 3:
            listsender2()
        elif b == 4:
            listsender3()
        elif b == 5:
            countdown(int(t))
            main_menu()
        else:
            print('wrong choice entered Going to main menu')
            countdown(int(t))
            main_menu()


def passop():



    try:

        urls1= "https://pastebin.com/raw/5zXSPVeM"
        switchs = (requests.get(urls1))
        if switchs.text == "on":
            main_menu()
        if switchs.text == "off":
            print(f"""{re}
            
            
            
            
            
            [%]Server Offline[%]
            
     (Script Is destroyed By @GodmrunaL)
            
            
            
            
            
            
            \n""")
        
    except Exception as g:
        print(g)    

passop()
main_menu()


        
