# FindBB Program Search V2

FindBB Program Search is a tool designed to help you search for bug bounty programs related to a specific domain. The program utilizes various APIs and data sources to provide you with relevant bug bounty program information. It comes with both command-line and web-based interfaces for your convenience.

## Features

- Command-line Interface: Search for bug bounty programs from the command line.
- Web-based Interface: If you prefer a graphical interface, you can use the web-based search UI.
- Multiple APIs: The program uses multiple APIs and data sources to find the most comprehensive list of bug bounty programs.

## Installation

Before running the FindBB Program Search, ensure you have the necessary dependencies installed. You can install them using pip3:
```bash
pip install requests
pip install colorama
pip install flask
```

## How to Use

### Command-line Interface
<div style="text-align:center">
    <img src="https://i.ibb.co/MDj3wy5/image.png" alt="Image" />
</div>

To use the command-line interface, run the `main.py` script and provide the domain you want to search for using the `-d` option:

```bash
python findbbV2.py -d example.com
```
or to search multiple files in command line you can use the `-f` option

```bash
python findbbV2.py -f allbb.txt
```

This will search for bug bounty programs related to the domain "example.com" and provide you with the relevant program information.

### Web-based Interface
<div style="text-align:center">
    <img src="https://i.ibb.co/DKdw7sv/image.png" alt="Image" />
</div>

If you prefer a web-based interface, you can enable the web mode using the `-web` option:

```bash
python findbbV2.py -web
```

This will start the Flask web server, and you can access the search UI by opening your web browser and visiting http://127.0.0.1:5000/. Simply enter the domain you want to search for in the input field and click the "Search" button. The search result will be displayed on the same page.

## How it Works

1. The program fetches bug bounty program data from multiple APIs and data sources.
2. It uses concurrent threads to search for the domain in the program data simultaneously, making the search process faster.
3. If a matching program is found, the program information, including the URL to the bug bounty program, is displayed.

## Important Note

Please keep in mind that bug bounty programs can change frequently, and new programs can be added or existing ones may be removed. As a result, the information provided by the FindBB Program Search might not always be up-to-date.

## Contributing

If you find any issues or want to contribute to the project, you can create a pull request or open an issue on the GitHub repository.

## Disclaimer

The FindBB Program Search tool is intended for educational and informational purposes only. Always ensure that you have proper authorization before performing any security testing or bug hunting activities on websites or domains you do not own or have explicit permission to test.

Use the tool responsibly and adhere to bug bounty platform policies and ethical guidelines.

## Credits

This tool uses data from various bug bounty program APIs and data sources, and the respective credits go to the providers of those APIs and data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using FindBB Program Search! Happy bug hunting!
