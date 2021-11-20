*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${SERVER}         http://loadrunnertips.com/LoadRunner_Correlation_Challenge_Mod.aspx
${BROWSER}        Chrome
${DELAY}          0
${number}         0
${flight_status}  0
${status}         0
${j}              0
${ontime}         On Time
${check}          0  

*** Keywords ***
Open Browser To Start Page
    Open Browser    ${SERVER}    ${BROWSER}
    Set Selenium Speed    ${DELAY}

Start
    Click Button    head_btnStart

Input Number
    ${number}=    Get Text    head_lblMagicno 
    Input Text    head_txtMacigNo    ${number}

Next
    Click Button    head_btnNext

Next2
    Click Button    Button1

Next3
    Click Button    head_btnNext3

