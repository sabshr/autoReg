# Instructions 
1) Launch Chrome remote debugging port (replace 'sabshr' with your user folder name)
### MacOS
```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/sabshr/Library/Application Support/Google/Chrome/Default"
```
### Windows
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```

2) Log into SIS on a new tab in the opened Chrome window within the remote debugging browser
2) Adjust `targetTime` and `numberOfTabs` as needed
3) Run the program!


# Automated Course Registration Script

## Overview

This project is a Node.js script utilizing **Puppeteer** to automate the process of registering for courses on the SIS platform. The script opens multiple browser tabs in parallel, navigates to the enrollment page, and attempts to register for courses at a pre-specified time.

## Prerequisites

- **Node.js** (v12 or higher)
- **Puppeteer** installed as a dependency.
- A running instance of Chrome/Chromium with remote debugging enabled (e.g., `chrome --remote-debugging-port=9222`).

