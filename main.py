from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
driver = webdriver.Chrome('C:/Users/***/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe',)

driver.get("https://www.linkedin.com/jobs/graphic-designer-jobs")
driver.maximize_window()
time.sleep(1)

elem = driver.find_element_by_tag_name("body")
no_of_pagedowns = 51

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    no_of_pagedowns-=1

time.sleep(20)
jobs_des=[]
base_cards= driver.find_elements_by_class_name('base-card')
for base_card in base_cards:
   base_card.click()
   time.sleep(20)
   driver.refresh()
   show_more=driver.find_element_by_class_name('show-more-less-html__button')
   show_more.click()
   time.sleep(10)
   job_details=driver.find_element_by_class_name('show-more-less-html__markup')
   jobs_des.append(job_details.text)
   time.sleep(30)

driver.close()
keep=[]
notkeep=[]

keywords = ['illustrator', 'indesign', 'photoshop','dreamweaver','exceptional creativity','innovative design','excellent communication','presentation skills','organizational','time-management','wordpress','photography','photo-editing','css','html','javascript']
for job_des in jobs_des:
    if any(word in job_des.lower() for word in keywords):
       keep.append(job_des.lower())
    else:
        notkeep.append(job_des.lower())
key_list=[]
for key in keywords :
    for ke in keep:
        if key in ke:
            key_list.append(key)

skills=[]
nums=[]
for skill in key_list:
    dam=int(skill.replace(skill,str(key_list.count(skill))))
    skills.append(skill)
    nums.append(dam)

jk=list(zip(nums,skills))
h_864=sorted(list(set(jk)))
i=0
while i<=len(h_864)-1:
    y89=h_864[i][0]
    print(str(round(int(y89)*100/len(key_list)))+"%","ask for",h_864[i][1],"skills")
    i+=1
