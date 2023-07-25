import requests
from urllib import parse as p
import json
from colorama import init, Fore
import argparse
import logging
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, render_template_string

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
headers = {'User-Agent': user_agent}

bootstrap_template = """
<!DOCTYPE html>
<html>
<head>
  <title>FindBB Program Search</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body class="container mt-5">
<center><pre>
  ___ _         _<font color="red"> ___ ___<font color="black"> ___                                 
 | __(_)_ _  __| <font color="red">| _ ) _ )<font color="black"> _ \_ _ ___  __ _ _ _ __ _ _ __  ___
 | _|| | ' \/ _` <font color="red">| _ \ _ \<font color="black">  _/ '_/ _ \/ _` | '_/ _` | '  \(_-<
 |_| |_|_||_\__,_<font color="red">|___/___/<font color="black">_| |_| \___/\__, |_| \__,_|_|_|_/__/
                       |___/ <font color="green">V2<font color="black">
 <font color="yellow">- ><font color="black"> Accidental Bug Happens find the program and report it
</pre></center><br/>
  <form method="post">
    <div class="mb-3">
      <label for="domain" class="form-label">Domain:</label>
      <input type="text" class="form-control" name="domain" id="domain" required>
    </div>
    <button type="submit" class="btn btn-primary">Search</button>
  </form>
  {% if program_info %}
    <div class="mt-4">
      <h2>Search Result</h2>
      <style>
      a {
        color: black;
        text-decoration: none;
      }
      </style>
      <div class='alert alert-success' role='alert'><a href='{{ program_info }}'>{{ program_info }}</a></div>
    </div>
  {% endif %}
</body>
</html>
"""

app = Flask(__name__)

class FindBBProgram:
    def __init__(self):
        self.programs_data = []

    def fetch_data(self, url):
        try:
            with requests.get(url, headers=headers) as req:
                if req.status_code == 200:
                    return json.loads(req.text)
                return []
        except requests.ConnectionError:
            return []
        except Exception as e:
            print(e)
            return []

    def api1(self, domain):
        if not self.programs_data:
            self.programs_data = self.fetch_data("https://raw.githubusercontent.com/disclose/diodb/master/program-list.json")
        for i in self.programs_data:
            if i['program_name'] == domain:
                return f"{Fore.GREEN}[Found Program]{Fore.RESET} {i['contact_url']}"
        return None

    def api2(self, domain):
        if not self.programs_data:
            self.programs_data = self.fetch_data("https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/master/chaos-bugbounty-list.json")
        for i in self.programs_data['programs']:
            if domain in i['domains']:
                return f"{Fore.GREEN}[Found Program]{Fore.RESET} {i['url']}"
        return None

    def api3(self, domain):
        try:
            endpoint = "https://raw.githubusercontent.com/trickest/inventory/main/targets.json"
            with requests.get(endpoint, headers=headers) as req:
                if req.status_code == 200:
                    data = json.loads(req.text)
                    data = data['targets']
                    for i in data:
                        if domain in i['domains']:
                            return f"{Fore.GREEN}[Found Program]{Fore.RESET} {i['url']}"
                return None
        except requests.ConnectionError:
            return None

    def search_program(self, domain):
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(api, domain) for api in (self.api1, self.api2, self.api3)]
            for future in futures:
                result = future.result()
                if result:
                    return result
        return None

    def engine(self, domain):
        print(f"{Fore.GREEN}[SRC]{Fore.RESET} Searching for {domain}")
        program_info = self.search_program(domain)
        return program_info

# Custom log handler for Flask
class CustomLogHandler(logging.StreamHandler):
    def emit(self, record):
        log_msg = self.format(record)
        if '127.0.0.1' in log_msg or 'localhost' in log_msg:
            log_msg = f"[WEB-UI] {log_msg}"
        else:
            level = record.levelname
            if level == 'INFO':
                log_msg = f"[INFO] {log_msg}"
            elif level == 'WARNING':
                log_msg = f"[WARN] {log_msg}"
        print(log_msg)

app.logger.addHandler(CustomLogHandler())

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        domain = request.form["domain"]
        program_info = FindBBProgram().engine(domain)
        if program_info:
            program_info = program_info.replace("[32m[Found Program][39m","")
            program_info = program_info.replace("[39m","")
            program_info = program_info.replace("[33m[WARN][39m","")
            program_info = program_info.replace("[39m","")
        return render_template_string(bootstrap_template, program_info=program_info)
    return render_template_string(bootstrap_template)

if __name__ == "__main__":
    init()
    print(f"""
  ___ _         _{Fore.RED} ___ ___{Fore.RESET} ___                                 
 | __(_)_ _  __| {Fore.RED}| _ ) _ ){Fore.RESET} _ \_ _ ___  __ _ _ _ __ _ _ __  ___
 | _|| | ' \/ _` {Fore.RED}| _ \ _ \{Fore.RESET}  _/ '_/ _ \/ _` | '_/ _` | '  \(_-<
 |_| |_|_||_\__,_{Fore.RED}|___/___/{Fore.RESET}_| |_| \___/\__, |_| \__,_|_|_|_/__/
                                      |___/ {Fore.GREEN}V2{Fore.RESET}
 {Fore.YELLOW}- >{Fore.RESET} Accidental Bug Happens find the program and report it
""")
    parser = argparse.ArgumentParser(description="FindBB Program Search")
    parser.add_argument("-web", action="store_true", help="Enable the web-based search UI")
    parser.add_argument("-d", "--domain", help="Domain to search")
    args = parser.parse_args()

    if args.domain:
        if args.domain == "":
            app.logger.warning("Please provide a domain to search using -d option.")
        else:
            domain = args.domain
            program_info = FindBBProgram().engine(domain)
            if program_info:
                print(program_info)
            else:
                app.logger.warning("No Program Found")
    elif args.web:
        app.run(host="127.0.0.1", port=5000, debug=True)
    else:
        parser.print_help()
