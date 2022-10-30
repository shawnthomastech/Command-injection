from asyncio import exceptions
from audioop import add
from gettext import install
from mimetypes import init
import sys
import requests
import urllib3
import git as gt

proxies = {'http' : 'http://127.0.0.1:8080' , 'https': 'http://http://127.0.0.1:8080'}
def main():
    if len(sys.argv) != 3:
        print("(+) Usage %s <url> <command>" % sys.argv[0])
        print("(+) Example: %s www.example.com whoami")
if __name__ == "__main__":
    main()

