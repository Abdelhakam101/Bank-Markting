import streamlit as st 
import pandas as pd 
import plotly.express as px 
from PIL import Image
import os
import pickle


st.set_page_config(page_title="Bank Marketing",layout="wide")
add_selectbox = st.sidebar.radio(
        "Pages",
        ("Info", "Analysis", "Prediction")
)
####################################################
df=pd.read_csv("./clean data.csv")
if add_selectbox =="Info":
    image = Image.open(os.path.join(os.getcwd(),"increase-deposits.jpg"))
    st.image(image, caption='Bank Marketing') 
    st.title("Bank Marketing Model, By [Abdelhakam Ashraf](https://www.linkedin.com/in/abdelhakam-ashraf-056393258/)")
    st.markdown("--"*50)
    st.header("About Dataset:")
    st.header("Overview:")
    st.write("- __DESCRIPTION:__ The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed")

    st.subheader("bank client data:")
    st.write("- __age:__(numeric)")
    st.write("- __job:__ type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')")
    st.write("- __marital:__ marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)")
    st.write("- __education:__ (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')")
    st.write("- __default:__ has credit in default? (categorical: 'no','yes','unknown')")
    st.write("- __housing:__ has housing loan? (categorical: 'no','yes','unknown')")
    st.write("- __loan:__ has personal loan? (categorical: 'no','yes','unknown')")

    st.subheader("related with the last contact of the current campaign:")
    st.write("- __contact:__ contact communication type (categorical: 'cellular','telephone')")
    st.write("- __month:__ last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')")
    st.write("- __day_of_week:__ last contact day of the week (categorical: 'mon','tue','wed','thu','fri')")
    st.write("- __duration:__ last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.")

    st.subheader("other attributes:")
    st.write("- __campaign:__ number of contacts performed during this campaign and for this client (numeric, includes last contact)")
    st.write("- __pdays:__ number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)")
    st.write("- __previous:__ number of contacts performed before this campaign and for this client (numeric)")
    st.write("- __poutcome:__ outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')")

    st.subheader("social and economic context attributes:")
    st.write("- __emp.var.rate:__ employment variation rate - quarterly indicator (numeric)")
    st.write("- __cons.price.idx:__ consumer price index - monthly indicator (numeric)")
    st.write("- __cons.conf.idx:__ consumer confidence index - monthly indicator (numeric)")
    st.write("- __euribor3m:__ euribor 3 month rate - daily indicator (numeric)")
    st.write("- __nr.employed:__ number of employees - quarterly indicator (numeric)")

    st.subheader("Output variable (target):")
    st.write("- __y:__ has the client subscribed a term deposit? (binary: 'yes','no')")
    
    st.markdown("[Link data](https://data.world/data-society/bank-marketing-data)")
    st.markdown("--"*50)

    st.markdown("This is the sample of dataframe :")
    sample=st.dataframe(df.sample(25))
    btn=st.button("Display another sample")
    if btn:
        print(sample)
    st.markdown("-----------------------------------")
#################################################################
    

if add_selectbox =="Analysis": 
    tab_overall_vision,tab_Business_Questions ,tab_conclusion = st.tabs(['Columns Overall ','Business Questions','Conclusion'])
    with tab_overall_vision :
        st.title('Here i will show Some statistcs for each column and correlation between some columns:')
        col = st.selectbox('select column you interest', df.select_dtypes(include="O").columns.to_list()+['age', 'duration', 'campaign', 'pdays', 'previous'])

        # creat function to countplot graph
        #(name of data , value of x_axis , valu of y_axes,hue , name of xaxes , name of y_axis , name for this histograme)
        def histogram(data , x , y , color ,x_axes,y_axes , title,barnorm=None): 
            fig = px.histogram(data_frame=data , x=x, y=y,
                        color=color,
                        barmode='group',
                        barnorm=barnorm,
                        text_auto=True ,
                        title=title)
            fig.update_layout(width=1000, height=600)
            fig.update_yaxes(title_text=y_axes)
            fig.update_xaxes(title_text=x_axes)
            fig.update_layout(title= {'y': 0.9, 'x': 0.5,'xanchor': 'center', 'yanchor': 'top'},
                            xaxis={'categoryorder':'total descending'})
            return fig 
        if col == 'job':
            st.plotly_chart(histogram(df,x='job',y=None,color=None ,
                    x_axes='job',
                    y_axes='count',
                    title='Histogram for job count'))
            
        elif col == 'marital':
            st.plotly_chart(histogram(df,x='marital',y=None,color=None ,
                    x_axes='marital',
                    y_axes='count',
                    title='Histogram for marital count'))
        
        elif col == 'education':
            st.plotly_chart(histogram(df,x='education',y=None,color=None ,
                    x_axes='education',
                    y_axes='count',
                    title='Histogram for education count'))
            
        elif col == 'default':
            st.plotly_chart(histogram(df,x='default',y=None,color=None ,
                    x_axes='default',
                    y_axes='count',
                    title='Histogram for default count'))
            
        elif col == 'housing':
            st.plotly_chart(histogram(df,x='housing',y=None,color=None ,
                    x_axes='housing',
                    y_axes='count',
                    title='Histogram for housing count'))
            
        elif col == 'loan':
            st.plotly_chart(histogram(df,x='loan',y=None,color=None ,
                    x_axes='loan',
                    y_axes='count',
                    title='Histogram for loan count'))


        elif col == 'contact':
            st.plotly_chart(histogram(df,x='contact',y=None,color=None ,
                    x_axes='contact',
                    y_axes='count',
                    title='Histogram for contact count'))
            
        elif col == 'month':
            st.plotly_chart(histogram(df,x='month',y=None,color=None ,
                    x_axes='month',
                    y_axes='count',
                    title='Histogram for month count'))
            

        elif col == 'day_of_week':
            st.plotly_chart(histogram(df,x='day_of_week',y=None,color=None ,
                    x_axes='day_of_week',
                    y_axes='count',
                    title='Histogram for day_of_week count'))
            

        elif col == 'poutcome':
            st.plotly_chart(histogram(df,x='poutcome',y=None,color=None ,
                    x_axes='poutcome',
                    y_axes='count',
                    title='Histogram for poutcome count'))
            

        elif col == 'quarter':
            st.plotly_chart(histogram(df,x='quarter',y=None,color=None ,
                    x_axes='quarter',
                    y_axes='count',
                    title='Histogram for quarter count'))
            

        elif col == 'age_group':
            st.plotly_chart(histogram(df,x='age_group',y=None,color=None ,
                    x_axes='age_group',
                    y_axes='count',
                    title='Histogram for age_group count'))
            
        elif col == 'age':
            st.plotly_chart(histogram(df,x='age',y=None,color=None ,
                    x_axes='age',
                    y_axes='count',
                    title='Histogram for age count'))


        elif col == 'y':
            st.plotly_chart(histogram(df,x='y',y=None,color=None ,
                    x_axes='y',
                    y_axes='count',
                    title='Histogram for target count'))
            

        elif col == 'duration':
            st.plotly_chart(histogram(df,x='duration',y=None,color=None ,
                    x_axes='duration',
                    y_axes='count',
                    title='Histogram for duration count'))
            
        elif col == 'campaign':
            st.plotly_chart(histogram(df,x='campaign',y=None,color=None ,
                    x_axes='campaign',
                    y_axes='count',
                    title='Histogram for campaign count'))
            
        elif col == 'pdays':
            st.plotly_chart(histogram(df,x='pdays',y=None,color=None ,
                    x_axes='pdays',
                    y_axes='count',
                    title='Histogram for pdays count'))
            
        elif col == 'previous':
            st.plotly_chart(histogram(df,x='previous',y=None,color=None ,
                    x_axes='previous',
                    y_axes='count',
                    title='Histogram for previous count'))
            
        elif col == 'emp_var_rate':
            st.plotly_chart(histogram(df,x='emp_var_rate',y=None,color=None ,
                    x_axes='emp_var_rate',
                    y_axes='count',
                    title='Histogram for emp_var_rate count'))
            
        st.markdown("--"*50)

        col = st.selectbox('select column you interest', ['age', 'duration', 'campaign', 'emp_var_rate',
        'cons_price_idx', 'cons_conf_idx', 'euribor3m'])
        def box (df , x ,title):
            fig = px.box(data_frame=df , x=x ,title=title)
            return fig 
        if col == 'age' :
            st.plotly_chart(box(df , x='age' ,
                                title= 'Variation in age' ))
        elif col == 'duration' :    
            st.plotly_chart(box(df , x='duration' ,
                                title= 'Variation in duration' ))
        elif col == 'campaign' :   
            st.plotly_chart(box(df , x='campaign' ,
                                title= 'campaign in age' ))
            
        elif col == 'emp_var_rate' :
            st.plotly_chart(box(df , x='emp_var_rate' ,
                                title= 'Variation in emp_var_rate' ))
        elif col == 'cons_price_idx' :   
            st.plotly_chart(box(df , x='cons_price_idx' ,
                                title= 'Variation in cons_price_idx' ))
        elif col == 'cons_conf_idx' :   
            st.plotly_chart(box(df , x='cons_conf_idx' ,
                                title= 'Variation in cons_conf_idx' ))
        elif col == 'euribor3m' :    
            st.plotly_chart(box(df , x='euribor3m' ,
                                title= 'Variation in euribor3m' ))
        st.markdown("--"*50)

        st.subheader('correlation between the columns ')
        st.plotly_chart(px.imshow(df.corr().round(3),
                                  text_auto=True,
                                  color_continuous_scale='Blues'))
        st.markdown("- __Note:__ there is high correlation between __euribor3m__ and  __nr_employed__ ")
        st.markdown("- __Note:__ there is high correlation between __euribor3m__ and __emp_var_rate__")
        st.markdown("- __Note:__ there is high correlation between __emp_var_rate__ and __nr_employed__")
        st.markdown("- __Note:__ there is high correlation between __emp_var_rate__ and __cons_price_idx__")
        st.markdown("--"*50)

        st.subheader("scatter plot to show the correlation between euribor3m and emp_var_rate")
        st.plotly_chart(px.scatter(df, y='euribor3m' , x='emp_var_rate'))
        st.markdown("- __Note:__ we can say there is positive corrletion")
        st.markdown("--"*50)


        # group for each month with mean to cons_price_idx
        st.subheader("line plot to each month with cons_price_idx")
        dff = df.groupby('month')['cons_price_idx'].mean().reset_index()
        st.plotly_chart(px.line(dff , x='month' , y='cons_price_idx',title='change cons_price_idx with month'))
        st.markdown("- the best month is __dec__ because it has little value with cons_price_idx")
        st.markdown("--"*50)

        # group for each month with mean to cons_price_idx
        st.subheader("line plot to each month with cons_conf_idx")
        dff = df.groupby('month',as_index=False)['cons_conf_idx'].mean()
        st.plotly_chart(px.line(dff , x='month' , y='cons_conf_idx',title='change cons_conf_idx with month'))
        st.markdown("- actully dec is the higher cons_conf_idx because it has little value with cons_price_idx")
        st.markdown("--"*50)


########################################################################
    with tab_Business_Questions :
        st.title("These are the questions I concluded from the analysis:")
        st.subheader("The information in this tab can answer the following questions :")
        st.write('1-Does age influence subscription to a term deposit?')
        st.write('2-What is the distribution of job types among clients who subscribed to a term deposit?')
        st.write('3-What is the distribution of target across different levels of education?')
        st.write('4-What is the distribution of target across marital?')
        st.write('5-Is there a relationship between housing loan status and subscription to a term deposit?')
        st.write('6-Is there a relationship between personal loan status and subscription to a term deposit?')
        st.write('7-What is the distribution of target across contact status?')
        st.write('8-How does the number of contacts performed before this campaign relate to the subscription to a term deposit?')
        st.markdown("--"*70)


        st.header('1-Does age influence subscription to a term deposit?')
        col1,col2,col3=st.columns([5,2,5])
        with col1 :
            st.plotly_chart(histogram(data = df 
         ,x= df.age_group, y=None 
         ,color='y' 
         ,x_axes='age_group' ,
         y_axes='count',
         title="Histogram for Age Group with Color by Target Column" ))
        with col3 :
            st.plotly_chart(histogram(data = df 
         ,x= df.age_group, y=None 
         ,color='y' ,
         barnorm='percent'
         ,x_axes='age_group' ,
         y_axes='percentage',
         title="Histogram for Age Group with Color by Target Column" ))
        st.markdown("- __Note:__ i expect you may be care about [15-29 , 30-39 ] intervals")
        st.markdown("--"*70)



        st.header("What is the distribution of job types among clients who subscribed to a term deposit?")
        col1,col2,col3=st.columns([5,2,5])
        with col1 :
            st.plotly_chart(histogram(data = df 
         ,x= df.job, y=None 
         ,color='y' 
         ,x_axes='job' ,
         y_axes='count',
         title="Histogram for job with Color by Target Column" ))
        with col3 :
            st.plotly_chart(histogram(data = df 
         ,x= df.job, y=None 
         ,color='y' ,
        barnorm='percent'
         ,x_axes='job' ,
         y_axes='percentage',
         title="Histogram for job with Color by Target Column" ))
        st.markdown("- __Note:__ Admin are the most job subscribed to a term deposit")
        st.markdown("--"*70)

        st.header("What is the distribution of target across different levels of education?")
        st.plotly_chart(histogram(data = df 
         ,x= df.education, y=None 
         ,color='y' 
         ,x_axes='education' ,
         y_axes='count',
         title="Histogram for education with Color by Target Column" ))
        st.markdown("- __Note:__ care about Among individuals with a university degree")
        st.markdown("--"*70)


        st.header("What is the distribution of target across marital?")
        st.plotly_chart(px.sunburst(df , path=['marital' , 'y']))
        st.markdown("- __Note:__ i expect marital status don't affect on the target")
        st.markdown("--"*70)


        st.header('Is there a relationship between housing loan status and subscription to a term deposit?')
        st.plotly_chart(histogram(data = df 
         ,x= df.housing, y=None 
         ,color='y' ,
         barnorm='percent'
         ,x_axes='housing' ,
         y_axes='percentage',
         title="Histogram for housing with Color by Target Column" ))
        st.markdown("- __Note:__ if you have housing loan or not that's not affect on target")
        st.markdown("--"*70)

        st.header("Is there a relationship between personal loan status and subscription to a term deposit?")
        st.plotly_chart(histogram(data = df 
         ,x= df.loan, y=None 
         ,color='y' ,
         barnorm='percent'
         ,x_axes='loan' ,
         y_axes='percentage',
         title="Histogram for housing with Color by Target Column" ))
        st.markdown("- __Note:__ if you have personal loan or not that's not affect on target")
        st.markdown("--"*70)


        st.header("What is the distribution of target across contact status?")
        st.plotly_chart(histogram(data = df 
         ,x= df.contact, y=None 
         ,color='y' ,
         barnorm='percent'
         ,x_axes='contact' ,
         y_axes='percentage',
         title="Histogram for contact with Color by Target Column" ))
        st.markdown("- __Note:__ I think cellular campaign better than telephone campaign")
        st.markdown("--"*70)


        st.header("How does the number of contacts performed before this campaign relate to the subscription to a term deposit?")
        st.plotly_chart(histogram(data = df 
         ,x= df.previous, y=None 
         ,color='y' ,
         barnorm='percent'
         ,x_axes='previous' ,
         y_axes='percentage',
         title="Histogram for previous with Color by Target Column" ))
        st.markdown("- __Note:__ There are those among the people you spoke with at the previous campaign they agreed now ")
        st.markdown("--"*70)
##################################################################################################################################
    with tab_conclusion :
        st.title("After Analysis")
        st.header("my recommendation to improve this business target or to gain customers subscribers do:")
        st.write("- You may be care about __[15-29 , 30-39 ]__ intervals")
        st.write("- Concentrate with the people who work as a __Admin__ ")
        st.write("- Care about Among individuals with a __university degree__")
        st.write("- I think cellular campaign better than telephone campaign")
        st.write("- contacting the customers who have been in contact with them but have not signed up for bank services in previous campaigns")

        st.header("My analysis shows that some columns don't have the effect on the target such as:")
        st.write("- marital status don't affect on the target")
        st.write("- if individual has housing loan or not that's not affect on target")
        st.write("- personal loan status not affect on target")

#########################################################################
if add_selectbox == "Prediction":
    model = pickle.load(open('model.pkl', 'rb'))
    inputs = pickle.load(open('inputs.pkl','rb'))
    #inputs 
    def prediction(age ,job ,marital ,education, housing,
                    loan, contact, month, day_of_week, pdays, previous,
                    emp_var_rate,cons_price_idx,cons_conf_idx,euribor3m
                    ,nr_employed):
            
        df= pd.DataFrame(columns=inputs)

        df.at[0, 'age'] = age
        df.at[0, 'job'] = job
        df.at[0, 'marital'] = marital
        df.at[0, 'education'] = education
        df.at[0, 'housing'] = housing
        df.at[0, 'loan'] = loan
        df.at[0, 'contact'] = contact
        df.at[0, 'month'] = month
        df.at[0, 'day_of_week'] = day_of_week
        df.at[0,'pdays'] = pdays
        df.at[0, 'previous'] = previous
        df.at[0, 'emp_var_rate'] = emp_var_rate
        df.at[0, 'cons_price_idx'] = cons_price_idx
        df.at[0, 'cons_conf_idx'] = cons_conf_idx
        df.at[0, 'euribor3m'] = euribor3m
        df.at[0, 'nr_employed'] = nr_employed


        def modify_age (x):
            if x in range(15,30):
                return '15-29'
            elif x in range(30 , 40):
                return '30-39'
            elif x in range (40,50):
                return '40-49' 
            elif x in range (50,60):
                return '50-59'
            elif x in range (60,81):
                return '60-80'
            
        df.at[0,'age_group']  = df.age.apply(modify_age)[0]

        

        res = model.predict_proba(df)[0]
        return res[1]

    def main():
        age = st.number_input('age', 15 , 90)
        job = st.selectbox('job',['housemaid', 'services', 'admin.', 'blue-collar', 'technician',
                                    'retired', 'management', 'unemployed', 'self-employed',
                                    'entrepreneur', 'student'])
        marital = st.selectbox('marital', ['married', 'single',])
        education = st.selectbox('education', ['Basic education' ,'university.degree' ,'high.school' ,'professional.course' ,'illiterate' ])
        housing = st.selectbox('housing', ['no', 'yes'])
        loan = st.selectbox('loan', ['no', 'yes'])
        contact = st.selectbox('contact', ['telephone', 'cellular'])
        month = st.selectbox('month', ['may', 'jun', 'jul', 'aug', 'oct', 'nov', 'dec', 'mar', 'apr','sep'])
        day_of_week = st.selectbox('day_of_week',['mon', 'tue', 'wed', 'thu', 'fri'])
        pdays = st.slider('pdays', min_value=0, max_value=50, step=1)
        previous = st.slider('previous', min_value=0, max_value=10, step=1)
        emp_var_rate = st.number_input('emp_var_rate',-10 , 10)
        cons_price_idx = st.number_input('cons_price_idx')
        cons_conf_idx = st.number_input('cons_conf_idx',)
        euribor3m = st.number_input('euribor3m',3,20)
        nr_employed = st.number_input('nr_employed',)



        if st.button('Predict'):
            res = prediction(age ,job ,marital ,education, housing,
                    loan, contact, month, day_of_week, pdays, previous,
                    emp_var_rate,cons_price_idx,cons_conf_idx,euribor3m
                    ,nr_employed)
        
            if res >= 0.13 :
                st.success('This client will subscribed to a term deposit')
            else :
                st.error('This client will not subscribed to a term deposit')
    main()
