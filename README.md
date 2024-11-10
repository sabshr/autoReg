# Dependencies 
- Node.js
- Chrome
- puppeteer
  
# Instructions (MacOS)
1) Launch Chrome remote debugging port (replace 'sabshr' with your user folder name)

```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/sabshr/Library/Application Support/Google/Chrome/Default"
```

# Instructions (Windows)
1) Launch Chrome remote debugging port (replace 'sabshr' with your user folder name)

```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```

1) Log into SIS on a new tab in the opened Chrome window (puppeteer intentionally runs in headed mode)
2) Set time delay (UTC Time) and adjust number of registrations as needed and run program


# Automated Course Registration Script

## Overview

This project is a Node.js script utilizing **Puppeteer** to automate the process of registering for courses on the SIS platform. The script opens multiple browser tabs in parallel, navigates to the enrollment page, and attempts to register for courses at a pre-specified time.

## Features

- Connects to a remote Chrome instance using Puppeteer.
- Opens a specified number of tabs to maximize registration attempts.
- Delays execution until the target registration time.
- Automates web actions such as clicking buttons and handling asynchronous operations.
- Logs registration status for each tab, indicating registration success or failure.

## Prerequisites

- **Node.js** (v12 or higher)
- **Puppeteer** installed as a dependency.
- A running instance of Chrome/Chromium with remote debugging enabled (e.g., `chrome --remote-debugging-port=9222`).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/registration-automation.git
   cd registration-automation
   
