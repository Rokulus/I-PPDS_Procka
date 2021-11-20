*** Settings ***
Resource          resource.robot

*** Test Cases ***
Tasks
    Open Browser To Start Page
    Start
    Input Number
    Next
    Next2
    FOR    ${i}    IN RANGE    21
            IF  ${i} > 0 
                    ${j} =  Set Variable    ${i}
                    ${status}=  Catenate    SEPARATOR=    head_lblstatus  ${j}
                    ${flight_status}=   Get Text    ${status}
                    ${check} =  Catenate    SEPARATOR=    head_chk  ${j}
                    Run Keyword If      '${flight_status}' == '${ontime}'    Select Checkbox     ${check}     
            END       
    END
    Next3
    
