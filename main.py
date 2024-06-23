import streamlit as st
import time

st.title('Streamlit 入門')

st.write('Display Progressbar')

'Start'
latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
  latest_iteration.text(f'Iteration {i+1} %')
  bar.progress(i + 1)
  time.sleep(0.1)
'Done'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('右カラムを表示')

expander = st.expander('問い合わせ1')
expander.write('問い合わせ内容の回答1')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ内容の回答2')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ内容の回答3')
expander = st.expander('問い合わせ4')
expander.write('問い合わせ内容の回答4')

# option = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100 ,50)
# 'あなたの趣味：', option
# 'コンディション：', condition

# if st.checkbox('Show Image'): 
#   img = Image.open('sample.jpg')
#   st.image(img, caption='sampleImage', use_column_width=True)
