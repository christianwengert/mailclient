# coding=utf-8
import subprocess

from imapclient import IMAPClient


HOST = 'mail.netzone.ch'
USERNAME = 'christian@wengert.ch'
PASSWORD = subprocess.check_output(["/usr/local/bin/pass", "mail/christian@wengert.ch"])
PASSWORD = PASSWORD.split()[0].decode('utf8')

KEYMAPPING = {}


ssl = True

class Signature():
    pass

class Account():
    #username, password, First name, Name, host, port, ssl
    pass

class Mailbox():
    #name, account
    pass


class Search():
    flags = ''
    searchtemrs = ''
    date = ''

class Message():
    id = ''
    flags = ''   # is replied and forwarded here?
    attachments = ''
    subject = ''
    content = ''
    date = ''
    mailbox = ''
    label = ''



def save_search():
    pass

def new_mailbox():
    pass
def delete_mailbox():
    pass
def rename_mailbox():
    pass

def reply():
    pass


def forward():
    pass


def mark_unread():
    pass


def label():
    pass

def move():
    pass


def search():
    pass



def flag():
    pass


def delete():
    pass


def compose():
    pass











def clean_database():
    pass

def sync_database():

    #fetch

    pass


def main():
    server = IMAPClient(HOST, use_uid=True, ssl=ssl)
    server.login(USERNAME, PASSWORD)

    select_info = server.select_folder('INBOX')
    print('%d messages in INBOX' % select_info[b'EXISTS'])

    messages = server.search(['NOT', 'DELETED'])
    print("%d messages that aren't deleted" % len(messages))

    print()
    print("Messages:")
    response = server.fetch(messages, ['FLAGS', 'RFC822', 'RFC822.SIZE', 'INTERNALDATE'])
    for msgid, data in response.items():
        print('   ID %d: %d bytes, flags=%s' % (msgid,
                                                data[b'RFC822.SIZE'],
                                                data[b'FLAGS']))




if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description='Command line mail client.')
    #
    # parser.add_argument('--host', dest='accumulate', action='store_const',
    #                    const=sum, default=max,
    #                    help='sum the integers (default: find the max)')
    #
    # args = parser.parse_args()
    # print(args.accumulate(args.integers))

    main()
