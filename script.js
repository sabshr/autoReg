const puppeteer = require('puppeteer');

(async () => {
    const targetTime = new Date('2024-07-18T11:00:00Z'); // UTC time -- Registration opens at 7:00 AM EST or (2024-07-22T11:00:00Z) in UTC

    
    const browser = await puppeteer.connect({
        browserURL: 'http://localhost:9222',
    });
    

    // Open tabs in parallel
    const numberOfTabs = 10; // TO EDIT LATER - not sure if I want to run a script that opens the tabs in parallel or in series...
    const newPages = await Promise.all(Array.from({ length: numberOfTabs }, () => browser.newPage()));


    // Haven't tested delay mechanism yet...
    const waitUntilTargetTime = async () => {
        const currentTime = new Date();
        const timeDelta = targetTime - currentTime;
        if (timeDelta > 0) {
            console.log(`Waiting for ${timeDelta / 1000} seconds until the target time.`);
            await new Promise(resolve => setTimeout(resolve, timeDelta));
        }
    };
    await waitUntilTargetTime();


    // Parallel page loading
    await Promise.all(newPages.map(async (newPage, i) => {
        await newPage.goto('https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=171958');
        
        // Puppeteer web actions
        await newPage.click('#SelectAllCheckBox');
        await newPage.click('#ctl00_contentPlaceHolder_ibEnroll');

        // Wait to ensure registration completes
        await newPage.waitForSelector('#ctl00_contentPlaceHolder_ibEnroll', { hidden: true });
        console.log(`Registered(${i + 1})`);
        await newPage.close(); // might be able to remove? -- or would an excess of chrome tabs take up too much memory??
    }));


    process.exit();
})();