import smtplib
import json

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = input("Please enter your Email(gmail) address:  ")
PASSWORD = input("Please enter your Password:  ")



def get_contacts():
    names=[]
    emails=[]
    subjects=[]
    
    with open('clients.json') as json_files:
        data = json.load(json_files)
        for i in data['clients']:
            #print(i['name'])
            #print(i['email'])
            #print(i['subject'])
                  
            names_n = [i['name']]
            names.append(names_n)

            emails_n = [i['email']]
            emails.append(emails_n)

            subjects_s = [i['subject']]
            subjects.append(subjects_s)
        
            #print(names)
            #print(emails)
            #print(subjects)

    return names, emails, subjects

"""def read_template():
    
    templates=[]

    with open('templates.json') as json_files:
        data = json.load(json_files)
        for j in data['information']:

            templates_t = [j['template']]
            templates.append(templates_t)

            #print(templates)

    return templates"""

def read_template():
    
    with open(r'C:\Users\Ayush\Desktop\New folder\template.txt', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return template_file_content


     

def main():
    names, emails, subjects = get_contacts()
    templates = read_template()
    print(templates)
    
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

   

    FROM = MY_ADDRESS
    TO = emails
    SUBJECT = subjects
    print(SUBJECT)

    
    s.sendmail(FROM, TO, templates)
        
    s.quit()

if __name__ == '__main__':
    main()

    
    

