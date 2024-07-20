const puppeteer = require('puppeteer');

(async () => {
    const targetTime = new Date('2024-07-18T11:00:00Z'); // UTC time -- Registration opens at 7:00 AM EST or (2024-07-22T11:00:00Z) in UTC

    const browser = await puppeteer.connect({
        browserURL: 'http://localhost:9222',

    });
    console.log('Connected to Browser');
    const pages = await browser.pages();
    const page = pages[0]; // Assuming login was done in the first tab

    for (let i = 1; i <= 5; i++) {
        // Open tab
        const newPage = await browser.newPage();
        await newPage.goto('https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=171958');
        

        // Time Delay
        const currentTime = new Date();
        const timeDelta = targetTime - currentTime;
        if (timeDelta > 0) {
            console.log(`Waiting for ${timeDelta / 1000} seconds until the target time.`);
            await new Promise(resolve => setTimeout(resolve, timeDelta));
        }

        // Select checkbox
        await newPage.click('#SelectAllCheckBox');

        // Click the register button
        await newPage.click('#ctl00_contentPlaceHolder_ibEnroll');

        // Wait to ensure the registration completes
        await newPage.waitForSelector('#ctl00_contentPlaceHolder_ibEnroll', { hidden: true });
        console.log("Registered(" + i + ")");
        await newPage.close();
    }
    process.exit();
})();