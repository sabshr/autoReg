const puppeteer = require('puppeteer');

(async () => {
    const targetTime = new Date('2024-11-15T11:59:58Z'); // UTC time -- Use Google to convert registration time to UTC.

    
    const browser = await puppeteer.connect({
        browserURL: 'http://localhost:9222',
    });
    
    // Open tabs in parallel (numberOfTabs can be specified)
    const numberOfTabs = 20; 
    const newPages = await Promise.all(Array.from({ length: numberOfTabs }, () => browser.newPage()));


    // Delay until targetTime has been reached
    const waitUntilTargetTime = async () => {
        const currentTime = new Date();
        const timeDelta = targetTime - currentTime;
        if (timeDelta > 0) {
            console.log(`Waiting for ${timeDelta / 1000} seconds until the target time.`);
            await new Promise(resolve => setTimeout(resolve, timeDelta));
        } else {
            console.log('Target time has already passed. Running script.');
        }
    };

    await waitUntilTargetTime();


    // Parallel page loading
    await Promise.all(newPages.map(async (newPage, i) => {
        await newPage.goto('https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=171958');
        
        // Puppeteer web actions
        try {
            await newPage.click('#SelectAllCheckBox');
            await newPage.click('#ctl00_contentPlaceHolder_ibEnroll');
            try {
                await newPage.waitForSelector('#ctl00_contentPlaceHolder_ibEnroll', { hidden: true });
                console.log(`Registered(${i + 1})`);
            } catch (error) {
                console.log('Registration Failed');
            }
        } catch (error) {
            console.log('Registration Failed');
        }
        // Wait to ensure registration completes
        await newPage.close(); // might be able to remove? -- or would an excess of chrome tabs take up too much memory?? 
    }));
    process.exit();
})();