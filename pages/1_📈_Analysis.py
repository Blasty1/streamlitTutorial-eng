import streamlit as st
from sqlalchemy import text
from utils.utils import *
import pandas as pd
def create_products_tab(products_tab):
    col1,col2,col3 = products_tab.columns(3)
    query = text("SELECT AVG(amount) as AveragePay, SUM(amount) as TotalPay, Max(amount) as MaxPay FROM payments;")
    result = execute_query(st.session_state['connection'],query)
    paymentAggregates = [dict(zip(result.keys(), row)) for row in result] #to create a structure
    with col1:
        col1.metric('Average Payement','$ ' + compact_format(paymentAggregates[0]['AveragePay']))
    with col2:
        col2.metric("Total Payement",'$ ' + compact_format(paymentAggregates[0]['TotalPay']))
    with col3:
        col3.metric("Max Payement",'$ ' + compact_format(paymentAggregates[0]['MaxPay']))
#each tab has a separate function

    with products_tab.expander('Product Overview',True):
        subcol1, subcol2 = st.columns(2)

        with subcol1:
            sortedby = subcol1.radio("Sort by:",['code','name','quantity','price'])
        with subcol2:
            orderMode = subcol2.selectbox('Order:',('Ascending','Descending'))
        conversion = {
            'code' : 'productCode',
            'name' : 'productName',
            'price' : 'buyPrice',
            'quantity' : 'quantityInStock',
            'Ascending' : 'ASC',
            'Descending' : 'DESC'
        }

        if st.button('Show',type='primary'):
            querybase = f'SELECT * FROM products ORDER BY {conversion[sortedby]} {conversion[orderMode]}'
            data = pd.DataFrame(execute_query(st.session_state['connection'],text(querybase)))
            st.dataframe(data,use_container_width=True)

    with products_tab.expander('Payment',False):
        dates = execute_query(st.session_state['connection'],text("SELECT MIN(paymentDate) AS minDate , MAX(paymentDate) AS maxDate FROM payments"))
        date = [dict(zip(dates.keys(), row)) for row in dates] #to create a structure

        interval_date = st.date_input("Select the data range:",value=(date[0]['minDate'],date[0]['maxDate']),min_value=date[0]['minDate'],max_value=date[0]['maxDate'])

        if len(interval_date) >= 2:
            query = f"SELECT paymentDate, SUM(amount) AS TotalAmount FROM payments WHERE paymentDate > '{interval_date[0]}' AND paymentDate < '{interval_date[1]}'GROUP BY paymentDate;"
            payments = pd.DataFrame(execute_query(st.session_state['connection'],text(query)))
            if payments.empty:
                st.warning('There are no payments')
            else:
                payments['TotalAmount'] = payments['TotalAmount'].astype(float)
                payments['paymentDate'] = pd.to_datetime(payments['paymentDate'])
                st.line_chart(payments,x='paymentDate',y='TotalAmount')
            st.write('Test')
def create_staff_tab(staff_tab):
    col1,col2 = staff_tab.columns(2)
    query = 'SELECT firstName , lastName FROM employees WHERE jobTitle = '
    with col1:
        president= execute_query(st.session_state['connection'],text(query + "'President'")).mappings().first()
        col1.markdown(f'#### :blue[President:] {president["firstName"]} {president["lastName"]}')
    with col2:
        vp = execute_query(st.session_state['connection'],text(query + "'VP Sales'")).mappings().first()
        col2.markdown(f'#### :orange[VP SALES:] {vp["firstName"]} {vp["lastName"]}')
    query = 'SELECT jobTitle , COUNT(*) AS TotalForRole FROM employees GROUP BY jobTitle'
    results = pd.DataFrame(execute_query(st.session_state['connection'],text(query)))
    staff_tab.bar_chart(results,x = 'jobTitle', y = 'TotalForRole')
if __name__ == "__main__":
    st.title("📈 Analysis")

    # creation of separate tabs
    products_tab, staff_tab, customers_tab = st.tabs(["Products", "Staff", "Customers"])

    if check_connection():
        create_products_tab(products_tab)
        create_staff_tab(staff_tab)

