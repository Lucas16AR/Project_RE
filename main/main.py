import clear
import constants as cs
import functions as ft
import analyzer as an

def main():
    analyzer = an.Analyzer()
    while True:
        clear.clear()
        print(cs.MENU)
        inp = input("")
        inp = inp.lower()
        if inp == '1':
            analyzer.search_sessions_by_user_id()
            ft.return_menu()
        elif inp == '2':
            analyzer.search_sessions_by_date_range_and_user_id()
            ft.return_menu()        
        elif inp == '3':
            analyzer.total_session_time()
            ft.return_menu()
        elif inp == '4':
            analyzer.mac_user_devices()
            ft.return_menu()
        elif inp == '5':
            analyzer.mac_ap_date1()
            ft.return_menu()
        elif inp == '6':
            analyzer.mac_ap_date2()
            ft.return_menu()
        elif inp == '7':
            ft.exit_program()
            break
        elif inp == 'e':
            ft.exit_program()
            break
        else:
            ft.error_menu()

if __name__ == '__main__':
    main()