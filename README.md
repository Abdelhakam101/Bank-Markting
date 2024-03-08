# Bank-Markting
# Overview
**DESCRIPTION**: 
- The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls and cellular. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

  # About Data 
## bank client data:
- __age:__(numeric)
- __job:__ type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')
- __marital:__ marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
- __education:__ (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')
- __default:__ has credit in default? (categorical: 'no','yes','unknown')
- __housing:__ has housing loan? (categorical: 'no','yes','unknown')
- __loan:__ has personal loan? (categorical: 'no','yes','unknown')

## related with the last contact of the current campaign:
- __contact:__ contact communication type (categorical: 'cellular','telephone')
- __month:__ last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
- __day_of_week:__ last contact day of the week (categorical: 'mon','tue','wed','thu','fri')
- __duration:__ last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.

## other attributes:
- __campaign:__ number of contacts performed during this campaign and for this client (numeric, includes last contact)
- __pdays:__ number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
- __previous:__ number of contacts performed before this campaign and for this client (numeric)
- __poutcome:__ outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')

## social and economic context attributes
- __emp.var.rate:__ employment variation rate - quarterly indicator (numeric)
- __cons.price.idx:__ consumer price index - monthly indicator (numeric)
- __cons.conf.idx:__ consumer confidence index - monthly indicator (numeric)
- __euribor3m:__ euribor 3 month rate - daily indicator (numeric)
- __nr.employed:__ number of employees - quarterly indicator (numeric)

## Output variable (desired target):
- __y:__ has the client subscribed a term deposit? (binary: 'yes','no')


# In this project i maked model to predict if the client subscribed a term deposit or not after some analysis
