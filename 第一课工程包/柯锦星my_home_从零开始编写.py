'''我的主页'''
import streamlit as st
import PIL
from streamlit_drawable_canvas import st_canvas
from PIL import Image

#st(background_image = Image.open("宇宙.gif"))

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区', '我的网页推荐'])

def page_1():
    '''我的兴趣推荐'''
    st.write("音乐推荐")
    with open(r'C:\Users\DELL\Desktop\第一课工程包\知更鸟、HOYO-MiX、Chevy - 在银河中孤独摇摆.mp3', "rb") as f:
        mymp3 = f.read()
        st.audio(mymp3, format="audio/mp3", start_time=0)
    with open(r'C:\Users\DELL\Desktop\第一课工程包\village people - Y.M.C.A. (Single Version).mp3', "rb") as f:
        mp3 = f.read()
        st.audio(mp3, format="audio/mp3", start_time=0)

    st.image("w700d1q75cms.jpg")
    st.write("特朗普遇刺！击中右耳")
    st.image("t046802595ed12354f9.jpg")
    st.write("特朗普支持率70%，拜登支持率13%。")
    st.write("拜登将何去何从？")
    pass

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))

    def img_change(img):
        width,height = img.size
        img_array = img.load()
        for x in range(width):
            for y in range(height):
                r = img_array[x,y][0]
                g = img_array[x,y][1]
                b = img_array[x,y][2]
                img_array[x,y] = (b,g,r)
    pass

def page_3():
    '''我的智慧词典'''
    st.write('智慧词典')

    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')

    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')

    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]

    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')

    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])

    word = st.text_input('请输入要查询的单词')

    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')

def page_4():
    '''我的留言区'''
    st.write('我的留言区')

    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '人':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '外星人':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['人', '外星人'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):

            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
def page_5():
    '''我的网页推荐'''
    st.write('我的网页推荐')
    st.write('-----------------------------')
    st.write('B站：https://www.bilibili.com/')
    st.write('NCT网址：https://nct-test.com/')
    st.write('爱奇艺：https://www.iqiyi.com/')
    st.write('抖音：https://www.douyin.com/')
    st.write('编程猫社区：https://shequ.codemao.cn/')


    
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的网页推荐':
    page_5()
