from awos_data_view import show_message, size_center
from tkinter import *
import tkinter.messagebox as messagebox
import time


# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def data_view():
    from awos_data_view import data_view
    win = Toplevel()
    data_view.ViewRoot(win)


def monitor():
    from awos_data_view import monitor
    win = Toplevel()
    monitor.Monitor(win)


def vis_rvr():
    ack = messagebox.askyesno('WARNING', '请注意，此定制功能在后续的版本中可能存在不兼容的问题，\n'
                                         '下一个大版本发布，或将不再支持此功能，如需要稳定版本，\n'
                                         '访问独立发行版：https://github.com/ilxir/vis_tab\n'
                                         '点击\'Yes\'知道风险并继续，\n点击\'No\'退出功能')
    if ack:
        from awos_data_view import vis_rvr
        win = Toplevel()
        vis_rvr.VisRoot(win)
    else:
        pass


def get_time():
    """
    ——以HHMMSS DDMMYY的格式更新时间，每1000毫秒更新一次

    :return: 无
    """
    var_time.set(time.strftime('%H:%M:%S %d/%m/%y'))  # 获取当前时间
    if tk:
        tk.after(1000, get_time)  # 每隔1s调用函数自身获取时间


def close_tk():
    # tkinter.messagebox.showwarning(title='警告', message='刚才你点击了关闭按钮,程序将退出！')
    print(tk.title() + ' is destroyed!')
    tk.destroy()
    exit('Goodbye!')


def please_wait():
    show_message(title='敬请期待！',
                 text='更多功能正在开发中，敬请期待！\n'
                      '可根据需求定制，欢迎来电咨询。\n'
                      '联系人：扬泰机场气象台预报室。\n'
                      '合作咨询电话：0514-86100220',
                 mode='info')


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    tk = Tk()
    tk.title('AWOS_DATA_VIEW')
    size_center(tk, 200, 150)
    tk.protocol('WM_DELETE_WINDOW', close_tk)

    var_time = StringVar()
    label_time = Label(tk)
    label_time.place(relx=0.35, rely=0.8)
    label_time.config(textvariable=var_time, fg='#222222', font=('Arial', 13))
    get_time()

    Button(tk, text='数据查找', fg='#111111', command=data_view).pack()
    Button(tk, text='数据监控', fg='#111111', command=monitor).pack()
    Button(tk, text='VIS&RVR', fg='#111111', command=vis_rvr).pack()
    Button(tk, text='定制功能', fg='#111111', command=please_wait).pack()

    mainloop()

########################################################################################################################
print('func \"main\" has run to the end!')
