import time
from selenium import webdriver

# Set the path to the chromedriver executable
CHROMEDRIVER_PATH = 'path/to/chromedriver'

# Set the path to the CV PDF
CV_PATH = "path/to/cv.pdf"

# Create a new Chrome driver instance
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.implicitly_wait(0.5)
driver.maximize_window()

# Navigate to the naukri landing page
print("Opening naukri landing page...")
driver.get('https://www.naukri.com/')

# Wait for the user to login
print("Please login within 60 seconds")
time.sleep(60)

# Continuously reload and navigate to different pages
while True:
    try:
        # Wait for some time before navigating to the next page
        time.sleep(120)

        # Reload the naukri landing page
        print("Reloading naukri landing page...")
        driver.get('https://www.naukri.com/')

        # Navigate to the recommended jobs page
        time.sleep(120)
        print("Opening recommended jobs page...")
        driver.get('https://www.naukri.com/mnjuser/recommendedjobs')

        # Navigate to the recruiter mails page
        time.sleep(120)
        print("Opening view recruiter mails page...")
        driver.get('https://my.naukri.com/Inbox/viewRecruiterMails')

        # Navigate to the naukri_promo_rd page
        time.sleep(120)
        print("Opening naukri_promo_rd page...")
        driver.get('https://resume.naukri.com/resume-display?fftid=notf_nauk_promo_rd')

        # Navigate to the performance page
        time.sleep(120)
        print("Opening performance page...")
        driver.get('https://www.naukri.com/mnjuser/performance')

        # Navigate to the upload CV page
        time.sleep(120)
        print("Opening upload CV page...")
        driver.get('https://www.naukri.com/mnjuser/profile?id=&altresid')

        # Upload the CV PDF
        time.sleep(60)
        print("Starting to upload CV...")
        driver.find_element_by_id('attachCV').send_keys(CV_PATH)
        print("CV uploaded successfully!")
    except Exception as e:
        # Print any errors that occur during navigation
        print(e)
