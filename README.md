# TLScontact Visa Appointment Availability Checker

This Python script automates checking for available visa appointment dates on the [TLScontact](https://visas-fr.tlscontact.com/) platform. It employs undetected Chrome automation, user-agent spoofing, dynamic headers, and VPN/proxy rotation to bypass anti-bot mechanisms and rate limits.

---

## 📌 Features

- ✅ **Undetected browser automation** using `undetected_chromedriver`
- 🕵️ **Randomized user-agent spoofing** via `fake_useragent`
- 🔄 **Custom HTTP headers** through `seleniumwire` interceptors
- 🌍 **VPN IP rotation** using Windscribe CLI (with optional proxy API support)
- 🔐 **Automatic login** and session simulation on TLScontact
- 🗓️ **Date scraping** for appointment availability
- 🔁 Runs every 5 minutes by default (`time.sleep(300)`)

---

## 🧰 Requirements

Ensure Python 3.7+ is installed. Then install required dependencies:

```bash
pip install selenium-wire undetected-chromedriver fake-useragent numpy
```

## 🔧 Windscribe Setup (Optional)

    Download and install Windscribe CLI from https://windscribe.com/download

Login to Windscribe via CLI:
```bash
windscribe login
```

Ensure the CLI path in the script is correct:

    w_path = r"C:\\Program Files\\Windscribe\\Windscribe-cli.exe" or the linux path

## 🛠️ Configuration

Edit the following variables in the script:
    
    username = "your_tls_username"
    password = "your_tls_password"
    
Optionally replace vpn("connect", location) with a proxy API configuration block if not using Windscribe.

## 🧪 Proxy API Option (optional)

You may replace VPN rotation with a proxy provider:
    
    API_KEY = 'your_key_here'
    s_options = {
        'proxy': {
            'http': f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
            'https': f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
            'verify_ssl': True,
        },
    }
    
Then pass s_options into your driver config.

## 📈 How It Works

- Connects to a random VPN server

- Launches an undetected Chrome session

- Spoofs headers and user-agent

- Logs into TLSContact portal

- Navigates to appointment section

- Scrapes available dates

- Disconnects VPN

- Waits 5 minutes and repeats

## ⚠️ Disclaimer

Use responsibly and ethically.

Automating appointment systems may violate TLSContact's Terms of Service.

You assume all risks for using this tool.
