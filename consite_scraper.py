import time
import math
import xlsxwriter
import openpyxl
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.common.keys import Keys

workbook = xlsxwriter.Workbook('tgtcat.xlsx')
worksheet = workbook.add_worksheet()
row=0
col=0

inputstr = ["tgtcggcggttcgctttttcttttttgtcgg","tgtcggtacaaaatggcacagcatttgtcgg", "tgtcggaagtcaaataacaaatctttgtcgg", "tgtcggcgatgcaattattgtcttttgtcgg", "tgtctctgtctc", "tgtcaagtgtcaa", "tgtcaaatgtcaa", "tgtcaactgtcaa", "tgtcaattgtcaa", "tgtcattgtcat", "tgtcagattgtcag", "tgtcacttgtcac", "tgtcacgtgtcac", "tgtctaatgtcta", "tgtctttgtctt", "tgtctgtttgtctg", "tgtcgctggttgctgtcgc","tgtcgagtgtcga", "tgtcgttgtcgt", "tgtccattgtcca", "tgtccttatagtccatcacaacggttcatgtcct", "tgtccttcttttctgcttctttgtcct", "tgtccttgtcct"];
MPS = "TCACTATATATAGGAAGTTCATTTCATTTGGAATGGACACGTGTTGTCATTTCTCAACAATTACCAACAACAACAAACAACAAACAACATTATACAATTACTATTTACAATTACATCTAGATAAACAATGGCTTCCTCC"

for string in inputstr:
    worksheet.write(row, col, string)
    row+=1
    driver = webdriver.PhantomJS()
    driver.get('http://consite.genereg.net/cgi-bin/consite?rm=t_input_single')
    driver.find_element_by_name("seq1").send_keys(string + MPS)
    elem = driver.find_element_by_name("submit").click()
    elem = driver.find_element_by_name(".submit").click()
    elem = driver.find_element_by_name("Image4").click()
    rows = driver.find_elements_by_xpath("/html/body/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr/td[1]")
    for a in rows:
        worksheet.write(row, col, a.text)
        row+=1
    row=0
    col+=1

workbook.close()
