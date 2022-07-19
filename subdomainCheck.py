#!/usr/bin/python3
#  Alex Dexter 2021
#
#
import requests
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--version", help="Displays the version of the script.", action="store_true")
parser.add_argument("-p", "--prefix", help="""Set the perfix of the URL to a given value. The default is https://""", default="""https://""")
parser.add_argument("-u", "--url", help="""The base URL being targeted for the script.""")
parser.add_argument("-f", "--file", help="""Specify the list of subdomains to check.""")
parser.add_argument("-w", "--write", help="""Write the output to a file of the given name.""")
#parser.add_argument("-s", "--sufix", help="""Set the sufix of the URL to a given value. The deffault is .com""", default="""".com""")
args = parser.parse_args()


version = "0.1.0"

headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

def request_sub_domain(subdomain):
    answer = ""
    try:
        request = requests.get(str(subdomain), allow_redirects=True, timeout=.25, headers=headers)
        if(request.status_code):
            answer = str(subdomain) + " " + str(request.status_code)
    except:
        pass
    return answer


if(args.file and args.url):
    with open(args.file, 'r') as f:
        content = f.readlines()
    
    content = [  args.prefix + str(i.rstrip()) + "." + args.url for i in content ]
    responces = []
    
    for i in content:
        responce = request_sub_domain(i)
        if(responce):
            responces.append(request_sub_domain(i))
    
    print(responces)
    
elif():
    print("subdomaincheck version " + version)
    
else:
    print("")


