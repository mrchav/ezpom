import tkinter as tk

import time


class timer():
    def __init__(self):

        self.timer_active = False
        self.left_time = 0
        # self.work_time = 20 * 60
        # self.rest_time = 5 * 60
        self.on_top = 1
        self.WORK_TIME = 11
        self.REST_TIME = 20

        self.timer_type = 'work'



        self.main_window = tk.Tk()
        self.main_window.iconbitmap(None)
        self.main_window.attributes('-topmost', True)
        self.main_window.geometry('400x150')
        self.main_window.configure(bg='#FFFFFF')
        self.main_window.resizable(width=False, height=False)

        self.main_window.title("Easy timer pomodoro")

        self.lb_current_action = tk.Label(self.main_window, text="Time to work", font=("PTSansRegular", 16),bg='#FFFFFF')
        #self.lb_current_action.grid(column=20, row=0, columnspan=30, rowspan=6,  sticky='nesw', padx=10, pady=5)
        self.lb_current_action.place(x=80, y=5)

        self.lb_timer = tk.Label(self.main_window, text=self.true_time_view(self.WORK_TIME), font=("PTSansRegular", 34),bg='#FFFFFF')
        #self.lb_timer.grid(column=20, row=7, columnspan=30, rowspan=6, padx=10, pady=5)
        self.lb_timer.place(x=90, y=40)

        self.btn_start = tk.Button(self.main_window, text="Start", command=self.start_stop, width=10,bg='#FFFFFF')
        #self.btn_start.grid(column=10, row=13,  columnspan=15)
        self.btn_start.place(x=20, y=110)

        self.btn_reset = tk.Button(self.main_window, text="Reset", command=self.but_reset, width=10,bg='#FFFFFF')
        #self.btn_reset.grid(column=30, row=13, columnspan=15)
        self.btn_reset.place(x=120, y=110)

        self.btn_on_top = tk.Button(self.main_window, text="on top", command=self.change_top, width=10,bg='#FFFFDD')
        self.btn_on_top.place(x=280, y=40)

        self.main_process()

    def main_process(self):
        if self.timer_active == 5:
            self.update_time()



        print(self.on_top)
        self.main_window.mainloop()


    def but_reset(self):
        self.timer_active = 0
        self.time_star_timer()
        self.set_data_to_work()
        self.btn_start.configure(text="Start")
        try:
            self.main_window.after_cancel(self.current_timer)
        except:
            print('timer not run')
        self.lb_timer.configure(text=self.true_time_view(self.left_time))


    def change_period(self):
        if self.timer_type == 'work':
            self.set_data_to_rest()

        elif self.timer_type == 'rest':
            self.set_data_to_work()
        self.left_time = self.actual_timer
        self.time_star_timer()


    def start_stop(self):

        if self.timer_active == 5:              #timer active
            print('active')
            self.timer_active = 1
            self.main_window.after_cancel(self.current_timer)
            self.btn_start.configure(text='Resume')

        elif self.timer_active == 0:            # timer is not active and full time left
            self.time_star_timer()
            if self.timer_type == 'work':
                self.actual_timer = self.WORK_TIME
            if self.timer_type == 'rest':
                self.actual_timer = self.REST_TIME
            self.timer_active = 5
            self.btn_start.configure(text='Pause')

        elif self.timer_active == 1:  #timer in pause
            self.resume_timer()
            self.actual_timer = self.left_time
            self.timer_active = 5
            self.btn_start.configure(text='Pause')
            self.resume_timer()

        self.main_process()


    def set_data_to_work(self):
        self.timer_type = 'work'
        self.lb_current_action.configure(text='Time to work')
        self.actual_timer = self.WORK_TIME


    def set_data_to_rest(self):
        self.timer_type = 'rest'
        self.lb_current_action.configure(text='Time to rest')
        self.actual_timer = self.REST_TIME


    def resume_timer(self):
        self.timer_start = time.time()


    def change_top(self):
        if self.on_top == 1:
            self.on_top = 0
            self.main_window.attributes('-topmost', False)
            self.btn_on_top.configure( bg = '#FFFFFF')

        else:
            self.on_top = 1
            self.main_window.attributes('-topmost', True)
            self.btn_on_top.configure(bg='#FFFFDD')



    def change_not_top(self):
        self.main_window.attributes('-topmost', False)

    def time_star_timer(self):
        self.timer_start = time.time()

    def stop_timer(self):
        pass

    def calc_time_left(self):
        #now = round(self.timer_start + self.left_time - time.time())
        self.left_time = round(self.actual_timer + self.timer_start - time.time())
        print(f'self.left_time = {self.left_time}')
        now_min = self.left_time // 60
        if len(str(self.left_time % 60)) < 2:
            now_sek = f'0{self.left_time % 60}'
        else:
            now_sek = self.left_time % 60

        self.time_left_str = f'{now_min}:{now_sek}'
        print(self.timer_active)
        return self.time_left_str

    def true_time_view(self, time):
        now_min = time // 60
        if len(str(time % 60)) < 2:
            now_sek = f'0{time % 60}'
        else:
            now_sek = time % 60

        time_str = f'{now_min}:{now_sek}'
        #print(self.timer_active)
        return time_str

    def update_time(self):
        self.calc_time_left()
        self.lb_timer.configure(text=self.time_left_str)
        if self.left_time < 1: self.change_period()
        #self.main_window.configure(text=now)
        self.current_timer = self.main_window.after(1000, self.update_time)


app = timer()
