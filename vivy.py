#upcoming 18090 due on 5th March
# upcoming 40000 due on 20th March
print("""
                             *****************************************************************
                             *****************************************************************
                             ***     xxxxxxx xx     xx xxxxxx  xxx   xxx xxxxxxx xxxxxxx   *** 
                             ***   xxxxx     xxx   xxx xx  xxx xxx   xxx xx      xx   xxx  ***
                             ***  xxxx        xxxxxxx  xx  xxx xxxxxxxxx xxxxxxx xx   xxx  ***
                             ***  xxxx          xxx    xxxxxx  xxxxxxxxx xxxxxxx xxxxxx    ***
                             ***   xxxxx        xxx    xxx     xxx   xxx xx      xx   xx   ***
                             ***     xxxxxxx  t  xxx    xxx     xxx   xxx xxxxxxx xx    xx  ***
                             *****************************************************************
                             *****************************************************************

""")

allowed_emails = ["tyrooncooper@gmail.com", #1
                  "wesleydavis910@gmail.com"               
                  ]

while True:
  number= input("enter the email number:")
  ref_time=input("Enter refresh seconds:")
  ref_time = float(ref_time)
  if number=="1":
    email="tyrooncooper@gmail.com"
    passw="Joseck@2022"
    if email not in allowed_emails:
      print("this email is not registered, please try again.")
    if email in allowed_emails:
      print("proceeding..")
      break
    if email not in allowed_emails:
      print("this email is not registered, please try again.")
    if email in allowed_emails:
      print("proceeding..")
      break
  elif number=="2":
    email="wesleydavis910@gmail.com"
    passw="Vivian2022@"
    if email not in allowed_emails:
      print("this email is not registered, please try again.")
    if email in allowed_emails:
      print("proceeding..")
      break
    if email not in allowed_emails:
      print("this email is not registered, please try again.")
    if email in allowed_emails:
      print("proceeding..")
      break
  elif number=="3":
    email="janetmammi55@outlook.com"
    passw="Dk?123456"
    if email not in allowed_emails:
      print("this email is not registered, please try again.")
    if email in allowed_emails:
      print("proceeding..")
      break
    if email not in allowed_emails:
      print("this email is not registered, please try again.")
    if email in allowed_emails:
      print("proceeding..")
      break


def sort(i):
    return i[0:9]
allowed_emails = list(map(sort,allowed_emails))
from selenium.webdriver.support import expected_conditions as ec
import undetected_chromedriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
key = Keys.CONTROL + Keys.ENTER
import random
import time
links_already_clicked = []
NewsJobsWillBeUploaded = ec.visibility_of_element_located((By.XPATH,"//*[@id=\"main\"]/div[4]/div[2]/div/div/div/h1"))
AutomatedToolsShouldNotBeUsed = ec.visibility_of_element_located((By.XPATH,"//*[@id=\"main\"]/div[3]/div/div[2]/p"))
JobsWaitingForEditing = ec.visibility_of_element_located((By.XPATH,"//*[@id=\"main\"]/div[4]/div[2]/div/div/div/div[1]/div[1]/h4/span"))
Page2loaded = ec.visibility_of_element_located((By.XPATH,"//*[@id=\"main\"]/div[4]/div[2]/div/div/div/div[2]/div/ul/li[4]/span"))
Page2Nothing = ec.visibility_of_element_located((By.LINK_TEXT,"Nothing found for your query"))
RateLimit = ec.visibility_of_element_located((By.XPATH,"//*[@id=\"main\"]/div[4]/div[2]/div/div/div/button"))
page2link = "//*[@id=\"main\"]/div[4]/div[2]/div/div/div/div[2]/div/ul/li[2]/a"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options, use_subprocess=True)
driver.get("https://users.verbit.co")
time.sleep(4)
url = driver.current_url
print(url)

'''from email.message import EmailMessage
import ssl
import smtplib

class Email_Sender():
    def __init__(self, user):
        self.user = user
        self.email_sender = "pythonemailsendv@gmail.com"
        self.password = "tlzinpseuczyydmj"
        self.email_reciever = "shawnbrown2002n@gmail.com"
        self.body = f"the current {user} is using a bot registered for Kevin black; {email}"
    def send_mail(self):
        em = EmailMessage()
        em["From"] = self.email_sender
        em["To"] = self.email_reciever
        em["subject"] = f"issue partaining bot registered for Kevin black for email; {email}"
        em.set_content(self.body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as smtp:
            smtp.login(self.email_sender,self.password)
            smtp.sendmail(self.email_sender,self.email_reciever, em.as_string())'''
try:
    if url == "https://users.verbit.co/" or url == "https://users.verbit.co/?redirect_to=https%3A%2F%2Fplatform.verbit.co%2F":
        wait = WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH,"//*[@id=\"root\"]/div/div/div[2]/form/button")))
        driver.find_element("xpath","//*[@id=\"root\"]/div/div/div[2]/form/div[1]/div[2]/input").send_keys(email)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/div[2]/form/button").click()
        try:
            wait = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,"//*[@id=\"root\"]/div/div/div[2]/p")))
            driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/div[2]/form/div[2]/div[2]/input").send_keys(passw)
            time.sleep(2)
            driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/div[2]/form/button").click()
        except:
            print("huh!!")
    elif url == "https://platform.verbit.co/":
            print("already logged in, proceeding")
except:
    print("unable to log in")



acceptable_pay = [0,15,16,19,20,23,24,25,28,29,30,35,40,50]

def tab_new(url):
    driver.execute_script(f"var win = window.open('{url}', '_blank'); ")
    
main_tab  = driver.current_window_handle
def click_event():
    Pay_Obj = driver.find_element("xpath","//tbody").find_elements(By.CSS_SELECTOR,".col-sm-2")
    for n in Pay_Obj:
        pay = int(n.text.replace(" ¢/min",""))
        alink = n.find_element(By.TAG_NAME, "a")
        link = alink.get_attribute("href")
        if (link not in links_already_clicked) and (pay in acceptable_pay):
            tab_new(link)
            links_already_clicked.append(link)
    driver.switch_to.window(main_tab)
def automated_tools_breaker():
    while True:
        try:
            url = driver.current_url
            if url == "https://platform.verbit.co/request_limit.html":
                waittime = float("%.2f" % (random.random() * 10 + 15))
                print(f'Automated tools message intercepted, waiting {waittime} secs...')
                wait = WebDriverWait(driver, 60,0.01).until(
                    ec.visibility_of_element_located((By.XPATH, "//*[@id=\"request_limit_back\"]")))
                time.sleep(waittime)
                driver.get("https://platform.verbit.co/")
            elif "https://platform.verbit.co" in url:
                wait = WebDriverWait(driver, 20, 0.01).until(ec.any_of(JobsWaitingForEditing, NewsJobsWillBeUploaded))
                break
        except:
            print("trying different diagnostics")
            continue
    return "automated tools message broken"

def table2():  
    try:
        page2presence = driver.find_element(By.XPATH, page2link).is_displayed()
    except:
        page2presence = False

    if page2presence:
            driver.find_element("xpath",page2link).click()
            try:
                wait = WebDriverWait(driver, 15,0.01).until(ec.any_of(Page2loaded, Page2Nothing))
                if wait.text == "Nothing found for your query":
                    return
                click_event()
            except:
                return "page 2 is taking too long to load"
print("Please login with your credentials")

#mails_already_sent = []
start = time.perf_counter()

while True:
    stop = time.perf_counter()
    if (stop - start) > 43200:
        driver.quit()
        print("you have run the bot for 12 hours. Please restart it...")
    refresh_time = float("%.2f"%(ref_time))
    time.sleep(refresh_time)
    myurl = driver.current_url
    try:
        user = driver.find_element(By.XPATH,"//*[@id=\"content-wrapper\"]/header/ul/li[7]/span/a")
        use = user.text[0:9].strip()
        print("your email is {}:".format(use))
        if "https://platform.verbit.co/" in myurl: 
            if  use in allowed_emails:
                driver.refresh()
                wait = WebDriverWait(driver, 30, 0.01).until(ec.any_of(JobsWaitingForEditing,NewsJobsWillBeUploaded,AutomatedToolsShouldNotBeUsed,RateLimit))
                if wait.text == "Jobs waiting for editing":
                    click_event()
                    table2()
                elif wait.text == "New jobs will be uploaded shortly":
                    continue
                elif wait.text == "Automated tools should not be used in our system":
                    print(automated_tools_breaker())
                    try:
                        click_event()
                    except:
                        print("no jobs")
                elif wait.text == "Retry":
                    time.sleep((refresh_time * 6))
            '''if use not in allowed_emails and use != "":
                if use not in mails_already_sent:
                    email = Email_Sender(user.text)
                    email.send_mail()
                    mails_already_sent.append(use)
                else:
                    print("Please register a bot for this account")
                    time.sleep(5)
                    driver.quit()
                    quit()'''
    except:
        time.sleep(3)
        continue
