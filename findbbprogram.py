import requests
from urllib import parse as p
import json
from colorama import init, Fore, Back, Style
import argparse
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
headers = {'User-Agent': user_agent}
print(f"""
█▀▀ █ █▄░█ █▀▄{Fore.RED} █▄▄ █▄▄{Fore.RESET} █▀█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█
█▀░ █ █░▀█ █▄▀ {Fore.RED}█▄█ █▄█ {Fore.RESET}█▀▀ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█ {Fore.CYAN}@0xjoyghosh{Fore.RESET}
----------------------------------------------------
{Fore.GREEN}Accidental Bug Happens find the program and report it{Fore.RESET}
""")
class findbbprogram():
    def api1(domain):
        try:
            req = requests.get("https://raw.githubusercontent.com/disclose/diodb/master/program-list.json", headers=headers)
            data = json.loads(req.text)
            for i in data:
                if i['program_name'] == host:
                    return f"{Fore.GREEN}[Found Program]{Fore.RESET} {i['contact_url']}"
                    break
                else:
                    pass
        except ConnectionError:
            return f"{Fore.YELLOW}[WARN]{Fore.RESET} No Internet Connection"
        except:
            pass
    def api2(domain):
        try:
            req = requests.get("https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/master/chaos-bugbounty-list.json", headers=headers)
            data = json.loads(req.text)
            for i in data['programs']:
                for j in i['domains']:
                    if j == domain:
                        return f"{Fore.GREEN}[Found Program]{Fore.RESET} {i['url']}"
                        break
                    else:
                        pass
        except ConnectionError:
            return f"{Fore.YELLOW}[WARN]{Fore.RESET} No Internet Connection"
        except:
            pass
    def api3(domain):
        try:
            req = requests.get("https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/hackerone_data.json", headers=headers)
            data = json.loads(req.text)
            for si in range(len(data)):
                for i in data[si]['targets']['in_scope']:
                    if domain in i['asset_identifier']:
                        return f"{Fore.GREEN}[Found Program]{Fore.RESET} {data[si]['url']}"
                        break
                    else:
                        pass
        except ConnectionError:
            return f"{Fore.YELLOW}[WARN]{Fore.RESET} No Internet Connection"
        except Exception as e:
            print(e)
            pass
    def api4(domain):
        try:
            req = requests.get("https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/bugcrowd_data.json", headers=headers)
            data = json.loads(req.text)
            for si in range(len(data)):
                for i in data[si]['targets']['in_scope']:
                   if domain in i['target']:
                        return f"{Fore.GREEN}[Found Program]{Fore.RESET} {data[si]['url']}"
                        break
        except ConnectionError:
            return f"{Fore.YELLOW}[WARN]{Fore.RESET} No Internet Connection"
        except:
            pass
    def api5(domain):
        try:
            req = requests.get("https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/federacy_data.json", headers=headers)
            data = json.loads(req.text)
            for si in range(len(data)):
                for i in data[si]['targets']['in_scope']:
                    if domain in i['target']:
                        return f"{Fore.GREEN}[Found Program]{Fore.RESET} {data[si]['url']}"
                        break
        except ConnectionError:
            return f"{Fore.YELLOW}[WARN]{Fore.RESET} No Internet Connection"
        except:
            pass
    def api6(domain):
        try:
            req = requests.get("https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/hackenproof_data.json", headers=headers)
            data = json.loads(req.text)
            for si in range(len(data)):
                for i in data[si]['targets']['in_scope']:
                    if domain in i['target']:
                        return f"{Fore.GREEN}[Found Program]{Fore.RESET} {data[si]['url']}"
                        break
        except ConnectionError:
            return f"{Fore.YELLOW}[WARN]{Fore.RESET} No Internet Connection"
        except:
            pass
    def api7(domain):
        try:
            req = requests.get("https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/intigriti_data.json", headers=headers)
            data = json.loads(req.text)
            for si in range(len(data)):
                for i in data[si]['targets']['in_scope']:
                    if domain in i['endpoint']:
                        return f"{Fore.GREEN}[Found Program]{Fore.RESET} {data[si]['url']}"
                        break
        except ConnectionError:
            return f"{Fore.YELLOW}[WARN]{Fore.RESET} No Internet Connection"
        except:
            pass
    def api8(domain):
        try:
            req = requests.get("https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/yeswehack_data.json", headers=headers)
            data = json.loads(req.text)
            for si in range(len(data)):
                for i in data[si]['targets']['in_scope']:
                    if domain in i['target']:
                        return f"{Fore.GREEN}[Found Program]{Fore.RESET} https://yeswehack.com/programs/{data[si]['id']}"
                        break
        except ConnectionError:
            return f"{Fore.YELLOW}[WARN]{Fore.RESET} No Internet Connection"
        except:
            pass
    def engine(domain):
        print(f"{Fore.GREEN}[INFO]{Fore.RESET} Searching for {domain}")
        try:
            if findbbprogram.api1(domain):
                print(findbbprogram.api1(domain))
            elif findbbprogram.api2(domain):
                print(findbbprogram.api2(domain))
            elif findbbprogram.api3(domain):
                print(findbbprogram.api3(domain))
            elif findbbprogram.api4(domain):
                print(findbbprogram.api4(domain))
            elif findbbprogram.api5(domain):
                print(findbbprogram.api5(domain))
            elif findbbprogram.api6(domain):
                print(findbbprogram.api6(domain))
            elif findbbprogram.api7(domain):
                print(findbbprogram.api7(domain))
            elif findbbprogram.api8(domain):
                print(findbbprogram.api8(domain))
            else:
                print(f"{Fore.YELLOW}[WARN]{Fore.RESET} No Program Found")
        except ConnectionError:
            print(f"{Fore.YELLOW}[WARN]{Fore.RESET} No Internet Connection")
        except:
            pass
    def readfile(file):
        try:
            with open(file, "r") as f:
                for line in f:
                    line = line.strip()
                    findbbprogram.engine(line)
        except FileNotFoundError:
            print(f"{Fore.YELLOW}[WARN]{Fore.RESET} File Not Found")
        except:
            pass

try:
    parse = argparse.ArgumentParser(description="Find Program from Domain")
    parse.add_argument("-d", "--domain", help="Domain to Find Program")
    parse.add_argument("-f", "--file", help="File to Find Program")
    args = parse.parse_args()
    if args.domain:
        if args.domain.startswith("http") or args.domain.startswith("https"):
            host = p.urlparse(args.domain).netloc
            findbbprogram.engine(host)
        else:
            findbbprogram.engine(args.domain)
    elif args.file:
        print(f"{Fore.GREEN}[INFO]{Fore.RESET} Multiple Domain Search")
        findbbprogram.readfile(args.file)
    else:
        print(f"{Fore.YELLOW}[WARN]{Fore.RESET} Please Use -h for Help")
except KeyboardInterrupt:
    print(f"{Fore.YELLOW}[WARN]{Fore.RESET} Keyboard Interrupt")
except:
    print(f"{Fore.YELLOW}[WARN]{Fore.RESET} Unknown Error")